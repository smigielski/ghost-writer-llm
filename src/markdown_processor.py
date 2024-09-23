import hashlib
import re
import logging
import utils.unifieddiff as udiff

logger = logging.getLogger(__name__)


class MarkdownProcessor:

    def __init__(self, engine, src=""):
        self.src= src
        self.engine = engine

    def process(self, text):
        logger.debug("Processing markdown...")
        comments_regex = r"<!--\s*([#/].*?)[:\s]+(.*?)\s*-->(\s*\n)?"
        commands_iter = iter(re.finditer(comments_regex, text))

        last_end = 0
        output_text = ""

        command = next(commands_iter, None)

        while command:
            # Get the text between last end and start of current command
            start, end = command.span()
            output_text+=text[last_end:end]
            last_end = end
            # Get the next command
            next_command = next(commands_iter, None)

            func_name = command.group(1)[1:] if "#" == command.group(1)[0] else "close_" + command.group(1)[1:]
            func_args = command.group(2) if command.group(2) else None

            logger.info(f"Command: {func_name}, content: {func_args}")

            if "chat" == func_name:
                current_hash = self.engine.compute_hash(func_args)
                if next_command and "/chat" == next_command.group(1):
                    # If there is a next command and it's a chat command
                    start, end = next_command.span()
                    chat_hash = next_command.group(2)
                    
                    if current_hash == chat_hash:
                        
                        #rewrite
                        output_text+=text[last_end:end]
                        self.engine.update_chat(func_args,text[last_end:start])
                    else:
                        output_text+=self.engine.chat(func_args)
                        output_text+=f"<!-- /chat {current_hash} -->\n"  
                    last_end = end
                    next_command = next(commands_iter, None)
                    #update end to the end of closing chat command
                    # Print text before the matched command and the matched command itself
                else:
                    output_text+=self.engine.chat(func_args)
                    output_text+=f"<!-- /chat {current_hash} -->\n"  
            elif "context" == func_name:
                # Load file specified in func_args
                with open(self.src + "/" + func_args, 'r') as f:
                    context = f.read()
                self.engine.update_chat("Context: "+context)
        
            else:
                engine = self.engine
                output_text+=getattr(engine, func_name)(func_args) if func_args else getattr(engine, func_name)()
            # Next interation
            command = next_command

        # Print any remaining non-matched text after the last match
        if last_end < len(text):
            output_text+=text[last_end:]

        diff = udiff.make_patch(text,output_text)
        logger.debug("Response:\n" + diff)
        return diff
