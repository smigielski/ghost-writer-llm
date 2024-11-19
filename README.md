<!-- #model llama3.1:latest -->
<!-- #system You are professional technical writer. Don't print what you do. Print output as markdown. Give as short answers as possible. -->
<!-- #chat Ghost LLM is ghost writer that process markdown files based on the hidden comments in oder to speed up documentation creation -->
# Ghost LLM: A Markdown Automation Tool
## Description
Ghost LLM is a powerful AI-driven tool designed to accelerate documentation creation by leveraging hidden comments in markdown files.

### Key Features

* **Markdown Processing**: Automatically generates content from markdown files based on hidden comments.
* **Documentation Speedup**: Streamlines the documentation process, saving time and effort for writers and developers alike.
<!-- /chat 7f4a41d7 -->
<!-- #chat Explain "Why". Writing documentation is much longer then reading it whereas this is reader who is more interested in the documentation. I developed Ghost LLM in order to fight this discrepency. Make this shorter -->
# Why Ghost LLM?
## Bridging the Gap
Documentation creation takes significantly more time than reading, yet readers are more invested in consuming content. I built Ghost LLM to bridge this gap by automating documentation generation from markdown files.
<!-- /chat a31c8aec -->
<!-- #chat also writing correct english for non native english speekers further slow down them or even fully stopped -->
# Additional Challenge
## Language Barriers
Non-native English speakers struggle with writing correct English, leading to delayed or abandoned documentation efforts. Ghost LLM aims to alleviate this issue by generating clear and concise content.
<!-- /chat 6a068673 -->
<!-- #chat Explain "How". Having this in mind, there is no easier way then just using markdown itself, enhance it with human to llm interaface in order to generate text. -->
# How Ghost LLM Works
## Leveraging Markdown & Human-LLM Interface
Ghost LLM enhances Markdown by integrating a human-LLM interface, allowing users to:

* Add hidden comments within Markdown files
* Interact with the LLM through a simple interface
* Generate high-quality text based on markdown content and user input
<!-- /chat 5eb8336f -->
<!-- #chat in fact this README file was create like that. In order to see it check raw content -->
# Creating Readme Files
## The Ghost LLM Process
This very README file demonstrates the process:

1. Initial Markdown with hidden comments (only visible in Raw mode)
2. Human-LLM interface used to interact with Ghost LLM
3. Generated text based on markdown content and user input
<!-- /chat d50f09a7 -->
<!-- #chat Regarding "what". First thing is to install Ollama based on https://ollama.com/ -->
# Getting Started with Ghost LLM
## Installing Ollama
1. Go to [https://ollama.com/](https://ollama.com/)
2. Follow the instructions to install and set up Ollama, which is the core Large Language Model used by Ghost LLM.
<!-- /chat be434ad1 -->
<!-- #chat Next is to decide which model will be used. Model need to be provided just after command like #model <model_name:version> -->
# Configuring Ghost LLM
## Choosing a Model
Specify the desired Ollama model using:

`#model <model_name:version>`

Example:
`#model x-large:1.0`
<!-- /chat 0876eeba -->
<!-- #chat then set system message like: "#system You are professional technical writer. Don't print what you do. Print output as markdown. Give short text." -->
# System Message
## Ghost LLM Instructions
`#system`
You are a professional technical writer.
Don't print what you do.
Print output as Markdown.
Give answers in short text.
<!-- /chat c9b0ce96 -->

<!-- #chat in order to ask for content generate use "#chat message". and that's it -->
# Starting the Conversation
## Generating Content
Type your request using:

`#chat message`

Example:
`#chat Write a brief introduction about Ghost LLM.`
<!-- /chat 8f59aeb8 -->

<!-- #chat there is also #converstation <name>, to start new conversation context. #context <src> to embed files from project, #seed <number> to set fixed seed for all the conversations -->
# Advanced Commands
## Conversation Management

* `#conversation <name>`: Start a new conversation context.
* `#context <src>`: Embed files from the project into conversations.
* `#seed <number>`: Set a fixed seed for all conversations, ensuring reproducibility.
<!-- /chat bd860f6a -->

<!-- #conversation usuage -->
<!-- #context ./src/ghost_llm.py -->
<!-- #chat generate how to use ghost_llm.py -->
## How to Use `ghost_llm.py`

### Command Line Interface (CLI)

You can run `ghost_llm.py` from the command line with various options.

#### Required Argument: `src`

* Specify the source directory where markdown files are located. The `-r` or `--recursive` option can be used in conjunction to search recursively.
```markdown
$ python ghost_llm.py /path/to/source/directory
```
#### Optional Arguments:

* `-r`, `--recursive`: Recursively search for markdown files in the specified source directory.
* `--dry-run`: Run without making changes. Useful for testing and debugging.
* `-w`, `--watch`: Watch the specified source directory for changes and re-process Markdown files as needed.

Example:
```markdown
$ python ghost_llm.py /path/to/source/directory -r --dry-run
```
or
```markdown
$ python ghost_llm.py /path/to/source/directory -w
```

### Environment Variable: `OLLAMA_URL`

* Set the environment variable `OLLAMA_URL` to specify the URL of Ollama server to use.

Example:
```bash
$ export OLLAMA_URL="https://your-ollama-server.com"
$ python ghost_llm.py /path/to/source/directory
```
Note: The OLLAMA_URL environment variable is required if you want to use a custom Ollama server.
<!-- /chat 6380cc81 -->
<!-- /conversation -->

<!-- #chat just to finish what is the best it does not upload your text anywhere, it works fully offline so you can work with that even in the plane. -->
The `ghost_llm.py` script is designed to be a completely offline, self-contained tool for generating content using AI. It doesn't require an internet connection or any online services, which makes it perfect for use on planes, trains, or anywhere else you might not have reliable internet access.

This offline-only design also means that your text and generated content remain private and secure, without being uploaded to any servers or databases. This is a major advantage for writers who value their intellectual property and want to maintain control over their work.

Overall, the `ghost_llm.py` script offers an excellent solution for writers and content creators who need a reliable, offline tool for generating ideas and text. Its flexibility and portability make it a great companion for any writing project!
<!-- /chat 7f8047df -->
<!-- #generated by https://github.com/smigielski/ghost-writer-llm -->
---
Generated by: [ghost-writer-llm](https://github.com/smigielski/ghost-writer-llm)
<!-- /generated -->
