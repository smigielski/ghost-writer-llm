import hashlib
import re
import logging
import time
import utils.unifieddiff as udiff
from lark import Lark, Token, Tree

logger = logging.getLogger(__name__)


class MarkdownProcessor:

    def __init__(self, engine, src=""):
        self.src= src
        self.engine = engine
        with open('./src/command_grammar.lark') as grammar_file:
            self.parser = Lark(grammar_file.read(), start='start')

    def get_func_from_children(self,children):
        #pass
        func_name = children[2].value
        func_args = children[4].value if len(children)>4 and children[4].type == 'COMMAND_TEXT' else None
        return func_name,func_args
    
    def get_content(self,tree):
        if isinstance(tree, Tree):
            return ''.join(self.get_content(child) for child in tree.children)
        elif isinstance(tree, Token) and tree.type in ('TEXT','INLINE','MULTILINE', 'WS'):      
            return tree.value  # Leaf node in the tree, just return its value (text content)
        else:
            return ""
            

    def rewrite_text(self,tree):
        if isinstance(tree, Tree):
            return ''.join(self.rewrite_text(child) for child in tree.children)
        elif isinstance(tree, Token):              
            return tree.value  # Leaf node in the tree, just return its value (text content)

    def recover_text(self,tree):
            if isinstance(tree, Tree):                
                if tree.data.value == 'opening_command':
                    func_name,func_args = self.get_func_from_children(tree.children)                        
                    output_text=getattr(self.engine, func_name)(func_args) if func_args else getattr(self.engine, func_name)()                    
                    return output_text + "".join(self.recover_text(child) for child in tree.children)
                elif tree.data.value == 'closing_command':
                    func_name,func_args = self.get_func_from_children(tree.children)
                    func_name = 'close_'+ func_name
                    output_text=getattr(self.engine, func_name)(func_args) if func_args else getattr(self.engine, func_name)()                    
                    return output_text + "".join(self.recover_text(child) for child in tree.children)
                elif tree.data.value == 'opening_chat':                    
                    func_name,func_args = self.get_func_from_children(tree.children)
                    current_hash = self.engine.compute_hash(func_args)
                    output_text=self.engine.chat(func_args)
                    output_text+=f"<!-- /chat {current_hash} -->\n" 
                    return "".join(self.recover_text(child) for child in tree.children) + output_text
                elif tree.data.value == 'chat':   
                    func_name,func_args = self.get_func_from_children(tree.children[0].children)
                    current_hash = self.engine.compute_hash(func_args)                    
                    _,chat_hash = self.get_func_from_children(tree.children[-1].children)
                                    
                    if current_hash == chat_hash:
                        self.engine.update_chat(func_args,response=self.get_content(tree))
                        return self.rewrite_text(tree)                    
                    output_text=self.engine.chat(func_args)
                    output_text+=f"<!-- /chat {current_hash} -->\n" 
                    return "".join(self.recover_text(child) for child in tree.children[0].children) + output_text          
                elif tree.data.value == 'opening_context':
                    func_name,func_args = self.get_func_from_children(tree.children)                            
                    
                    # func_args finsh with jpg or png
                    
                    if func_args.endswith("png") or func_args.endswith("jpg"):
                        self.engine.update_image(self.src + func_args)
                    else:
                        with open(self.src + func_args, 'r') as f:
                            context = f.read()
                        self.engine.update_chat("Context: "+context)
                    return "".join(self.recover_text(child) for child in tree.children)
                else:
                    return "".join(self.recover_text(child) for child in tree.children)
            elif isinstance(tree, Token):              
                return tree.value  # Leaf node in the tree, just return its value (text content)

    def process(self, text):
        logger.debug("Processing markdown...")

        tree = self.parser.parse(text)

        output_text = self.recover_text(tree)
        diff = udiff.make_patch(text,output_text)
        logger.debug("Response:\n" + diff)
        return diff


    def process2(self, text):
        logger.debug("Processing markdown...")

        comments_regex = r"<!--\s*([#/].*?)[:\s]+(.*?)\s*-->(\s*\n)?"
        commands_iter = iter(re.finditer(comments_regex, text))

        last_end = 0
        generated = False
        modified = False
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
                    current_text = text[last_end:start]
                    if current_hash == chat_hash:
                        
                        #rewrite
                        output_text+=text[last_end:end]
                        self.engine.update_chat(func_args,current_text)
                    else:
                        modified = True
                        output_text+=self.engine.chat(func_args,current_text)
                        output_text+=f"<!-- /chat {current_hash} -->\n"  
                    last_end = end
                    next_command = next(commands_iter, None)
                    #update end to the end of closing chat command
                    # Print text before the matched command and the matched command itself
                else:
                    modified = True
                    output_text+=self.engine.chat(func_args)
                    output_text+=f"<!-- /chat {current_hash} -->\n"  
            elif "context" == func_name:
                # Load file specified in func_args
                with open(self.src + func_args, 'r') as f:
                    context = f.read()
                self.engine.update_chat("Context: "+context)
            elif "generated" == func_name:
                generated = True
                if next_command and "/generated" == next_command.group(1):                    
                    start, end = next_command.span()
                    if modified:
                        output_text+=self.__generated_by_message()
                    else:
                        #rewrite
                        output_text+=text[last_end:end]
                    last_end = end
                    next_command = next(commands_iter, None)
                else:
                    output_text+=self.__generated_by_message()
            else:
                engine = self.engine
                output_text+=getattr(engine, func_name)(func_args) if func_args else getattr(engine, func_name)()
            # Next interation
            command = next_command

        # Print any remaining non-matched text after the last match
        if last_end < len(text):
            output_text+=text[last_end:]

        if modified and not generated:
            # Add generated by comment message to the end of the text
            output_text+=self.__generated_by_message()

        diff = udiff.make_patch(text,output_text)
        logger.debug("Response:\n" + diff)
        return diff

    def __generated_by_message(self):
        text=f"<!-- #generated by https://github.com/smigielski/ghost-writer-llm -->\n"        
        text+="---\n"
        text+=f"Generated by: [ghost-writer-llm](https://github.com/smigielski/ghost-writer-llm)\n"
        text+=f"<!-- /generated -->\n"
        return text
