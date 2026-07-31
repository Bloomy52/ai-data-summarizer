# Main Code File
# main.py
# Code file containing the main function and the main logic for the AI Data Summarizer program.
# SPDX-License-Identifier: MIT

# Import Statements
import os
import sys
import datetime
import csv

# Import the functions from the summarizer.py helper file
from summarizer import *
from tokenizer import *
from prompt import *
from apicheck import *
from envvar import *
from fileloader import *

# Function Definitions

def get_model_provider():
    while True:
        print("\nSelect a model provider:")
        print("1. Google Gemini")
        print("2. OpenAI")
        print("3. Anthropic")
        choice = input("Enter the number corresponding to your choice: ").strip()

        if choice == '1':
            return 1 # Gemini
        elif choice == '2':
            return 2 # OpenAI
        elif choice == '3':
            return 3 # Anthropic
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

# Main Function
def main():
    # TODO: Implement main function logic
    read_env()  # Read the .env file to set environment variables
    # Main Interactive Loop:
    # Get input file
    while True:
        filepath = input("\nEnter the path to your CSV file: ").strip()

        # Remove quotes if user wrapped path in quotes
        input_file = filepath.strip('"\'')
        

        if not os.path.exists(input_file):
            print(f"Error: File '{input_file}' not found.  Please try again.")
            continue

        if not input_file.lower().endswith('.csv') and not input_file.lower().endswith('.xlsx') and not input_file.lower().endswith('.xls'):
            print("Warning: file extension is not .csv, .xlsx, or .xls. Continue anyway? (y/N)")
            if input().lower() != 'y':
                continue

        break

    file_type = detect_file_type(input_file)
    
    csv_text = load_file(input_file, file_type)  # Load the file (CSV or Excel) and get its content as CSV text
    

    model_provider_choice = 1 # get_model_provider()
                              # Defaults to Gemini since it is the only one provided
    check_api_keys(model_provider_choice)
    prompt_type = get_prompt_type()
    prompt = get_prompt(prompt_type)

    check_tokens_gemini(prompt, csv_text)

    summary = gemini_summarizer(prompt, csv_text, os.path.basename(input_file).split(".")[0], prompt_type)
    print("\nSummary:\n")
    print(summary)

    return None

if __name__ == "__main__":
    main()