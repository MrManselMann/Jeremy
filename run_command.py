from gpt4all import GPT4All
import tts
import playsound
import webbrowser
from ytmusicapi import YTMusic

# AI setup
device_type = "gpu" # gpu or cpu
models = "small" # micro, small, medium, large
if models == "micro":
    model= GPT4All("qwen2-1_5b-instruct-q4_0.gguf", device=device_type) # 4gb ram
if models == "small":
    model = GPT4All("Phi-3-mini-4k-instruct.Q4_0.gguf", device=device_type)  # 4gb ram
elif models == "medium":
    model = GPT4All("Meta-Llama-3-8B-Instruct.Q4_0.gguf", device=device_type) # 8gb ram
elif models == "large":
    model = GPT4All("nous-hermes-llama2-13b.Q4_0.gguf", device=device_type) # 16gb ram

ai_prompt = "Please answer the following question in the shortest possible way without any additional context or elaboration: "

# YouTube Music setup
ytmusic = YTMusic("oauth.json")

# wolfram alpha setup


def run_command(command):
    playsound.playsound("audio/processing.mp3")
    
    if command.startswith("quit") or command.startswith("shutdown"):
        quit()

    if command.startswith("play"):
        query = command.replace("play", "").strip()
        if query:  # Ensure the query is not empty
            response = ytmusic.search(query)
            if response and isinstance(response, list) and 'videoId' in response[0]:
                top_result_video_id = response[0]['videoId']
                url = f"https://youtube.com/watch?v={top_result_video_id}"
                webbrowser.open(url)

            else:
                print("No results found for your query.")
        else:
            print("No query provided for play command.")
    elif command.startswith("calculate"):
        pass
    else:
        with model.chat_session():
            response_text = model.generate(ai_prompt + command, max_tokens=512)
            tts.tts(response_text)
    
    print("Done!\n")

# Example usage
# run_command("play some song")  # Uncomment to test
