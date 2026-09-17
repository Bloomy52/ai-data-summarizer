from importlib.metadata import version

import main


def run_checks() -> None:
    assert version("ai-data-summarizer")
    assert callable(main.main)


if __name__ == "__main__":
    run_checks()
    print("Smoke test passed")
