# AI-Powered Terminal Assistant

## Overview

AI-Powered Terminal Assistant is a Python-based terminal assistant that helps users with smart shell command suggestions, auto-corrections, and command execution. It integrates **OpenAI GPT-4** for intelligent suggestions and corrections. In case the API is unavailable, the assistant also provides fallback fuzzy matching using Python's built-in libraries. The project is designed to run directly in your terminal, offering an efficient and interactive way to execute shell commands.

## Tech Stack

- **Python 3.x**: Core programming language used for backend logic.
- **OpenAI GPT-4**: For intelligent command suggestions and corrections.
- **subprocess module**: For executing shell commands.
- **difflib module**: For fuzzy matching of commands.
- **shlex module**: For safely splitting user input into shell commands.
- **Regex**: For pattern-based command corrections (e.g., fixing common flag mistakes).

## Project Structure
/ai-terminal-assistant ├── ai_terminal_assistant.py # Main Python file with terminal logic ├── requirements.txt # File containing project dependencies ├── .gitignore # Git ignore file ├── README.md # Project documentation └── /venv (optional, for virtual environment)

markdown
Copy
Edit

## Prerequisites

Ensure you have the following installed:

- **Python 3.x**: To run the project. Download [Python here](https://www.python.org/downloads/).
- **pip**: Python package manager for installing dependencies.
- **Git**: To clone the repository.
- **OpenAI API Key**: Required to make command suggestions using OpenAI's GPT-4 model.

## Setup & Installation

### Clone the Repository

Clone the repository using Git:

git clone https://github.com/Khushi-dubey-dot/ai-terminal-assistant.git cd ai-terminal-assistant

cpp
Copy
Edit

### Install Dependencies

Create and activate a virtual environment (optional but recommended):

python -m venv venv

markdown
Copy
Edit

Activate the virtual environment:
- On **Windows**:

.\venv\Scripts\activate

markdown
Copy
Edit

- On **macOS/Linux**:

source venv/bin/activate

swift
Copy
Edit

Install the required dependencies:

pip install -r requirements.txt

vbnet
Copy
Edit

### Set Up OpenAI API Key

Sign up at OpenAI and get your API key. Add the key in the `ai_terminal_assistant.py` file:

```python
openai.api_key = 'your-api-key-here'
Alternatively, you can set the API key as an environment variable for better security:

On macOS/Linux:
bash
Copy
Edit
export OPENAI_API_KEY='your-api-key-here'
On Windows:
bash
Copy
Edit
set OPENAI_API_KEY='your-api-key-here'
Running the Application
Start the AI Terminal Assistant
To run the assistant, execute the following command:

nginx
Copy
Edit
python ai_terminal_assistant.py
Interaction with the Assistant
You will see the following prompt in the terminal:

pgsql
Copy
Edit
💻 AI-Powered Terminal Assistant Ready! Type 'exit' to quit.
Enter a shell command or a mistyped command, and the assistant will suggest the correct command and execute it. Type exit to quit the assistant.

License
This project is licensed under the MIT License. See the LICENSE file for details.




