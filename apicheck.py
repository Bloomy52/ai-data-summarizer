# apickeck.py
# This file contains functions to check for API keys and token counts for the different model providers.
# SPDX-License-Identifier: MIT

import os   
import sys

import anthropic
from google import genai
from openai import OpenAI

def check_api_keys(provider_choice):
    if provider_choice == 1:
        check_for_gemini_api_key()
        check_valid_gemini_api_key()
    elif provider_choice == 2:
        check_for_openai_api_key()
        check_valid_openai_api_key()
    elif provider_choice == 3:
        check_for_anthropic_api_key()
        check_valid_anthropic_api_key()

def check_for_gemini_api_key():
    if os.getenv("GEMINI_API_KEY") is None or os.getenv("GEMINI_API_KEY") == "":
        print("Error: Gemini API key not found. Please update the .env file with your API key.")
        sys.exit(1)
    else:
        return True
    
def check_valid_gemini_api_key():
    try:
        client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
        # Attempt to list models to check if the API key is valid
        models = client.models.list()
        return True
    except Exception as e:
        print(f"Error: Invalid Gemini API key. Please check your .env file. Details: {e}")
        sys.exit(1)


def check_for_openai_api_key():
    if os.getenv("OPENAI_API_KEY") is None or os.getenv("OPENAI_API_KEY") == "":
        print("Error: OpenAI API key not found. Please update the .env file with your API key.")
        sys.exit(1)
    else:
        return True
    
def check_valid_openai_api_key():
    try:
        client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        # Attempt to list models to check if the API key is valid
        # TODO: Implement correct method to validate OpenAI API key
        return True
    except Exception as e:
        print(f"Error: Invalid OpenAI API key. Please check your .env file. Details: {e}")
        sys.exit(1)


def check_for_anthropic_api_key():
    if os.getenv("ANTHROPIC_API_KEY") is None or os.getenv("ANTHROPIC_API_KEY") == "":
        print("Error: Anthropic API key not found. Please update the .env file with your API key.")
        sys.exit(1)
    else:
        return True
    
def check_valid_anthropic_api_key():
    try:
        client = anthropic.Client(api_key=os.getenv("ANTHROPIC_API_KEY"))
        # Attempt to list models to check if the API key is valid
        # TODO: Implement correct method to validate Anthropic API key
        return True
    except Exception as e:
        print(f"Error: Invalid Anthropic API key. Please check your .env file. Details: {e}")
        sys.exit(1)