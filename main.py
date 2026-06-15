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
from tokenizer import *

# Function Definitions

def check_tokens_gemini(text):
    # This function checks the number of tokens to make sure that they are within the Free Tier limits
    google_tokens = google_tokenizer(text)
    if creds.GEMINI_FREE_TIER == True and google_tokens > 250000:
        print(f"Warning: Your input text has {google_tokens} tokens, which exceeds the free tier limit of 250,000 tokens per minute for Gemini. Consider reducing the input size or upgrading your plan.")
    elif creds.GEMINI_FREE_TIER == True:
        print(f"Your input text has {google_tokens} tokens, which is within the free tier limit for Gemini.")
    # TODO (maybe): Add cost functionality to estimate cost of input response


def check_tokens_openai(prompt, text):
    tokens = openai_tokenizer(prompt, text)
    print(f"Your input text has {tokens} tokens.")


def check_tokens_anthropic(prompt, text):
    tokens = anthropic_tokenizer(prompt, text)
    print(f"Your input text has {tokens} tokens.")


# Main Function
def main():
    # TODO: Implement main function logic
    # Main Interactive Loop:
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