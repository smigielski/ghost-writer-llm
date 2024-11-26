<!-- #model llama3.1:latest -->
<!-- #system You are professional technical writer. Don't print what you do. Print output as markdown. Give as short answers as possible. -->
<!-- #chat Ghost LLM is ghost writer that process markdown files based on the hidden comments in oder to speed up documentation creation -->
**What is Ghost LLM?**
====================

A collaborative AI tool for generating documentation content from markdown files, using hidden comments as input.

**How does it work?**
--------------------

Processes markdown files with embedded comments, allowing for faster and more efficient documentation creation. 

**Key Benefits:**
---------------

*   Speeds up documentation creation
*   Utilizes AI-powered generation capabilities 
*   Supports markdown file format
<!-- /chat 898f44f1 -->
<!-- #chat Explain "Why". Writing documentation is much longer then reading it whereas this is reader who is more interested in the documentation. I developed Ghost LLM in order to fight this discrepency. Make this shorter -->
**The Problem:**
--------------

Writing documentation takes significantly longer than reading it.

**Ghost LLM Solution:**
-------------------

Aim to benefit the reader, not just the writer, by leveraging AI to automate documentation creation, bridging the efficiency gap.
<!-- /chat f2f30ce1 -->
<!-- #chat also writing correct english for non native english speekers further slow down them or even fully stopped -->
**The Additional Challenge:**
---------------------------

Non-native English writers struggle with language accuracy, further slowing down documentation creation.

**Ghost LLM Helps:**
------------------

Provides AI-powered language assistance to ensure accurate and polished content, enabling smoother documentation creation.
<!-- /chat e10e1392 -->
<!-- #chat Explain "How". Having this in mind, there is no easier way then just using markdown itself, enhance it with human to llm interaface in order to generate text. -->
**The Approach:**
--------------

*   **Leverage Markdown**: Build upon the existing markdown format, making it easy to integrate and maintain.
*   **Human-LLM Interface**: Create a seamless interaction between humans and LLMs, enabling writers to provide context and guidance.

**Ghost LLM's Core Functionality:**
---------------------------------

Enhance markdown files with hidden comments that serve as input for the LLM.
<!-- /chat c165af7f -->
<!-- #chat in fact this README file was create like that. In order to see it check raw content -->
**Raw Markdown Content:**
-------------------------

```markdown
# Ghost LLM - A Collaborative AI Tool for Documentation Generation

## Problem Statement
Writing documentation takes significantly longer than reading it.

## Solution Overview
Aim to benefit the reader, not just the writer, by leveraging AI to automate documentation creation, bridging the efficiency gap.

## Additional Challenge
Non-native English writers struggle with language accuracy, further slowing down documentation creation.

## How It Works
Leverage Markdown, enhance it with human-LLM interface in order to generate text. Build upon existing format, make easy to integrate and maintain.

## Core Functionality
Enhance markdown files with hidden comments that serve as input for LLM.
```

**Note:** This README file is a prime example of how Ghost LLM can be used to create documentation content directly within the Markdown file itself!
<!-- /chat 2ba32175 -->
<!-- #chat Regarding "what". First thing is to install Ollama based on https://ollama.com/ -->
**Getting Started:**
-------------------

1.  **Install Ollama**: Follow the instructions on the official website (https://ollama.com/) to set up the LLM model.
2.  **Integrate with Markdown**: Enhance markdown files by adding hidden comments that serve as input for Ollama, enabling AI-powered content generation.
<!-- /chat b4214e5f -->
<!-- #chat Next is to decide which model will be used. Model need to be provided just after command like #model <model_name:version> -->
**Model Selection:**
------------------

*   **Specify the Model**: Use a command like `#model <model_name:version>` to select the desired LLM model.
*   **Example Usage**: Include the model specification directly within the markdown file, e.g., `#model llama:1.3`
<!-- /chat 66f306db -->
<!-- #chat then set system message like: "#system You are professional technical writer. Don't print what you do. Print output as markdown. Give short text." -->
**System Message:**
------------------

```markdown
#system
You are a professional technical writer.
Don't write out instructions or explanations.
Instead, provide concise and to-the-point answers.
Format your response in Markdown, keeping it brief and clear.
```

*   **Example Response**: Use this system message as a reminder to keep responses concise, formatted in Markdown, and focused on the essential information.
<!-- /chat 5d0542b3 -->

<!-- #chat in order to ask for content generate use "#chat message". and that's it -->
**Content Generation:**
---------------------

*   **Request Content**: Simply add `#chat message` to initiate a conversation with Ollama.
*   **Example Usage**: Use this command directly within the markdown file, followed by your message, e.g., `#chat What is Ghost LLM?`.
<!-- /chat 0cce389d -->

<!-- #chat there is also #converstation <name>, to start new conversation context. #context <src> to embed files from project, #seed <number> to set fixed seed for all the conversations -->
**Additional Commands:**
----------------------

*   **#conversation <name>**: Start a new conversation context.
*   **#context <src>**: Embed external files into the current conversation context.
*   **#seed <number>**: Set a fixed seed value to ensure reproducibility across conversations.
<!-- /chat 7ee8cdaf -->

<!-- #conversation usuage -->
<!-- #context ./src/ghost_llm.py -->
<!-- #chat generate how to use ghost_llm.py -->
## How to Use Ghost LLM
### Command Line Interface

You can run `ghost_llm.py` from the command line using the following options:

#### Required Option
* `src`: The source directory containing Markdown files.

#### Optional Options
* `-r`, `--recursive`: Recursively search for Markdown files in the specified source directory.
* `--dry-run`: Run without making changes to existing Markdown files.
* `-w`, `--watch`: Watch the specified source directory for changes and re-process Markdown files as needed.
* `--ollama`: URL of Ollama server to use.

### Example Usage

#### Process all Markdown files in a directory
```
python ghost_llm.py /path/to/markdown/files --recursive
```

#### Run without making changes (dry run)
```
python ghost_llm.py /path/to/markdown/files --recursive --dry-run
```

#### Watch the source directory for changes and re-process Markdown files as needed
```
python ghost_llm.py /path/to/markdown/files -r
```

#### Specify Ollama server URL (optional)
```
python ghost_llm.py /path/to/markdown/files --ollama https://example.com/ollama
```
<!-- /chat 2e42564a -->
<!-- /conversation -->

<!-- #chat just to finish what is the best it does not upload your text anywhere, it works fully offline so you can work with that even in the plane. -->
To highlight the key benefits of `ghost_llm.py`, here's a summary:

**Ghost LLM: Offline Markdown Processing**

* **Offline operation**: Process Markdown files without any internet connection required.
* **Local processing**: All text processing happens on your local machine, ensuring complete control and security over your data.
* **Plane-friendly**: Work with Markdown files anywhere, anytime, even in areas with no internet access.

These benefits make `ghost_llm.py` an ideal choice for:

* Writers and authors who want to focus on their craft without worrying about internet connectivity.
* Researchers and students who need to work with large datasets or sensitive information offline.
* Anyone who values the security and convenience of local data processing.
<!-- /chat 5ca02750 -->
<!-- #generated by https://github.com/smigielski/ghost-writer-llm -->
---
Generated by: [ghost-writer-llm](https://github.com/smigielski/ghost-writer-llm)
<!-- /generated -->
