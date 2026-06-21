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
        print("\nSelect a Summary:")
        print("1. TL;DR Summary")
        print("2. Data Overview")
        print("3. Deep Dive Analysis")
        choice = input("Enter the number corresponding to your choice: ").strip()

        if choice == '1':
            return "tldr"
        elif choice == '2':
            return "overview"
        elif choice == '3':
            return "deepdive"
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


def get_prompt(prompt_type):
    """
    This function retrieves the appropriate prompt based on the user's selection.
    Returns: str: The selected prompt.
    """
    if prompt_type == "tldr":
        return get_tldr_prompt()
    elif prompt_type == "overview":
        return get_overview_prompt()
    elif prompt_type == "deepdive":
        return get_deepdive_prompt()


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


def get_overview_prompt():
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
    - {{Use plain text only — no Markdown. Bullets are to be noted with '-'. No Markdown headings.}}
    """

    # Concatenate to final prompt
    final_prompt = f"""{task_summary}
    {context_information}
    {model_instructions}
    {response_style}"""

    return final_prompt


def get_deepdive_prompt():
    task_summary = f"""
    ## Task Summary:
    {{Perform a detailed deep dive analysis of the attached CSV dataset. Go beyond surface-level description to examine distributions, patterns, relationships, and notable characteristics in the data.}}
    """

    context_information = f"""
    ## Context Information:
    - {{Standard CSV format with headers in the first row}}
    - {{Columns may include numbers, text, dates, or categorical values}}
    - {{Treat all dates as recorded historical values}}
    - {{The dataset may cover any domain — analyze based solely on what is present}}
    """

    model_instructions = f"""
    ## Model Instructions:
    - {{For numeric columns: report range (min-max), central tendency (mean/median if relevant), and distribution shape}}
    - {{For categorical/text columns: list top unique values with counts and note any dominant categories}}
    - {{Identify any clear relationships or correlations between columns that stand out}}
    - {{Highlight temporal patterns if dates are present, or geographic patterns if location data exists}}
    - {{Flag outliers, unusual spikes/drops, or data quality concerns}}
    - {{Base every observation strictly on the data provided — do not speculate beyond visible evidence}}
    - {{Suggest 2–3 specific follow-up questions or analyses the user could explore next}}
    """

    response_style = f"""
    ## Response style and format requirements:
    - {{Write as if explaining the data in detail to a data-savvy coworker}}
    - {{Use these four clear sections in order: Overview, Column Analysis, Key Patterns & Relationships, Takeaways & Next Steps}}
    - {{Use plain text only — no Markdown. Bullets are to be noted with '-'. No Markdown headings in the final output.}}
    - {{Keep the total response under 800 words}}
    - {{Be specific and quantitative where possible}}
    """

    final_prompt = f"""{task_summary}
    {context_information}
    {model_instructions}
    {response_style}"""

    return final_prompt