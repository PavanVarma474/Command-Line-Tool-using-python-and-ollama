# Text Summarizer using Python and Ollama Qwen2 0.5B Model


### Installation Steps

To use this project, you need to install Ollama and the Qwen2 0.5B model. Follow these steps:

1. **Install Ollama**: Visit Ollama's website at [https://ollama.ai](https://ollama.ai) and download the installer for your operating system.
2. **Verify Installation**: Open a terminal and run the `ollama` command to verify the installation.
3. **Download Qwen2 0.5B Model**: Run `ollama pull qwen2:0.5B` to download the Qwen2 0.5B model.
4. **List Models**: Run `ollama list` to view all the downloaded models.
5. **Run Qwen2 0.5B Model**: Run `ollama run qwen2:0.5` to start the model.
6. The ollama model now starts listenning at localhost:11434.

### Getting the Code Running

To use this project, follow these steps:

1. **Clone the Repository**: Clone this repository to your local machine.
2. **Navigate to Project Folder**: Open a terminal and navigate to the project folder.
3. **Run the Summarizer**: Run one of the following commands to summarize your text:
```bash
python Summarizer.py your_text_to_be_summarized
````
```bash
python Summarizer.py -t filename.txt
````
Replace yourtexttobesummarized with the text you want to summarize, or filename.txt with the path to your text file.
