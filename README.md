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
- API Key from Google AI Studio

See [INSTALL.md](INSTALL.md) for detailed setup instructions, including how to obtain API keys.


## How to Use

1. Clone the git repository and `cd` into it
   ```bash
   git clone https://www.github.com/Bloomy52/ai-data-summarizer.git
   cd ai-data-summarizer
   ```
2. Initialize and Activate your Python Virtual Environment  
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
3. **TODO: Move to a different file and then implement `pyproject.toml` usage instructions**   
Install the requirements using `pip`. You can use one of the following methods depending on your OS.  
   **Linux & macOS Users**
   ```bash
   python3 -m pip install -r requirements.txt
   ```
   **Windows Users**
   ```cmd
   python -m pip install -r requirements.txt
   ```

   You can also use `uv` if you would like. If you would like to use uv, use the following commands:
   **Linux & macOS Users**
   ```bash
   python3 -m pip install uv
   uv pip install -r requirements.txt
   ```
   **Windows Users**
   ```cmd
   python -m pip install uv
   uv pip install -r requirements.txt
   ```

4. Rename `creds_sample.py` to `creds.py` and set up your `creds.py` file with your API key.
   See [CONFIGURATION.md](CONFIGURATION.md) for details.

5. Run the CLI using the following command based on your OS. 
   **Linux & macOS Users**
   ```bash
   python3 main.py
   ```
   **Windows Users**
   ```cmd
   python main.py
   ```


   
## License
This project is licensed under the MIT License. The full license text can be found [here](LICENSE)