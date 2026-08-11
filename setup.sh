#!/usr/bin/env bash
# Environment Variable Setup Script
# setup.sh
# This script automates setup for the summarizer app
# SPDX-License-Identifier: MIT

set -euo pipefail

read -rsp "Please enter your Gemini API Key: (press enter to leave empty):\n" GEMINI_API_KEY
read -rsp "Please enter your OpenAI API Key: (press enter to leave empty):\n" OPENAI_API_KEY
read -rsp "Please enter your Anthropic API Key: (press enter to leave empty):\n" ANTHROPIC_API_KEY
read -rp "Do you want to use Gemini Free Tier? (y/n): " gemini_free_flag

if [ "$gemini_free_flag" == "y" ] || [ "$gemini_free_flag" == "Y" ]; then
  GEMINI_FREE_TIER=True
else
  GEMINI_FREE_TIER=False
fi

touch "./.env"
cat > "./.env" << EOF
GEMINI_API_KEY=${GEMINI_API_KEY}
OPENAI_API_KEY=${OPENAI_API_KEY}
ANTHROPIC_API_KEY=${ANTHROPIC_API_KEY}
GEMINI_FREE_TIER=${GEMINI_FREE_TIER}
EOF
