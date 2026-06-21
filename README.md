# AI Data Summarization Tool
A Python CLI Tool that takes a dataset and uses AI to summarize the data and presents it to the user.

This project is a continuation of my CS178 Final Project. You can find the repo at [Bloomy52/cs178-data-summarizer-py](https://www.github.com/Bloomy52/cs178-data-summarizer-py)


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
> [!NOTE]
> This only supports Gemini at the moment. Support for the Anthropic and OpenAI APIs are coming soon.

- Python
- Git
- Gemini API Key from Google AI Studio

See [INSTALL.md](INSTALL.md) for detailed setup instructions, including how to obtain API keys.


## How to Use

1. Clone the git repository and `cd` into it
```bash
   git clone https://www.github.com/Bloomy52/ai-data-summarizer.git
   cd ai-data-summarizer
```

2. Rename `creds_sample.py` to `creds.py` and add your API key.  
   See [CONFIGURATION.md](CONFIGURATION.md) for details.

3. Install dependencies and run the tool using one of the two options below.

   ### Option A: Install as a package (recommended)
```bash
   pip install .
```
   Then run:
```bash
   ai-summarizer
```

   ### Option B: Run without installing
   **Linux & macOS Users**
```bash
   python3 -m venv .venv
   source .venv/bin/activate
   python3 -m pip install -r requirements.txt
   python3 main.py
```
   **Windows Users**
```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   python -m pip install -r requirements.txt
   python main.py
```

   > [!NOTE]
   > Both options run the same underlying code. Option A installs `ai-summarizer` as a command while Option B runs it directly via `main.py` inside a virtual environment.


   
## License
This project is licensed under the MIT License. The full license text can be found [here](LICENSE)