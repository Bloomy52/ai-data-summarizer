# Main code file for the AI Data Summarizer project
# SPDX-License-Identifier: MIT

# Import Statements
import creds
import os
import sys
import datetime
import csv

# Import the functions from the summarizer.py helper file
from summarizer import *

# Function Definitions






# Main Function
def main():
    # TODO: Implement main function logic
    # Main Interactive Filename Loop:
    # Get input file
    while True:
        filepath = input("\nEnter the path to your CSV file: ").strip()

        # Remove quotes if user wrapped path in quotes
        input_file = filepath.strip('"\'')

        if not os.path.exists(input_file):
            print(f"Error: File '{input_file}' not found.  Please try again.")
            continue

        if not input_file.lower().endswith('.csv'):
            print("Warning: file extension is not .csv. Continue anyway? (y/n)")
            if input().lower() != 'y':
                continue

        break

    return None

if __name__ == "__main__":
    main()