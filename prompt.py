# Main Prompt File
# SPDX-License-Identifier: MIT

def get_prompt():
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