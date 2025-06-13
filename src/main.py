import subprocess
import re
from openai import OpenAI
import os
from dotenv import load_dotenv
import json

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

def parse_command(text):
    """Extract command from text that contains <command>...</command> tags."""
    match = re.search(r'<command>(.*?)</command>', text, re.DOTALL)
    if match:
        return match.group(1).strip()
    return None

def confirm(prompt):
    response = input(f"{prompt} (y/n): ").strip().lower()
    return response == 'y' or response.lower() == 'yes'

def run_shell_command(command):
    try:
        # Use bash -c to handle wildcards and other shell features
        subprocess.run(['bash', '-c', command], check=False)
    except subprocess.CalledProcessError as e:
        print(f"Error while executing shell command: {e}")

def main():
    print("Shelly – Natural Language to Bash\n")

    base_URL = "https://api.openai.com/v1"
    client = OpenAI(api_key=OPENAI_API_KEY, base_url=base_URL)
    
    system_prompt = """You are an experienced Linux shell expert. 
        Translate user requests into safe Bash/zsh compatible commands. 
        Always give the command in the following format: <command> ENTER COMMAND HERE </command> 
        Everything else should come in the next lines. 
        Do not use quotations around the command. Always explain your suggestions briefly. 
        Avoid destructive commands like 'rm' unless absolutely necessary and give clear warnings."""

    messages = [
        {"role": "system", "content": system_prompt},
    ]
    
    while True:
        user_input = input("What do you want to do? (type 'exit' to quit)\n> ")
        if user_input.lower() in ['exit', 'quit']:
            break
        messages.append({"role": "user", "content": json.dumps(user_input, indent=2)})
        try: 
            response = client.chat.completions.create(
                model="gpt-4.1",
                messages=messages,
            )

            result = response.choices[0].message.content
            command = parse_command(result)
            print(result)
            print(command)

            command = parse_command(result)
            if command:
                if confirm("\nDo you want to execute this command?"):
                    run_shell_command(command)
            else:
                print("No valid command found.")

            print("\n" + "-"*40 + "\n")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()