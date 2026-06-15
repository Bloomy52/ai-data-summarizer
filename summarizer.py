# Code File for calling the summarization functions -- Mainly a helper file to keep code organized
# SPDX-License-Identifier: MIT

# Import Statements
import creds
import os
import sys
import datetime
import csv

# Importing AI Libraries
from openai import OpenAI
import anthropic
from google import genai
from google.genai import types


# Function Definitions
# TODO: Implement summarization functions here

# Gemini Summarizer
def gemini_summarizer(prompt, text, filename):
    client = genai.Client(api_key=creds.GEMINI_API_KEY)

    MODEL_ID = "gemini-3.5-flash"

    response = client.models.generate_content(
        model=MODEL_ID,
        contents=[
            text,
            prompt,
        ]
    )
    output = response.text

    summary_local_path = f"/summaries/{MODEL_ID}.{filename}.txt"
    with open(summary_local_path, "w") as outfile:
        outfile.write(output)
    return output