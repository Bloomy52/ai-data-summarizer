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
from google.genai import local_tokenizer

prompt = # TODO: Add prompt here

# Function Definitions
# TODO: Implement summarization functions here


# Tokenization Functios
# Google GenAI Tokenizer
def google_tokenizer(text):
    client = genai.Client(api_key=creds.GEMINI_API_KEY)
    tokenizer = local_tokenizer.LocalTokenizer(model_name='gemini-3.5-flash')
    result = tokenizer.count_tokens(text)
    return result

# OpenAI Tokenizer
def openai_tokenizer(prompt, text):
    client = OpenAI(api_key=creds.OPENAI_API_KEY)
    response = client.responses.input_tokens.count(
    model="gpt-5.4-mini",
    instructions=prompt,
    input=text,
)
    return response.input_tokens
    

