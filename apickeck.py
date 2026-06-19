# apickeck.py
# This file contains functions to check for API keys and token counts for the different model providers.
# SPDX-License-Identifier: MIT

import creds
import sys

import anthropic
from google import genai
from openai import OpenAI


def check_gemini_api_key():
    if creds.GEMINI_API_KEY is None or creds.GEMINI_API_KEY == "":
        print("Error: Gemini API key not found. Please update the creds.py file with your API key.")
        sys.exit(1)
    

def check_openai_api_key():
    if creds.OPENAI_API_KEY is None or creds.OPENAI_API_KEY == "":
        print("Error: OpenAI API key not found. Please update the creds.py file with your API key.")
        sys.exit(1)

def check_anthropic_api_key():
    if creds.ANTHROPIC_API_KEY is None or creds.ANTHROPIC_API_KEY == "":
        print("Error: Anthropic API key not found. Please update the creds.py file with your API key.")
        sys.exit(1)