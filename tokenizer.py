import creds

from openai import OpenAI
import anthropic
from google import genai
from google.genai import types
from google.genai import local_tokenizer

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

# Anthropic Tokenizer
def anthropic_tokenizer(prompt, text):
    client = anthropic.Anthropic(api_key=creds.ANTHROPIC_API_KEY)
    response = client.messages.count_tokens(
        model="claude-haiku-4-5",
        system=prompt,
        messages=[{"role": "user", "content": text}],
    )
    return response.get("input_tokens", 0)

