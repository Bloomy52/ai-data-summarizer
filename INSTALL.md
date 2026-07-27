# Installation
## Python
This project utilizes Python 3.12. You can download Python at the following download link [https://www.python.org/downloads/](https://www.python.org/downloads/). Click the yellow button to download the latest version of Python for your OS, and install the Python Interpreter.

> [!IMPORTANT]
> **Windows Users**: Make sure that the Python Interpreter was added to the Path environment variable. When going through the installer, there should be an option in the Python installer that says "Add to Path." Make sure that option is checked. If you don't check the box, the following commands when running the code will not work!


## API Keys
This project utilizes AI API Keys. You may use any model you please as long as you have the correct API Key. Google has a very generous Free API, so I will be basing the rest of this project off of that, but I will include support for the OpenAI and Anthropic API Libraries. You can find documentation for how to get API Keys in the API Keys section below.

### Getting API Keys
- **Gemini**: Go to [Google AI Studio](https://aistudio.google.com). Login with your Google Account and Click Dashboard. Click "Create API Key", fill out the information and click create. Copy this key and add it to your `.env` file.
- **OpenAI**: Go to the [OpenAI API Docs](https://developers.openai.com/api/docs). Click "Create API Key", login to the OpenAI API Portal. Click "Create new secret key", add a name (optional), then click "Create secret key." Copy the key and add it to your `.env` file.
- **Anthropic**: Go to the [Claude API Docs](https://platform.claude.com/docs/en/home). Click "Get API Key", login with your Claude Developer Account, click "Create key", add a name, then click "Add." Copy this key and add it to your `.env` file.


## Git
This project utilizes Git. Please install Git according to your OS. 
### Windows
Go to [https://git-scm.com/install/windows](https://git-scm.com/install/windows) and use one of the options to install Git for Windows.

### macOS
Go to [https://git-scm.com/install/mac](https://git-scm.com/install/mac) and use one of the following options to install Git. I recommend using Homebrew [https://www.brew.sh](https://www.brew.sh).

### Linux
Go to [https://git-scm.com/install/linux](https://git-scm.com/install/linux) and follow the instructions for your specific Linux Distribution.

## uv
This project utilizes the [uv](https://docs.astral.sh/uv/) Python Package and Project Manager. You can install it from PyPI with the following command.
```bash
pip install uv
```
More installation information and options are available at [https://docs.astral.sh/uv/getting-started/installation/](https://docs.astral.sh/uv/getting-started/installation/).

## Docker
If you don't want to install Python on your computer, you can run this program in a Docker container. 

### macOS
**Make sure you have Homebrew installed** [https://www.brew.sh](https://www.brew.sh).
```bash
brew install docker colima
colima start
```

### Linux
**This will depend on your distribution, but I will list the way to do it using `apt`.**
```bash
sudo apt update
sudo apt install -y docker.io
```

### Windows
To use the Docker Engine on Windows, we need to install Docker Desktop. You can install Docker Desktop here: [https://docs.docker.com/desktop/setup/install/windows-install/](https://docs.docker.com/desktop/setup/install/windows-install/).