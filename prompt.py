# Main Prompt File
# File contains different prompts which can be used to help the user understand the file 
# SPDX-License-Identifier: MIT

# Define Prompt Choosing Functions
def get_prompt_type():
    """
    This function allows the user to select a prompt from a list of available prompts. 
    It returns the selected prompt as a string.
    Returns: str: The selected prompt.
    """
    while True:
        print("\nSelect a prompt:")
        print("1. TL;DR Summary Prompt")
        print("2. Data Audit Prompt")
        choice = input("Enter the number corresponding to your choice: ").strip()

        if choice == '1':
            return "tldr"
        elif choice == '2':
            return "audit"
        else:
            print("Invalid choice. Please enter 1 or 2.")

def get_prompt(prompt_type):
    """
    This function retrieves the appropriate prompt based on the user's selection.
    Returns: str: The selected prompt.
    """
    if prompt_type == "tldr":
        return get_tldr_prompt()
    elif prompt_type == "audit":
        return get_audit_prompt()
  



# Define Prompts that can be used

def get_tldr_prompt():
    task_summary = f"""
    ## Task Summary:
    {{Produce a 'Too Long; Didn’t Read' (TL;DR) summary of the attached dataset. The TL;DR sentence should describe, in one high-level line, what the dataset is and what it covers. Then provide 2–3 bullets highlighting the most notable patterns, trends, or anomalies visible in the data. Use numeric ranges when helpful, but keep the focus on the biggest takeaways.}}
    """

    response_style = f"""
    ## Response style and format requirements:
    - {{Write in a sharp, punchy, and bottom-line-up-front (BLUF) style}}
    - {{Format: Start with a single 'TL;DR:' sentence, followed by a short bulleted list}}
    - {{Bullets must follow these rules:
        - Start with a short, strong label (e.g., 'Trend shift:', 'Category contrast:', 'Peak anomaly:')
        - Contain exactly one idea per bullet
        - Use numeric anchors when possible
        - Avoid hedging, filler, or multi-clause sentences
        - Read like headlines, not explanations}}
    - {{Strictly limit the response to 100 words or less}}
    - {{Use plain text only — no Markdown. Bullets are to be noted with '-'}}
    """

    final_prompt = f"""{task_summary}
    {response_style}"""
    
    return final_prompt


def get_audit_prompt():
    # Prompt for the Summarizer:
    # Use this to clearly define the task and job needed by the model
    task_summary = f"""
    ## Task Summary:
    {{Review the attached CSV and summarize what the data covers, including anything notable or unusual.}}
    """

    # Use this to provide contextual information related to the task
    context_information = f"""
    ## Context Information:
    - {{Standard CSV format with headers in the first row}}
    - {{Columns may include numbers, text, or dates}}
    - {{Treat all dates in the data file as a recorded value and not predictions}}
    - {{The dataset may cover any domain — do not assume a specific subject area}}
    """

    # Use this to provide any model instructions that you want model to adhere to
    model_instructions = f"""
    ## Model Instructions:
    - {{Explain what each column represents and flag anything out of the ordinary}}
    - {{Base all observations only on the data provided}}
    - {{Only use historical context or external knowledge where it clearly and directly explains a specific data pattern — do not force connections}}
    - {{If no external context is relevant, rely entirely on what the data shows}}
    """

    # Use this to provide response style and formatting guidance
    response_style = f"""
    ## Response style and format requirements:
    - {{Write as if explaining the data to a coworker}}
    - {{Use three sections: overview, column breakdown, and key takeaways}}
    - {{Limit the response to 500 words or less}}
    - {{Use plain text only — no Markdown. Bullets are to be noted with '-'. No headings.}}
    """

    # Concatenate to final prompt
    final_prompt = f"""{task_summary}
    {context_information}
    {model_instructions}
    {response_style}"""

    return final_prompt