# Contributing to AI Data Summarization Tool

Thank you for your interest in contributing to the AI Data Summarization Tool! Contributions are welcome, including bug fixes, documentation improvements, tests, usability enhancements, and new summarization capabilities.

## Code of Conduct

Please be respectful and constructive when participating in discussions, reviewing code, or submitting changes. Assume good intentions and focus feedback on improving the project.

## Before You Start

Please check the existing documentation and open issues before beginning work:

- [README.md](README.md) — Project overview and usage
- [INSTALL.md](INSTALL.md) — Installation instructions
- [CONFIGURATION.md](CONFIGURATION.md) — API-key and environment configuration
- [SECURITY.md](SECURITY.md) — Security-related reporting instructions

For significant changes, consider opening an issue first to discuss the proposed approach.

## Development Requirements

The project currently requires:

- Python 3.12 or newer
- Git
- `uv` or `pip`
- An API key for testing AI-powered summaries
- Optional: Docker and Visual Studio Code with the Dev Containers extension

The project currently supports CSV and Excel files through pandas and `openpyxl`.

## Setting Up a Development Environment

1. Fork the repository on GitHub.

2. Clone your fork:

   ```bash
   git clone https://github.com/<your-username>/ai-data-summarizer.git
   cd ai-data-summarizer
   ```

3. Create a branch for your changes:

   ```bash
   git checkout -b feature/short-description
   ```

4. Create and activate a virtual environment.

   Using `uv`:

   ```bash
   uv sync
   ```

   Using Python and `pip`:

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```

   On Windows PowerShell:

   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   pip install -r requirements.txt
   ```

5. Configure your local environment:

   ```bash
   cp .env.sample .env
   ```

   On Windows, copy `.env.sample` to `.env` manually or run:

   ```powershell
   Copy-Item .env.sample .env
   ```

   Add your API key to `.env` as described in [CONFIGURATION.md](CONFIGURATION.md).

   **Never commit `.env`, API keys, or other secrets to the repository.**

## Running the Application

Run the application directly with Python:

```bash
python main.py
```

Or run it through `uv`:

```bash
uv run main.py
```

If the package entry point is available in your environment, you can also run:

```bash
sumdata
```

When testing changes, use small local datasets whenever possible. The files in the `examples/` directory can be used for development and manual testing.

## Running Tests

Run the test suite with:

```bash
pytest
```

Or, when using `uv`:

```bash
uv run pytest
```

Before submitting a pull request:

- Run all existing tests.
- Add or update tests for changed behavior.
- Verify that the application still starts successfully.
- Test both expected input and invalid input where practical.
- Confirm that generated summaries and files are written to the expected locations.

If a change requires an API call, keep tests deterministic by avoiding unnecessary live API requests. Prefer mocking external services or testing the data-processing logic separately.

## Making Changes

The main modules are organized as follows:

| File | Purpose |
|---|---|
| `main.py` | CLI entry point and application flow |
| `summarizer.py` | AI summarization functionality |
| `prompt.py` | Prompt templates and prompt management |
| `tokenizer.py` | Token counting and token-management utilities |
| `fileloader.py` | CSV and Excel file loading |
| `profiler.py` | Dataset profiling and pandas summaries |
| `apicheck.py` | API configuration validation |
| `envvar.py` | Environment-variable loading |

When making changes:

- Keep changes focused and avoid unrelated refactoring.
- Preserve the command-line interface unless the change specifically targets it.
- Handle invalid files, missing configuration, and API failures gracefully.
- Avoid logging API keys, credentials, or sensitive dataset contents.
- Prefer clear, maintainable Python over overly complex abstractions.
- Update documentation when user-facing behavior changes.
- Keep generated files, local environments, and temporary output out of commits.

## Data and Privacy

This project processes user-provided datasets and may send dataset summaries or related content to an external AI provider.

Contributors must:

- Never commit private or confidential datasets.
- Use synthetic, anonymized, or already-public data in examples and tests.
- Avoid including real API keys in source code, tests, documentation, screenshots, or issue reports.
- Clearly document any new behavior that sends data to an external service.
- Consider whether error messages could expose sensitive file contents.

## Documentation Changes

Documentation improvements are welcome. Please keep documentation:

- Accurate for Python 3.12 and the current dependency setup.
- Consistent with the actual CLI behavior.
- Clear for both technical and non-technical users.
- Free of private credentials and sensitive example data.

If you add a new example dataset or output, explain its purpose and confirm that it can be legally and safely distributed.

## Commit Guidelines

Use clear commit messages that describe the change. Examples:

```text
Add validation for unsupported file types
Fix token-limit warning in Gemini summarization
Update installation instructions for Windows
Add tests for CSV loading
```

Keep each commit focused on one logical change when practical.

## Pull Requests

Before opening a pull request:

1. Rebase or update your branch with the latest changes from the default branch.
2. Run the test suite.
3. Review your changes for accidental secrets or unrelated files.
4. Update relevant documentation.
5. Confirm that generated files and local configuration files are not included.

A pull request description should include:

- A summary of the change.
- The motivation or problem being addressed.
- How the change was tested.
- Any limitations, follow-up work, or known issues.
- Screenshots or example output for user-facing changes, when useful.

Keep pull requests focused and reasonably sized so they can be reviewed efficiently.

## Reporting Bugs

When reporting a bug, include:

- A clear description of the problem.
- Steps to reproduce it.
- Your operating system.
- Your Python version.
- The installation method used (`uv`, `pip`, Docker, or package installation).
- A minimal, sanitized example dataset or input description.
- The full error message or traceback, with secrets and private data removed.

Please do not include API keys or confidential datasets in issues.

## Suggesting Features

Feature requests are welcome. Please describe:

- The problem the feature would solve.
- The proposed user experience.
- Example commands or expected output.
- Whether the change affects supported providers, file formats, prompts, or configuration.
- Any compatibility or privacy considerations.

## License

By contributing to this project, you agree that your contributions will be licensed under the project's [MIT License](LICENSE).
