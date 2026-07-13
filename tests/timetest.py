# Time Testing File for Parsing Files
# timetest.py
# This module provides functions to test the time taken to parse CSV and Excel files.
# SPDX-License-Identifier: MIT

import statistics
import time
import pandas as pd

def test_large_excel(filepath):
    """
    Tests the time taken to parse a large Excel file using openpyxl and calamine.
    Prints the average time taken for parsing with each engine.
    """
    for engine in ("openpyxl", "calamine"):
        times = []

        for _ in range(10):
            start = time.perf_counter()
            pd.read_excel(filepath, engine=engine)
            times.append(time.perf_counter() - start)

        print(f"Average time taken to parse Excel file '{filepath}' using {engine}: {statistics.mean(times):.4f} seconds")


if __name__ == "__main__":
    test_file_path = input("Enter the path to the Excel file for time testing: ")
    test_large_excel(test_file_path)