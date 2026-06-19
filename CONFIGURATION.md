# Configuration

This project uses a `creds.py` file to store your API key(s).


> [!IMPORTANT]
> `creds.py` is included in `.gitignore` and should never be committed to version control. Keep your API keys private.


## Setup

1. Rename `creds_sample.py` to `creds.py`.
2. Open `creds.py` and fill in the API key for the provider you plan to use.

```python
GEMINI_API_KEY = ""
OPENAI_API_KEY = ""
ANTHROPIC_API_KEY = ""
GEMINI_FREE_TIER = True
```

> [!NOTE]
> This project defaults to the Gemini Free Tier being `True`. If you are paying for the Gemini API Key, please change the `GEMINI_FREE_TIER` flag to `False` to remove restrictions.

## Available Keys

| Variable | Provider | Status |
|---|---|---|
| `GEMINI_API_KEY` | Google Gemini | Supported |
| `OPENAI_API_KEY` | OpenAI | Coming soon |
| `ANTHROPIC_API_KEY` | Anthropic Claude | Coming soon |

See [INSTALL.md](INSTALL.md) for instructions on obtaining API keys from each provider.