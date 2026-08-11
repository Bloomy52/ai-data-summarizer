# Environment Variable Setup Script
# setup.ps1
# This script automates setup for the summarizer app for Windows.
# SPDX-License-Identifier: MIT

$GEMINI_API_KEY = Read-Host -Prompt "Enter your Gemini API Key" -AsSecureString
$OPENAI_API_KEY = Read-Host -Prompt "Enter your OpenAI API Key" -AsSecureString
$ANTHROPIC_API_KEY = Read-Host -Prompt "Enter your Anthropic API Key" -AsSecureString
$GEMINI_FREE_TIER = Read-Host -Prompt "Do you want to use Gemini Free Tier? (y/n)"

if ($GEMINI_FREE_TIER -eq "y" -or $GEMINI_FREE_TIER -eq "Y") {
    $GEMINI_FREE_TIER = True
} else {
    $GEMINI_FREE_TIER = False
}

# add the environment variables to .env
$envContent = @"
GEMINI_API_KEY=$GEMINI_API_KEY
OPENAI_API_KEY=$OPENAI_API_KEY
ANTHROPIC_API_KEY=$ANTHROPIC_API_KEY
GEMINI_FREE_TIER=$GEMINI_FREE_TIER
"@

Set-Content -Path ".env" -Value $envContent