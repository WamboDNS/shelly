```text
 ░▒▓███████▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓████████▓▒░▒▓█▓▒░      ░▒▓█▓▒░   ░▒▓█▓▒░░▒▓█▓▒░
░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░   ░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░   ░▒▓█▓▒░░▒▓█▓▒░ 
 ░▒▓██████▓▒░░▒▓████████▓▒░▒▓██████▓▒░ ░▒▓█▓▒░      ░▒▓█▓▒░    ░▒▓██████▓▒░  
       ░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░     
       ░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░     
░▒▓███████▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓████████▓▒░▒▓████████▓▒░▒▓████████▓▒░▒▓█▓▒░     
```

# Shelly – Natural Language to Bash

Shelly is a command-line tool that converts natural language input into safe, executable Bash or Zsh commands using OpenAI's language models.

It provides:
- A natural language interface to the shell
- Secure command generation with optional confirmation before execution
- Simple and clean interface to extend

## Installation

You can set up the project using either `pip` or `uv` (a faster, Rust-based package manager compatible with pip).

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/shelly.git
cd shelly
```

## Setup

**Option A:** Using uv
Install uv (if not already installed)
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```
Then set up your environment:
```bash
uv venv
source .venv/bin/activate
uv sync
```
**Option B**: Using pip
Create a virtual environment
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```
## Configuration
Create a .env file inside the src/ directory and add you OpenAI API key:
```bash
cp src/env src/.env
```

## Usage
```bash
uv run src/shelly.py
OR
python3 src/shelly.py # if you are using pip
```
## Example
```
> uv run src/main.py
Shelly – Natural Language to Bash

What do you want to do? (type 'exit' to quit)
> print all files in the directory above

Suggested command:

Command: ls ..

This command lists all the files and directories in the parent directory. The ".." represents the parent directory in Linux.

Do you want to execute this command? (y/n): y
fonts			leetcode-adventures	shelly			thesis-obsidian

----------------------------------------

What do you want to do? (type 'exit' to quit)
> exit
```

Be careful, this automated command execution is not working for every command yet. Mainly due to security reasons, I'm still looking for a way to make this work. An example is the '*' wildcard.
However, it is no problem to just copy the returned command and execute it manually! :)

If you want to contribute, have any suggestions or questions, feel free to open an issue, a PR or message me (e.g. on [x](https://x.com/wambosec)).
