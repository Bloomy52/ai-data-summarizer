# Dataset File Loader
# fileloader.py
# This module provides functions to load and read CSV files for processing.
# SPDX-License-Identifier: MIT

import os
import sys
import pandas as pd


def detect_file_type(filepath):
    """
    Determines the normalized file type ("csv" or "excel") based on the file extension.
    Raises a ValueError if the extension is not supported.

    Returns: str: "csv" or "excel"
    """
    _, ext = os.path.splitext(filepath)
    ext = ext.lower()

    if ext == ".csv":
        return "csv"
    elif ext in [".xlsx", ".xls"]:
        return "excel"
    else:
        print(f"Unsupported file extension '{ext}'. Supported extensions are: .csv, .xlsx, .xls")
        sys.exit(1)


def get_sheet_names(filepath):
    """
    Returns a list of sheet names if the file is an Excel workbook.
    Returns None for CSV files, since they do not have sheets.

    Returns: list[str] | None
    """
    file_type = detect_file_type(filepath)

    if file_type == "csv":
        return None

    try:
        excel_file = pd.ExcelFile(filepath)
    except Exception as e:
        print(f"Could not read Excel file '{filepath}'. Details: {e}")
        sys.exit(1)

    return excel_file.sheet_names

def choose_sheet(filepath, file_type):
    if file_type == "excel":
        sheet_names = get_sheet_names(filepath)
        if sheet_names is None:
            print(f"Error: Could not retrieve sheet names from Excel file '{filepath}'.")
            sys.exit(1)

        print("\nAvailable sheets:")
        for idx, sheet in enumerate(sheet_names):
            print(f"{idx + 1}. {sheet}")

        while True:
            sheet_choice = input("Enter the number of the sheet you want to load: ").strip()
            try:
                sheet_index = int(sheet_choice) - 1
                if 0 <= sheet_index < len(sheet_names):
                    selected_sheet = sheet_names[sheet_index]
                    break
                else:
                    print("Invalid choice. Please enter a valid number.")
            except Exception as e:
                print(f"Invalid input. Please enter a number. Details: {e}")
                sys.exit(1)

        # Load the selected sheet as CSV text
        try:
            dataframe = pd.read_excel(filepath, sheet_name=selected_sheet)
            csv_text = dataframe.to_csv(index=False)
            return csv_text
        except Exception as e:
            print(f"Error: Could not read the selected sheet '{selected_sheet}' from Excel file '{filepath}'. Details: {e}")
            sys.exit(1)


def load_csv(filepath):
    """
    Loads a CSV file and returns it as normalized CSV-formatted text.

    Returns: str
    """
    try:
        dataframe = pd.read_csv(filepath, thousands=',', decimal='.')
    except Exception as e:
        print(f"Could not read CSV file '{filepath}'. Details: {e}")
        sys.exit(1)

    if dataframe.empty:
        print(f"CSV file '{filepath}' appears to be empty.")
        sys.exit(1)

    return dataframe


def load_excel(filepath, sheet_name=None):
    """
    Loads a single sheet from an Excel file (.xlsx or .xls) and returns it as
    normalized CSV-formatted text. If sheet_name is not provided, the first
    sheet in the workbook is used.

    Returns: str
    """
    try:
        if sheet_name is None:
            available_sheets = get_sheet_names(filepath)
            sheet_name = available_sheets[0]

        dataframe = pd.read_excel(filepath, sheet_name=sheet_name)
    except Exception as e:
        print(f"Could not read Excel file '{filepath}'. Details: {e}")
        sys.exit(1)

    if dataframe.empty:
        print(f"Sheet '{sheet_name}' in file '{filepath}' appears to be empty.")
        sys.exit(1)

    return dataframe


def load_file(filepath, file_type):
    """
    Dispatches to the correct loader based on the file's detected type, and
    returns normalized CSV-formatted text regardless of the original source format.

    sheet_name is only relevant for Excel files. It is ignored for CSV files.

    Returns: str
    """

    if file_type == "csv":
        return load_csv(filepath)
    elif file_type == "excel":
        return load_excel(filepath)
    return None