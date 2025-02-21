import subprocess
import difflib
import shlex
import openai

# Set your OpenAI API key (either in the code or via environment variable)
openai.api_key = 'your-api-key-here'

def get_installed_commands():
    """Returns a list of available shell commands."""
    try:
        result = subprocess.run("compgen -c", shell=True, text=True, capture_output=True, executable='/bin/bash')
        return result.stdout.split() if result.stdout else []
    except Exception:
        return []

def correct_command(user_command, available_commands):
    """Use OpenAI's API to get smart suggestions for the user's command."""
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Updated to a supported model
            messages=[
                {"role": "system", "content": "You are a helpful terminal assistant."},
                {"role": "user", "content": f"Suggest the correct version of this command: '{user_command}'"}
            ]
        )
        return response['choices'][0]['message']['content'].strip()
    except Exception as e:
        print(f"Error with OpenAI API: {e}")
        # Fallback to fuzzy matching in case of failure
        words = shlex.split(user_command)
        corrected_words = []
        for word in words:
            matches = difflib.get_close_matches(word, available_commands, n=1, cutoff=0.7)
            corrected_words.append(matches[0] if matches else word)
        return " ".join(corrected_words)

def execute_command(command):
    """Executes the given shell command and prints output."""
    try:
        result = subprocess.run(command, shell=True, text=True, capture_output=True, executable='/bin/bash')
        output = result.stdout.strip() if result.stdout else result.stderr.strip()
        print(output if output else "(No output)")
    except Exception as e:
        print(f"Error executing command: {e}")

def main():
    print("\n💻 AI-Powered Terminal Assistant Ready! Type 'exit' to quit.\n")
    available_commands = get_installed_commands()
    
    while True:
        user_command = input("💻 Enter Command (or say 'exit' to quit): ").strip()
        
        if user_command.lower() == "exit":
            print("👋 Exiting Terminal Assistant. Goodbye!")
            break
        
        corrected = correct_command(user_command, available_commands)
        
        if corrected != user_command:
            choice = input(f"💡 Did you mean: '{corrected}'? (yes/no): ").strip().lower()
            if choice == 'yes':
                execute_command(corrected)
            else:
                print("⚠️ Command not executed.")
        else:
            execute_command(user_command)

if __name__ == "__main__":
    main()
