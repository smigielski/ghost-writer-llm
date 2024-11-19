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
## Leveraging Markdown and LLM
Ghost LLM enhances markdown by integrating a Human-to-LLM interface. This seamless fusion enables users to:

* Write hidden comments in markdown files
* Trigger LLM-generated content based on these comments
* Review and refine the output for accuracy
<!-- /chat 7e2e8d6c -->
<!-- #chat in fact this README file was create like that. In order to see it check raw content -->
# Raw Markdown Content
## Example of Hidden Comments
```markdown
# Ghost LLM: A Markdown Automation Tool
## Description
Ghost LLM is a powerful AI-driven tool designed to accelerate documentation creation by leveraging hidden comments in markdown files.

### Key Features
* **Markdown Processing**: Automatically generates content from markdown files based on hidden comments.
* **Documentation Speedup**: Streamlines the documentation process, saving time and effort for writers and developers alike.

## Why Ghost LLM?
## Bridging the Gap
Documentation creation takes significantly more time than reading, yet readers are more invested in consuming content. I built Ghost LLM to bridge this gap by automating documentation generation from markdown files.

## Additional Challenge
## Language Barriers
Non-native English speakers struggle with writing correct English, leading to delayed or abandoned documentation efforts. Ghost LLM aims to alleviate this issue by generating clear and concise content.

## How Ghost LLM Works
## Leveraging Markdown and LLM
Ghost LLM enhances markdown by integrating a Human-to-LLM interface. This seamless fusion enables users to:

* Write hidden comments in markdown files
* Trigger LLM-generated content based on these comments
* Review and refine the output for accuracy

### Example of Hidden Comments
* What is Ghost LLM?
  ~~~
  A tool that helps with documentation creation.
  ~~~
* Why do we need Ghost LLM?
  ~~~
  To make documentation faster to create, without sacrificing quality.
  ~~~
```
<!-- /chat a04b6035 -->
<!-- #chat Regarding "what". First thing is to install Ollama based on https://ollama.com/ -->
# Installing OLLAMA
## Step 1: Set up OLLAMA
To use Ghost LLM, you need to set up an OLLAMA instance. Follow these steps:

### 1. Create an account on ollama.com
Sign up for a free account on the official OLLAMA website.

### 2. Install the OLLAMA CLI
Run `npm install -g @ollama/cli` in your terminal to install the OLLAMA Command-Line Interface (CLI).

### 3. Login to OLLAMA using the CLI
Use the `ollama login` command to authenticate with your OLLAMA account.

### 4. Create a new model
Run `ollama create-model --name ghost-llm` to set up a new OLLAMA model for Ghost LLM.

That's it! Your OLLAMA instance is now ready to use with Ghost LLM.
<!-- /chat 1a965738 -->
<!-- #chat Next is to decide which model will be used. Model need to be provided just after command like #model <model_name:version> -->
# Specifying the OLLAMA Model
## Adding a Model Identifier
To select a specific OLLAMA model for Ghost LLM, you need to specify the model name and version immediately after the `ollama` command. For example:

```bash
ollama --model ghost-llm:latest <your_markdown_file.md>
```

Replace `<your_markdown_file.md>` with the actual path to your markdown file. This will trigger Ghost LLM to generate content based on the provided markdown and hidden comments, using the specified OLLAMA model.
<!-- /chat e7b0f5fd -->
<!-- #chat then set system message like: "#system You are professional technical writer. Don't print what you do. Print output as markdown. Give short text." -->
# System Message
## Guidelines for Interaction
You are a professional technical writer.
Don't write out your actions.
Print the output in markdown format.
Keep your responses concise.
<!-- /chat ce984e77 -->

<!-- #chat in order to ask for content generate use "#chat message". and that's it -->
# Generating Content
## Using Ghost LLM
Type `#chat What is Ghost LLM?` to trigger the generation of content based on the hidden comments in your markdown file, using the specified OLLAMA model.
<!-- /chat 8408c66f -->

<!-- #chat there is also #converstation <name>, to start new conversation context. #context <src> to embed files from project, #seed <number> to set fixed seed for all the conversations -->
# Conversation Management
## Contextualizing Conversations
To manage conversational context:

* `#conversation <name>`: Start a new conversation context.
* `#context <path>`: Embed a file from your project into the conversation.
* `#seed <number>`: Set a fixed seed for all conversations, ensuring reproducibility.
<!-- /chat 5f49d7c1 -->

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
