<!-- #model llama3.1:latest -->
<!-- #system You are professional technical writer. Don't print what you do. Print output as markdown. Give short text. -->
<!-- #chat Ghost LLM is ghost writer that process markdown files based on the hidden comments in oder to speed up documentation creation -->

**Ghost LLM**

A ghost writing tool designed for processing Markdown files, utilizing hidden comments to accelerate documentation creation.
### Key Features

* **Efficient Documentation Creation**: Streamlines documentation processes by leveraging AI-driven capabilities.
* **Markdown File Support**: Works directly with Markdown files, making it a seamless fit for writers and developers alike.
* **Hidden Comments Utilization**: Employs hidden comments within Markdown files to inform Ghost LLM's content generation process.
<!-- /chat bb689363 -->
<!-- #chat Explain "Why". Writing documentation is much longer then reading it whereas this is reader who is more interested in the documentation. I developed Ghost LLM in order to fight this discrepency. Make this shorter -->

**Addressing the Documentation Discrepancy**

Documentation creation is a time-consuming process, often taking more time to write than read. To bridge this gap, **Ghost LLM** was developed to assist writers in generating content based on hidden comments within Markdown files, saving precious time and effort.
<!-- /chat 3eec5f58 -->
<!-- #chat also writing correct english for non native english speekers further slow down them or even fully stopped -->

**Breaking the Language Barrier**

Non-native English speakers often struggle with writing accurate English, hindering their ability to create documentation. **Ghost LLM** aims to alleviate this issue by generating content in proper English, freeing writers from language-related constraints and allowing them to focus on conveying information effectively.
<!-- /chat ef4b2e5e -->
<!-- #chat Explain "How". Having this in mind, there is no easier way then just using markdown itself, enhance it with human to llm interaface in order to generate text. -->
**Harnessing Markdown's Power**

To overcome the challenges of documentation creation, **Ghost LLM** builds upon the simplicity of Markdown by integrating a human-LLM interface.
### The Approach

1.  **Markdown as Input**: Utilize Markdown files with hidden comments containing information and context for content generation.
2.  **Human-LLM Interface**: Provide an intuitive interface where users can interact with the LLM, fine-tuning generated text to meet their specific needs.
3.  **Generated Text**: Produce high-quality, proper English content based on user input and Markdown file data.

By leveraging Markdown's flexibility and a human-friendly interface, **Ghost LLM** streamlines documentation creation, making it more efficient and accessible.
<!-- /chat e695657e -->
<!-- #chat in fact this README file was create like that. In order to see it check raw content -->
**Behind-the-Scenes**

This very README file was indeed created using **Ghost LLM**, showcasing its capabilities in generating Markdown content from scratch. To witness the process, simply view the raw content of this file. The interaction between human input and LLM-driven generation is seamlessly woven into the Markdown formatting.
### A Glimpse Inside

Raw content reveals a blend of user-inputted comments and AI-generated text, demonstrating how **Ghost LLM** enables efficient documentation creation.
<!-- /chat 7e44d91e -->
<!-- #chat Regarding "what". First thing is to install Ollama based on https://ollama.com/ -->

**Getting Started with Ghost LLM**

To begin leveraging **Ghost LLM**, the first step is to set up Ollama, a Large Language Model (LLM) that serves as the core technology behind **Ghost LLM**.
### Installing Ollama

1.  **Visit Ollama's Website**: Go to https://ollama.com/ and explore the platform.
2.  **Sign Up or Log In**: Create an account on Ollama, if you haven't already.
3.  **Install Ollama**: Follow the instructions provided by Ollama to install their LLM on your machine.

By completing these steps, you'll be ready to integrate Ollama with **Ghost LLM** and start generating Markdown content efficiently.
<!-- /chat fc7750e9 -->
<!-- #chat Next is to decide which model will be used. Model need to be provided just after command like #model <model_name:version> -->

**Model Selection Made Easy**

To efficiently generate Markdown content with **Ghost LLM**, choose the right Ollama model by specifying it after commands, like this:
### #model Directive

Use `#model` followed by `<model_name>:<version>` to select a suitable model for your needs.

*   **Example:** `#model llama:large`
*   **Format:** `<command> #model <model_name>:<version>`
*   **Tips:**
    *   Replace `<model_name>` with the actual Ollama model name.
    *   Specify the corresponding `<version>` number for accurate results.

By selecting a suitable model, you can optimize **Ghost LLM**'s performance and tailor it to your specific documentation creation needs.
<!-- /chat b3a09c0d -->
<!-- #chat then set system message like: "#system You are professional technical writer. Don't print what you do. Print output as markdown. Give short text." -->

**Configuring System Messages**

To fine-tune **Ghost LLM**, configure a system message that sets the tone for interactions.
### #system Directive

Use `#system` to define a message that will be displayed before each command execution.

*   **Example:** `#system You are a professional developer. Print output as markdown.`
*   **Format:** `<command> #system <message>`
*   **Tips:**
    *   Replace `<message>` with the desired system message.
    *   This directive can be used to provide context or instructions for users.

By setting a clear and concise system message, you can establish expectations and guide users through their interactions with **Ghost LLM**.
<!-- /chat ca9af031 -->

<!-- #chat in order to ask for content generate use "#chat message". and that's it -->

**Starting the Content Generation Process**

To initiate content generation using **Ghost LLM**, simply use the `#chat` directive followed by your message.
### #chat Directive

*   **Format:** `<command> #chat <message>`
*   **Example:** `#chat I need a short text about Ghost LLM.`
*   **Purpose:** This directive triggers the content generation process based on the provided message.

With this straightforward approach, you can easily ask **Ghost LLM** to generate Markdown content tailored to your needs.
### Example Output

Generated markdown content will be printed out as a result of using `#chat` directive.
<!-- /chat c9ccf191 -->

<!-- #chat there is also #converstation <name>, to start new conversation context. #context <src> to embed files from project, #seed <number> to set fixed seed for all the conversations -->

**Enhancing Conversational Flow with Additional Directives**

To further enrich interactions with **Ghost LLM**, consider utilizing the following directives:
### #conversation Directive

*   **Format:** `<command> #conversation <name>`
*   **Example:** `#chat I need a short text about Ghost LLM.` #conversation documentation
*   **Purpose:** This directive initiates a new conversation context, allowing you to separate discussions and preserve their specific settings.

### #context Directive

*   **Format:** `<command> #context <src>`
*   **Example:** `#chat I need a short text about Ghost LLM.` #context ./project/README.md
*   **Purpose:** This directive embeds files from your project, enabling you to incorporate existing content into the conversation.

### #seed Directive

*   **Format:** `<command> #seed <number>`
*   **Example:** `#chat I need a short text about Ghost LLM.` #seed 42
*   **Purpose:** This directive sets a fixed seed for all conversations, ensuring consistent results across different discussions.

By leveraging these directives, you can customize and optimize your interactions with **Ghost LLM**, tailoring the experience to suit your specific needs.
<!-- /chat 11a5ae60 -->

<!-- #conversation usuage -->
<!-- #context ./src/ghost_llm.py -->
<!-- #chat generate how to use ghost_llm.py -->
Here is a Markdown formatted guide on how to use `ghost_llm.py`:

**Using Ghost LLM**

You can use Ghost LLM in three different ways:

### 1. Process Markdown files without watching for changes

To process Markdown files in the specified source directory without watching for changes, run the following command:
```bash
python ghost_llm.py /path/to/source/directory [-r|--recursive] [--dry-run]
```
*   `-r` or `--recursive` : Recursively search for markdown files in the specified source directory.
*   `--dry-run`: Run without making changes.

Example:
```bash
python ghost_llm.py /path/to/source/directory -r --dry-run
```

### 2. Watch a directory for changes and re-process Markdown files

To watch a directory for changes and re-process Markdown files, run the following command:
```bash
python ghost_llm.py /path/to/source/directory [-r|--recursive] [--watch]
```
*   `-r` or `--recursive`: Recursively search for markdown files in the specified source directory.
*   `--watch`: Watch the specified source directory for changes and re-process Markdown files as needed.

Example:
```bash
python ghost_llm.py /path/to/source/directory -r --watch
```

### 3. Specify Ollama server URL

You can also specify the Ollama server URL to use by passing it as an argument like so:

```bash
python ghost_llm.py /path/to/source/directory [-r|--recursive] [--dry-run|--watch] (--ollama=OLLAMA_SERVER_URL)
```

Example:
```bash
python ghost_llm.py /path/to/source/directory -r --watch --ollama=https://your-ollama-server.com
```
Note that you need to have the `OLLAMA_SERVER_URL` set up correctly for this to work.
<!-- /chat 26afd806 -->
<!-- /conversation -->

<!-- #chat just to finish what is the best it does not upload your text anywhere, it works fully offline so you can work with that even in the plane. -->
To summarize:

**Ghost LLM's Unique Selling Point**

*   **Fully Offline Operation**: Ghost LLM runs entirely on your local machine, without any online dependencies. This means you can use it in airplanes, coffee shops, or anywhere else without worrying about internet connectivity.
*   **Private and Secure**: Since all processing happens locally, your text data remains private and secure, without being transmitted to any servers.

This makes Ghost LLM an excellent choice for anyone who values their privacy, works with sensitive information, or simply wants a seamless writing experience without distractions.
<!-- /chat 8b108c29 -->
<!-- #generated by https://github.com/smigielski/ghost-writer-llm -->
---
Generated by: [ghost-writer-llm](https://github.com/smigielski/ghost-writer-llm)
<!-- /generated -->
