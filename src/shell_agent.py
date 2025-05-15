import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_shell_command(natural_language_input):
    system_prompt = (
        "You are an experienced Linux shell expert. "
        "Translate user requests into safe Bash/zsh compatible commands. "
        "Before the command, ALWAYS write 'Command: ' and only put the command afterwards."
        "Everything else should come in the next lines."
        "Do not use quotations around the command."
        "Always explain your suggestions briefly. Avoid destructive commands like 'rm' unless absolutely necessary and with clear warnings."
    )

    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": f"Request: {natural_language_input}"}
    ]

    response = openai.chat.completions.create(
        model="gpt-4",
        messages=messages,
        temperature=0.2
    )

    return response.choices[0].message.content
