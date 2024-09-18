import datetime
import os
from stt import get_text
from tts import say
from chat import response
from mucis import plays_song
# Define constants
EXIT_PHRASES = ["bye", "goodbye", "that's all", "thats is all"]
CHAT_LOG_PATH = "chatlog.txt"
CONTEXT_FILE_PATH = "context.txt"

def clear_file(file_path):
    """Clear the contents of a file."""
    with open(file_path, 'w') as file:
        pass

def log_conversation(text, answer):
    """Log conversation to a file with a timestamp."""
    with open(CHAT_LOG_PATH, "a") as chatlog:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        chatlog.write(f"{timestamp}\n")
        chatlog.write(f"    you:\n{text}\n")
        chatlog.write(f"    chat:\n{answer}\n")

def update_context(text, answer):
    """Update the context file with the latest conversation."""
    with open(CONTEXT_FILE_PATH, "a") as context_file:
        context_file.write(f"user:\n{text}\n")
        context_file.write(f"chatbot:\n{answer}\n")

# Initialize context file
clear_file(CONTEXT_FILE_PATH)
with open(CONTEXT_FILE_PATH, "a") as context_file:
    context_file.write("If there is nothing here, that means it's the beginning of the conversation.")

# Conversation loop
while True:
    try:
        print("Listening for input...")
        text = get_text()
        print("                                                               ")  # Clear line
        if not text:
            print("No text received. Retrying...")
            continue

        with open(CONTEXT_FILE_PATH, "r") as context_file:
            context = context_file.read()
            
        answer = response(text, context)
        log_conversation(text, answer)
        if "#" == answer[0] and "#" == answer[1] and "!" == answer[2] and "##!@#$%^&*()##" in answer:
            answer = answer.lstrip('##!@#$%^&*()##')
            if ', ' in answer:
                title, artist = answer.split(', ', 1)
                plays_song(title, artist)
        update_context(text, answer)
        say(answer)

        log_conversation(text, answer)

        if text.lower() in EXIT_PHRASES:
            break

    except Exception as e:
        print(f"An error occurred: {e}")
