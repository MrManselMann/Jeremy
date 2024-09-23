import speech_recognition as sr
import run_command

recognizer = sr.Recognizer()

# make sure wake word is all lowercase
WAKE_WORD = "jarvis"  

def strip_before_phrase(text, phrase):
    index = text.find(phrase)
    
    if index != -1:
        return text[index:]
    
    return text


def listen_for_commands():
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        print("Listening for wake word...")

        while True:
            audio = recognizer.listen(source)
            try:
                transcript = recognizer.recognize_google(audio)
                print(f"Detected: {transcript}")

                if WAKE_WORD in transcript.lower():
                    command = strip_before_phrase(transcript.lower(), "jarvis")
                    command = command.replace(WAKE_WORD, '').strip()  
                    print(f"Command received: {command}")
                    process_command(command)

            except sr.UnknownValueError:
                print("Could not understand audio")
            except sr.RequestError as e:
                print(f"Could not request results; {e}")

def process_command(command):
    print(f"Executing command: {command}")
    print("Processing")
    run_command.run_command(command)
