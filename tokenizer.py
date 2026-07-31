# Dataset Tokenizer
# tokenizer.py
# Code File for calling the tokenization functions -- Mainly a helper file to keep code organized
# SPDX-License-Identifier: MIT

import os
import sys

from openai import OpenAI
import anthropic
from google import genai
from google.genai import local_tokenizer

# Tokenization Functions
# Google GenAI Tokenizer
def google_tokenizer(prompt, text):
    MODEL_ID = "gemini-3.5-flash"
    client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

    response = client.models.count_tokens(
        model=MODEL_ID,
        contents=[
            text,
            prompt,
        ]
    )
    tokens = response.total_tokens
    return tokens

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
    return None

# OpenAI Tokenizer
def openai_tokenizer(prompt, text):
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    response = client.responses.input_tokens.count(
        model="gpt-5.4-mini",
        instructions=prompt,
        input=text,
    )
    return response.input_tokens


def check_tokens_openai(prompt, text):
    tokens = openai_tokenizer(prompt, text)
    print(f"Your input text has {tokens} tokens.")
    return None

# Anthropic Tokenizer
def anthropic_tokenizer(prompt, text):
    client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
    response = client.messages.count_tokens(
        model="claude-haiku-4-5",
        system=prompt,
        messages=[{"role": "user", "content": text}],
    )
    return response.get("input_tokens", 0)

def check_tokens_anthropic(prompt, text):
    tokens = anthropic_tokenizer(prompt, text)
    print(f"Your input text has {tokens} tokens.")
    return None