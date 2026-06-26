# Main code file for the AI Data Summarizer project
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

def check_tokens_gemini(prompt, text):
    # This function checks the number of tokens to make sure that they are within the Free Tier limits
    google_tokens = google_tokenizer(prompt, text)
    if os.getenv("GEMINI_FREE_TIER") == "True" and google_tokens > 250000:
        print(f"Warning: Your input text has {google_tokens} tokens, which exceeds the free tier limit of 250,000 tokens per minute for Gemini. Consider reducing the input size or upgrading your plan. ")
        sys.exit(1)
    elif os.getenv("GEMINI_FREE_TIER") == "True":
        print(f"Your input text has {google_tokens} tokens, which is within the free tier limit for Gemini.")
        print("Would you like to continue? (Y/n)")
        if input().lower() == 'n':
            sys.exit(1)
    # TODO (maybe): Add cost functionality to estimate cost of input response


def check_tokens_openai(prompt, text):
    tokens = openai_tokenizer(prompt, text)
    print(f"Your input text has {tokens} tokens.")


def check_tokens_anthropic(prompt, text):
    tokens = anthropic_tokenizer(prompt, text)
    print(f"Your input text has {tokens} tokens.")

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
    if file_type == "excel":
        sheet_names = get_sheet_names(input_file)
        if sheet_names is None:
            print(f"Error: Could not retrieve sheet names from Excel file '{input_file}'.")
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
            except ValueError:
                print("Invalid input. Please enter a number.")

        # Load the selected sheet as CSV text
        try:
            dataframe = pd.read_excel(input_file, sheet_name=selected_sheet)
            csv_text = dataframe.to_csv(index=False)
        except Exception as e:
            print(f"Error: Could not read the selected sheet '{selected_sheet}' from Excel file '{input_file}'. Details: {e}")
            sys.exit(1)

    csv_text = load_file(input_file)  # Load the file (CSV or Excel) and get its content as CSV text
    

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