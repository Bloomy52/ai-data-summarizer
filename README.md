# AI Data Summarization Tool
A Python CLI Tool that takes a dataset and uses AI to summarize the data and presents it to the user.

This project is a continuation of my CS178 Final Project. You can find the repo at [Bloomy52/cs178-data-summarizer-py](https://www.github.com/Bloomy52/cs178-data-summarizer-tool)


## Repo Structure
The structure of this git repository is as follows:
```text
ai-data-summarizer/
├── main.py                 # CLI entry point and main application logic
├── summarizer.py           # Core data summarization functionality
├── prompt.py               # Prompt templates and management
├── tokenizer.py            # Token counting and management utilities
├── creds_sample.py         # Sample credentials file (rename to creds.py)
├── requirements.txt        # Python dependencies
├── README.md               # Project documentation
├── LICENSE                 # MIT License
├── .gitignore              # Git ignore rules
├── .vscode/
│   └── settings.json       # VSCode configuration
└── examples/
    ├── CTA_Ridership_RedLine_WrigleyField_DailyTotals.csv  # Sample dataset
    └── CTA_Ridership_RedLine_WrigleyField_DailyTotals.txt  # Sample summary
```

## Project Requirements
### Python
This project utilizes Python 3.12. You can download Python at the following download link [https://www.python.org/downloads/](https://www.python.org/downloads/). Click the yellow button to download the latest version of Python for your OS, and install the Python Interpreter.

> [!IMPORTANT]
> **Windows Users**: Make sure that the Python Interpreter was added to the Path environment variable. When going through the installer, there should be an option in the Python installer that says "Add to Path." Make sure that option is checked. If you don't check the box, the following commands when running the code will not work!


### API Keys
This project utilizes AI API Keys. You may use any model you please as long as you have the correct API Key. Google has a very generous Free API, so I will be basing the rest of this project off of that, but I will include support for the OpenAI and Anthropic API Libraries. You can find documentation for how to get API Keys in the API Keys section below.

#### Getting API Keys
- **Gemini**: Go to [Google AI Studio](https://aistudio.google.com). Login with your Google Account and Click Dashboard. Click "Create API Key", fill out the information and click create. Copy this key and add it to your `creds.py` file.
- **OpenAI**: Go to the [OpenAI API Docs](https://developers.openai.com/api/docs). Click "Create API Key", login to the OpenAI API Portal. Click "Create new secret key", add a name (optional), then click "Create secret key." Copy the key and add it to your `creds.py` file.
- **Anthropic**: Go to the [Claude API Docs](https://platform.claude.com/docs/en/home). Click "Get API Key", login with your Claude Developer Account, click "Create key", add a name, then click "Add." Copy this key and add it to your `creds.py` file.


### Git
This project utilizes Git. Please install Git according to your OS. 
#### Windows
Go to [https://git-scm.com/install/windows](https://git-scm.com/install/windows) and use one of the options to install Git for Windows.

#### macOS
Go to [https://git-scm.com/install/mac](https://git-scm.com/install/mac) and use one of the following options to install Git. I recommend using Homebrew [https://www.brew.sh](https://www.brew.sh).

#### Linux
Go to [https://git-scm.com/install/linux](https://git-scm.com/install/linux) and follow the instructions for your specific Linux Distribution.


## How to Use
> [!NOTE]
> This only supports Gemini at the moment. Support for the Anthropic and OpenAI APIs are coming soon.

1. Clone the git repository and `cd` into it
   ```bash
   git clone https://www.github.com/Bloomy52/ai-data-summarizer.git
   cd ai-data-summarizer
   ```
2. Initalize and Activate your Python Virtual Environment  
   **Linux and macOS Users**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```
   **Windows Users**
   ```cmd
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```
3. Install the requirements using `pip`. You can use one of the following methods depending on your OS.  
   **Linux & macOS Users**
   ```bash
   python3 -m pip install -r requirements.txt
   ```
   **Windows Users**
   ```cmd
   python -m pip install -r requirements.txt
   ```
5. Add your environment variables to the `creds.py` file.  
> [!IMPORTANT]  
> Make sure to rename the `creds_sample.py` file to `creds.py`. The program will not work otherwise.
6. Run the CLI using the following command based on your OS
   **Linux & macOS Users**
   ```bash
   python3 main.py
   ```
   **Windows Users**
   ```cmd
   python main.py
   ```


   
