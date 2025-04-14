import subprocess
import shlex
from shell_agent import generate_shell_command

def confirm(prompt):
    response = input(f"{prompt} (y/n): ").strip().lower()
    return response == 'y'

def run_shell_command(command):
    try:
        subprocess.run(shlex.split(command), check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error while executing: {e}")

def main():
    print("🧠 Shelly – Natural Language to Bash\n")
    while True:
        user_input = input("💬 What do you want to do? (type 'exit' to quit)\n> ")
        if user_input.lower() in ['exit', 'quit']:
            break

        result = generate_shell_command(user_input)
        print("\n🤖 Suggested command:\n")
        print(result)

        lines = result.splitlines()
        command_line = next((line for line in lines if line.startswith("Command:")), None)
        if command_line:
            command = command_line.replace("Command:", "").strip()
            if confirm("\nDo you want to execute this command?"):
                run_shell_command(command)
        else:
            print("⚠️ No valid command found.")

        print("\n" + "-"*40 + "\n")

if __name__ == "__main__":
    main()