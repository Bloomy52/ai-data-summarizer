from __future__ import annotations

import importlib
import os
import tempfile
from importlib.metadata import PackageNotFoundError, distribution, version
from pathlib import Path

DIST_NAME = "ai-data-summarizer"
EXPECTED_CONSOLE_SCRIPT = "main:main"
REPO_ROOT = Path(__file__).resolve().parents[1]


def run_checks() -> None:
    try:
        _ = version(DIST_NAME)
    except PackageNotFoundError as e:
        raise SystemExit(f"Distribution '{DIST_NAME}' not installed in this environment") from e

    dist = distribution(DIST_NAME)
    console_scripts = {ep.name: ep.value for ep in dist.entry_points if ep.group == "console_scripts"}
    if console_scripts.get("sumdata") != EXPECTED_CONSOLE_SCRIPT:
        raise SystemExit(
            f"Console script 'sumdata' misconfigured: expected {EXPECTED_CONSOLE_SCRIPT!r}, "
            f"found {console_scripts.get('sumdata')!r}"
        )

    # Avoid importing local sources from the repo checkout; import from the installed artifact instead.
    with tempfile.TemporaryDirectory() as td:
        prev_cwd = os.getcwd()
        os.chdir(td)
        try:
            main_mod = importlib.import_module("main")
        finally:
            os.chdir(prev_cwd)

    main_file_str = getattr(main_mod, "__file__", None)
    if not main_file_str:
        raise SystemExit("Imported 'main' module has no __file__ (unexpected)")

    main_file = Path(main_file_str).resolve()
    if main_file.is_relative_to(REPO_ROOT):
        raise SystemExit(f"Imported local module at {main_file}; expected installed distribution module")

    if not callable(getattr(main_mod, "main", None)):
        raise SystemExit("main.main is not callable")


if __name__ == "__main__":
    run_checks()
    print("Smoke test passed")
