<!-- #model llama3.1:latest -->
<!-- #system output markdown but limit answer to few sentences -->
<!-- #chat Ghost llm is ghost writer that process markdown files exactly like this one-->

**Ghost LLM: A Markdown Ghost Writer**

This AI-powered tool processes and generates Markdown files with ease, replicating the exact format of this document. It can take in Markdown content, analyze its structure, and produce similar or identical output, making it a useful ghost writer for editing and creating Markdown files.
<!-- /chat 2c72b0cc -->
<!-- #chat it does it thanks to command that are hidden in the comments -->**Ghost LLM's Secret Power**

It uses specific commands embedded within the **comments** of the Markdown file, allowing Ghost LLM to understand and replicate the formatting. These hidden commands trigger the AI to perform various actions, such as preserving the original formatting, adding or removing elements, and more.
<!-- /chat fe27afb9 -->
<!-- #chat you can use : seed, model, system, conversation, chat and context -->
**Ghost LLM's Hidden Commands**

You can utilize the following commands in comments to control Ghost LLM:

* `:seed`: Set a specific input or prompt for the AI.
* `:model`: Specify which language model to use for processing.
* `:system`: Configure system-specific settings, such as formatting or syntax.
* `:conversation`: Engage in a conversation-like interaction with the AI.
* `:chat`: Trigger a chat-like interface for interacting with the AI.
* `:context`: Provide context for the AI to better understand the surrounding text.
<!-- /chat 6c4261ff -->
<!-- #chat seed set the seed for the llm so you get consisten results other the runs -->
**Consistent Results with :seed**

Using `:seed` in a comment sets a specific seed value for the Large Language Model (LLM), which ensures consistent results across multiple runs. This means that if you run the same input through Ghost LLM multiple times, you'll get identical output, as long as the seed remains the same.
<!-- /chat 5a228b39 -->
<!-- #chat model tells Ollama server which model to load -->
**Model Selection with :model**

Using `:model` in a comment instructs the Ollama server to load and use a specific language model for processing, allowing you to switch between different models as needed. This command enables flexibility and control over which model is used for generation or analysis tasks.
<!-- /chat ed67c8ee -->
<!-- #chat system set system message that sets how ollama should respond -->
**System Messages with :system**

Using `:system` in a comment allows you to set system messages that instruct Ollama on how to respond in specific situations, such as custom error messages or warnings. This command gives you fine-grained control over the output and behavior of the AI.
<!-- /chat c26b85e7 -->
<!-- #chat conversation can group messages together -->
**Conversational Groups with :conversation**

Using `:conversation` in a comment enables grouping related messages together, allowing Ollama to understand the context and flow of a conversation. This command helps the AI identify themes, tone, and intent within a series of messages, making it more conversational and contextual.
<!-- /chat 84900a0d -->
<!-- #chat chat provide information to llm what to do -->
**Chat Commands with :chat**

Using `:chat` in a comment provides direct instructions to Ollama on how to proceed or respond to specific inputs, acting as a kind of "chat command" that overrides default behavior. This allows you to explicitly tell the AI what to do in a particular situation.
<!-- /chat 906250cc -->
<!-- #conversation ghost_llm -->
<!-- #context: ./src/ghost_llm.py -->
<!-- #chat describe all the cli interface -->
Here is a description of the CLI interface:

**Available Arguments:**

* `src`: The source directory to process. This is a required argument.
* `-r` or `--recursive`: A flag that tells the script to recursively search for Markdown files in the specified source directory. If not provided, only top-level Markdown files will be processed.
* `--dry-run`: A flag that tells the script to run without making changes to the original Markdown files. This is mutually exclusive with `-w` or `--watch`.
* `-w` or `--watch`: A flag that tells the script to watch the specified source directory for changes and re-process Markdown files as needed.
* `--ollama`: The URL of the Ollama server to use. If not provided, no Ollama server will be used.

**Example Usage:**

To process a single Markdown file in the current directory without making changes:
```
python script.py src_file.md
```

To process all Markdown files in the `src` directory recursively and make changes:
```bash
python script.py /path/to/src --recursive
```

To watch the `src` directory for changes and re-process Markdown files as needed:
```
python script.py /path/to/src -w
```

To use an Ollama server with a specific URL:
```
python script.py /path/to/src --ollama https://example.com/ollama
```
<!-- /chat ef408743 -->
<!-- /conversation -->
