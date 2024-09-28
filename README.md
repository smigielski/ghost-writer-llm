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
**Ghost LLM Commands**

You can control Ghost LLM's behavior by adding commands in comments, including:

* `:seed` - Set input or prompt
* `:model` - Specify language model
* `:system` - Configure system settings
* `:conversation` - Engage in conversation-like interaction
* `:chat` - Trigger chat interface
* `:context` - Provide context for AI understanding
<!-- /chat bb621713 -->
<!-- #chat seed set the seed for the llm so you get consisten results other the runs -->
**Consistent Results with :seed**

The `:seed` command allows you to set a specific value, ensuring **consistent results** across multiple runs of the AI. This means that even if you process the same input multiple times, Ghost LLM will always produce the **same output**, giving you predictable and reliable results.
 
Example:
```markdown
:seed 1234
```
This sets the seed to 1234, ensuring consistent output on subsequent runs.
<!-- /chat 6cf560c1 -->
<!-- #chat model tells Ollama server which model to load -->
**Easy Model Switching**

Use `:model` command to **switch between models**, allowing you to:

* Load specific models (`llama`, `bloom`, etc.)
* Experiment with different models for diverse tasks
* Adapt to changing requirements by switching between models.

Example:
```markdown
:model llama
```
 Loads the LLaMA model.
<!-- /chat 382df494 -->
<!-- #chat system set system message that sets how ollama should respond -->
**Fine-Tuning Ollama with :system**

Use `:system` command to **set custom system messages**, allowing you to:

* Control how Ollama responds in various situations
* Provide clear and concise answers
* Adapt the AI's behavior to specific needs and requirements.

Example:
```markdown
:system "I'm not sure what you mean."
```
 Sets a custom response for when Ollama is unsure about a question or statement.
<!-- /chat 2b205881 -->
<!-- #chat conversation can group messages together -->
**Grouping Messages with :conversation**

Use `:conversation` to **group related messages**, enabling Ghost LLM to:

* Recognize context and connections between messages
* Understand the flow of conversation and relationships between ideas
* Provide more cohesive, relevant, and contextual responses.

Example:
```markdown
:conversation "Discuss AI ethics"
```
 Groups subsequent messages under the topic of discussing AI ethics.
<!-- /chat b6d0d88c -->
<!-- #chat chat provide information to llm what to do -->
**Explicit Control with :chat**

The `:chat` command gives you **explicit control** over Ollama, allowing you to:

* Dictate specific responses or outputs
* Update the AI's behavior in real-time
* Customize interactions with explicit commands.

Example:
```markdown
:chat "tell me a joke"
```
 Tells Ollama to respond with a joke.
<!-- /chat 4f525208 -->
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
<!-- #generated -->
---
Generated by: [ghost-writer-llm](https://github.com/smigielski/ghost-writer-llm)
<!-- /generated -->
