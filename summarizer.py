# Dataset Summarizer
# summarizer.py
# Code File for calling the summarization functions -- Mainly a helper file to keep code organized
# SPDX-License-Identifier: MIT

# Import Statements
import os
import sys
from zoneinfo import ZoneInfo
import datetime as dt
import csv

# Importing AI Libraries
from openai import OpenAI
import anthropic
from google import genai
from google.genai import types


# Function Definitions
# TODO: Implement summarization functions here

# Write File Function
def write_outfile(output, filename, prompt_type, model_id):
    # Create summaries directory if it doesn't exist
    summaries_dir = f"./summaries/{prompt_type}"
    os.makedirs(summaries_dir, exist_ok=True)
    
    now = dt.datetime.now()
    date_time_string = now.strftime("%Y-%m-%d %H-%M-%S")
    central_tz = ZoneInfo("America/Chicago")
    date_written = dt.datetime.now(central_tz).strftime("%A, %B %d, %Y")
    time_written = dt.datetime.now(central_tz).strftime("%I:%M %p %Z")
    summary_local_path = f"{summaries_dir}/{date_time_string}.{filename}.{model_id}.txt"
    with open(summary_local_path, "w", encoding="utf-8") as outfile:
        # Add Header Section to the output file
        outfile.write("=" * 10 + "BEGIN HEADER" + "=" * 10 + "\n")
        outfile.write("Date Written: " + date_written + "\n")
        outfile.write("Time Written: " + time_written + "\n")
        outfile.write("Model Used: " + model_id + "\n")
        outfile.write("Prompt Type: " + prompt_type + "\n")
        outfile.write("File Name: " + filename + "\n")
        outfile.write("=" * 10 + "END HEADER" + "=" * 10 + "\n\n")
        
        # Add main summary output to the output file
        outfile.write(output)
    
    return None

# Gemini Summarizer
def gemini_summarizer(prompt, text, filename, prompt_type):
    MODEL_ID = "gemini-3.5-flash"
    try:
        client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

        response = client.models.generate_content(
            model=MODEL_ID,
            contents=[
                text,
                prompt,
            ]
        )
        output = response.text
    except Exception as e:
        print(f"Error generating summary: {e}")
        sys.exit(1)
    
    write_outfile(output, filename, prompt_type, MODEL_ID)
    return output


def openai_summarizer(prompt, text, filename, prompt_type):
    MODEL_ID = "gpt-5.4-mini"
    try:
        client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

        response = client.response.create(
            model=MODEL_ID,
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt + "\n\n" + text},
            ],
        )
        output = response.choices[0].message.content
    except Exception as e:
        print(f"Error generating summary: {e}")
        sys.exit(1)
    
    write_outfile(output, filename, prompt_type, MODEL_ID)
    return output

def anthropic_summarizer(prompt, text, filename, prompt_type):
    MODEL_ID = "claude-haiku-4-5"
    try:
        client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

        response = client.completions.create(
            model=MODEL_ID,
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt + "\n\n" + text},
            ],
        )
        output = response.completion
    except Exception as e:
        print(f"Error generating summary: {e}")
        sys.exit(1)
    
    write_outfile(output, filename, prompt_type, MODEL_ID)
    return output