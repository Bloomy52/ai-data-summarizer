# AI Data Summarization Tool
A Python Tool that takes a dataset and uses Artifical Intelligence (AI) to summarize the data and presents it to the user.

This project is a continuation of my CS178 Final Project. You can find the repo at [Bloomy52/cs178-data-summarizer-py](https://www.github.com/Bloomy52/cs178-data-summarizer-py)

### Why This Exists
I created this project because I found that it is difficult to understand what an underlying dataset is and what it entails without reading and understanding the full dataset. I found that using a Large Language Model (LLM) to summarize the dataset made the dataset more approachable since I had a general understanding of what the dataset was and some features about said dataset I was analyzing. I specifically crafted the summary templates so they would help the user understand the dataset and its features. It can also give you a heads up if there are any concerns or anomalies before you start fully analyzing the data to prevent issues and to guide the user on the right path to analysis. 

## Repo Structure
The structure of this git repository is as follows:
```text
ai-data-summarizer/
├── main.py                 # CLI entry point and main application logic
├── summarizer.py           # Core data summarization functionality
├── prompt.py               # Prompt templates and management
├── tokenizer.py            # Token counting and management utilities
├── .env.sample             # Sample credentials file (rename to .env)
├── apicheck.py             # Checks API variables to prevent early issues
├── requirements.txt        # Python dependencies
├── README.md               # Project documentation
├── INSTALL.md              # Project installation documentation
├── CONFIGURATION.md        # Project configuration documentation
├── LICENSE                 # MIT License
├── .gitignore              # Git ignore rules
├── pyproject.toml          # Python project application configuration files
├── .vscode/
│   └── settings.json       # VSCode configuration
├── summaries/              # Summary output folder -- gets created upon first output summary         
└── examples/
    ├── CTA_Ridership_RedLine_WrigleyField_DailyTotals.csv                 # Sample dataset
    └── OverviewPrompt_CTA_Ridership_RedLine_WrigleyField_DailyTotals.txt  # Sample summary
```

## Example
The example used here is the number of daily riders from the Addison 'L' Stop on the Chicago Transit Authority's (CTA) Red Line using the Data Overview prompt. More information about the original dataset can be found at the bottom of the README. Other prompts will be added to the example folder as well.

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

Summaries save to the `summaries` folder. It will be created automatically with the subfolder with the prompt and a header in the file.

> [!TIP]
> The capital `Y` means that it is the default option. You can click the `Enter`/`Return` key as a shortcut.


## Project Requirements
> [!NOTE]
> This only supports Gemini at the moment. Support for the Anthropic and OpenAI APIs are coming soon.

- Python
- uv
- Git
- Gemini API Key from Google AI Studio

See [INSTALL.md](INSTALL.md) for detailed setup instructions, including how to obtain API keys.


## How to Use/Installation
There are three options for running this program. Please choose one of these options.

### Option A: Install as a package (recommended)
```bash
   uv tool install git+https://www.github.com/Bloomy52/ai-data-summarizer.git
```
   Then run:
```bash
   ai-summarizer
```

### Option B: Run without installing
1. Clone the git repository and `cd` into it
```bash
   git clone https://www.github.com/Bloomy52/ai-data-summarizer.git
   cd ai-data-summarizer
```

2. Rename `.env.sample` to `.env` and add your API key.  
   See [CONFIGURATION.md](CONFIGURATION.md) for details.

3. Run the tool with uv
```bash
uv run main.py
```

### Option C: Manually run without installing 
1. Clone the git repository and `cd` into it
```bash
   git clone https://www.github.com/Bloomy52/ai-data-summarizer.git
   cd ai-data-summarizer
```

2. Rename `.env.sample` to `.env` and add your API key.  
   See [CONFIGURATION.md](CONFIGURATION.md) for details.

3. Install dependencies and run the tool according to your OS

**Linux & macOS Users**
```bash
uv venv
source .venv/bin/activate
uv pip install -r requirements.txt
python3 main.py
```
**Windows Users**
```powershell
uv venv
.\.venv\Scripts\Activate.ps1
uv pip install -r requirements.txt
python main.py
```

> [!NOTE]
> All three options run the same underlying code. Option A installs `ai-summarizer` as a command while Options B & C run it directly via `main.py` inside a virtual environment. 


   
## License
This project is licensed under the MIT License. The full license text can be found [here](LICENSE)

*The original data came from the City of Chicago's Data Portal. You can find the original dataset link [here](https://data.cityofchicago.org/Transportation/CTA-Ridership-L-Station-Entries-Daily-Totals/5neh-572f/about_data)