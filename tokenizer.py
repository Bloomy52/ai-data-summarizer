# Code File for calling the tokenization functions -- Mainly a helper file to keep code organized
# SPDX-License-Identifier: MIT

import os

from openai import OpenAI
import anthropic
from google import genai
from google.genai import local_tokenizer

# Tokenization Functios
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

# OpenAI Tokenizer
def openai_tokenizer(prompt, text):
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    response = client.responses.input_tokens.count(
        model="gpt-5.4-mini",
        instructions=prompt,
        input=text,
    )
    return response.input_tokens

# Anthropic Tokenizer
def anthropic_tokenizer(prompt, text):
    client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
    response = client.messages.count_tokens(
        model="claude-haiku-4-5",
        system=prompt,
        messages=[{"role": "user", "content": text}],
    )
    return response.get("input_tokens", 0)

