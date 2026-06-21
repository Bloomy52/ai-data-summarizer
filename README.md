# AI Data Summarization Tool
A Python CLI Tool that takes a dataset and uses AI to summarize the data and presents it to the user.

This project is a continuation of my CS178 Final Project. You can find the repo at [Bloomy52/cs178-data-summarizer-py](https://www.github.com/Bloomy52/cs178-data-summarizer-py)

## Example
The example used here is the number of daily riders from the Addison 'L' Stop on the Chicago Transit Authrotiy's (CTA) Red Line using the Data Overview prompt. More information about the original dataset can be found at the bottom of the README. Other prompts will be added to the example folder as well.

**CSV File Structure**
```csv
"date","daytype","rides"
"01/01/2001","U","1,227"
"01/02/2001","W","3,937"
"01/03/2001","W","4,329"
"01/04/2001","W","4,607"
"01/05/2001","W","4,666"
```
* `date` is when the data was recorded
* `daytype` is the type of day of which the data was recorded
   - `W` is a weekday
   - `A` is a Saturday
   - `U` is Sunday/Holidays
* `rides` is the number of riders recorded on a given day

```bash
ai-summarizer
```
```text
Enter the path to your CSV file: examples/CTA_Ridership_RedLine_WrigleyField_DailyTotals.csv

Please Select a Summary:
1. TL;DR Summary
2. Data Overview
3. Deep Dive Analysis
Enter the number corresponding to your choice: 2
Your input text has 195174 tokens, which is within the free tier limit for Gemini.
Would you like to continue? (Y/n)
Y

Summary:

Overview:

I reviewed the dataset you shared. It contains daily transit ride tracking data spanning over 25 years, from 
January 1, 2001, to March 31, 2026. This extensive daily record captures long-term ridership trends and reveals 
how public transit usage fluctuates across weekdays, weekends, and holidays, alongside the long-term impact 
of major external disruptions.

```
The rest of the example can be found in the `examples` folder labeled [OverviewPrompt_CTA_Ridership_RedLine_WrigleyField_DailyTotals.txt](examples/OverviewPrompt_CTA_Ridership_RedLine_WrigleyField_DailyTotals.txt)

Summaries save to the `summaries` folder. It will be automatically be created with the subfolder with the prompt and a header in the file.

> [!TIP]
> The capital `Y` means that it is the default option. You can click the `Enter`/`Return` key as a shortcut.

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

*The original data came from the City of Chicago's Data Portal.