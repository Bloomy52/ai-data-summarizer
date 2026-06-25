# Environment Variable Management
# envvar.py
# This file contains functions to manage environment variables, including reading and writing to the .env file
# SPDX-License-Identifier: MIT

import os
import getpass


def _strip_quotes(value):
    # Remove a single matching pair of surrounding quotes (single or double), if present.
    value = value.strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in ('"', "'"):
        return value[1:-1]
    return value


def write_env_value(env_path, key_name, value):
    # Update key_name's value in the .env file in place, preserving other lines.
    # If key_name isn't found in the file, it gets appended.
    lines = []
    if os.path.exists(env_path):
        with open(env_path, "r") as env_file:
            lines = env_file.readlines()

    found = False
    for i, line in enumerate(lines):
        stripped = line.strip()
        if "=" in stripped and not stripped.startswith("#"):
            existing_key = stripped.split("=", 1)[0].strip()
            if existing_key == key_name:
                lines[i] = f"{key_name}={value}\n"
                found = True
                break

    if not found:
        lines.append(f"{key_name}={value}\n")

    with open(env_path, "w") as env_file:
        env_file.writelines(lines)


def create_env():
    # Create a .env file if it doesn't exist
    base_dir = os.path.dirname(os.path.abspath(__file__))
    env_path = os.path.join(base_dir, ".env")
    # Check if the .env file exists
    if not os.path.exists(env_path):
        # have system create a .env file with default values
        with open(env_path, "w") as env_file:
            env_file.write("GEMINI_API_KEY=\n")
            env_file.write("OPENAI_API_KEY=\n")
            env_file.write("ANTHROPIC_API_KEY=\n")
            env_file.write("GEMINI_FREE_TIER=True\n") # TODO: Remove Free Tier Flag and make that hardcoded
    
    return None

def read_env():
    # read full .env and set environment variables
    base_dir = os.path.dirname(os.path.abspath(__file__))
    env_path = os.path.join(base_dir, ".env")
    if not os.path.exists(env_path):
        create_env()
    if os.path.exists(env_path):
        with open(env_path, "r") as env_file:
            for line in env_file:
                if "=" in line:
                    key, value = line.strip().split("=", 1)
                    value = _strip_quotes(value)
                    os.environ[key.strip()] = value
    return None

def set_api_keys(model_provider_choice):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    env_path = os.path.join(base_dir, ".env")   

    # Select the appropriate API key based on the model provider choice
    if model_provider_choice == 1:
        api_key_name = "GEMINI_API_KEY"
    elif model_provider_choice == 2:
        api_key_name = "OPENAI_API_KEY"
    elif model_provider_choice == 3:
        api_key_name = "ANTHROPIC_API_KEY"

    if os.getenv(api_key_name):  # Check to see if environment variables are already in RAM
        return True

    read_env()  # Read the .env file to set environment variables

    # If environment variable is not in .env nor in RAM, prompt the user to enter the API key and save it to .env securely
    if not os.getenv(api_key_name):
        api_key = getpass.getpass(prompt=f"Enter your {api_key_name} (or leave blank to skip): ", stream=None, echo_char="*").strip()
        api_key = _strip_quotes(api_key)  # Allow the user to paste a key wrapped in quotes
        if api_key:
            os.environ[api_key_name] = api_key
            write_env_value(env_path, api_key_name, api_key)
            print(f"{api_key_name} has been set and saved to {env_path}.")
        else:
            print(f"Warning: {api_key_name} is not set. You will not be able to use the selected model provider.")