import asyncio
import edge_tts
import pygame
import os
import time
import uuid

def say(text):
    unique_id = str(uuid.uuid4())  # Generate a unique identifier
    OUTPUT_FILE = f"temp_audio_{unique_id}.mp3"

    async def save_text_to_speech():
        try:
            VOICE = 'en-US-SteffanNeural'
            communicate = edge_tts.Communicate(text, VOICE)
            await communicate.save(OUTPUT_FILE)
            print(f"Successfully saved to {OUTPUT_FILE} with text: {text}")
        except Exception as e:
            print(f"An error occurred while saving TTS: {e}")

    def play_mp3(file_path):
        if not os.path.exists(file_path):
            print(f"File {file_path} does not exist.")
            return
        try:
            pygame.mixer.quit()  # Ensure previous mixer state is cleaned up
            pygame.mixer.init()
            pygame.mixer.music.load(file_path)
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(10)
            pygame.mixer.quit()  # Clean up after playback
        except Exception as e:
            print(f"An error occurred during playback: {e}")

    async def process_audio():
        await save_text_to_speech()
        if os.path.exists(OUTPUT_FILE):
            print(f"Playing audio file: {OUTPUT_FILE}")
            play_mp3(OUTPUT_FILE)
            # Delay to ensure the file is no longer in use
            time.sleep(1)
            try:
                os.remove(OUTPUT_FILE)
                print(f"Removed audio file: {OUTPUT_FILE}")
            except Exception as e:
                print(f"An error occurred while removing the file: {e}")
        else:
            print(f"Failed to find {OUTPUT_FILE} after saving.")

    asyncio.run(process_audio())
