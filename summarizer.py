# Code File for calling the summarization functions -- Mainly a helper file to keep code organized
# SPDX-License-Identifier: MIT

# Import Statements
import creds
import os
import sys
import datetime
import csv

# Importing AI Libraries
import openai
import anthropic
from google import genai
from google.genai import types
from google.genai import local_tokenizer

# Function Definitions
# TODO: Implement summarization functions here

geminiClient = genai.Client(api_key='GEMINI_API_KEY')


# Tokenization Functios
# Google GenAI Tokenizer
def google_tokenizer(text):
    tokenizer = local_tokenizer.LocalTokenizer(model_name='gemini-3.5-flash')
    result = tokenizer.count_tokens(text)
    return result



