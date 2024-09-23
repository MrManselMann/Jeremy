import re
import elevenlabs
from elevenlabs import ElevenLabs, stream

client = ElevenLabs(api_key="sk_16db5422f4a66a5bbb283238ce61648909afa32533258dac")

def list_voices():
    print(client.voices.get_all())
def list_models():
    print(client.models.get_all())

def clean_text_for_tts(input_text):
    emoji_pattern = re.compile(
        "["
        "\U0001F600-\U0001F64F"  # emoticons
        "\U0001F300-\U0001F5FF"  # symbols & pictographs
        "\U0001F680-\U0001F6FF"  # transport & map symbols
        "\U0001F700-\U0001F77F"  # alchemical symbols
        "\U0001F780-\U0001F7FF"  # Geometric Shapes Extended
        "\U0001F800-\U0001F8FF"  # Supplemental Arrows-C
        "\U0001F900-\U0001F9FF"  # Supplemental Symbols and Pictographs
        "\U0001FA00-\U0001FA6F"  # Chess Symbols
        "\U00002700-\U000027BF"  # Dingbats
        "]+",
        flags=re.UNICODE
    )
    
    # Remove emojis and normalize spaces
    cleaned_text = emoji_pattern.sub('', input_text)
    return re.sub(r'\s+', ' ', cleaned_text).strip()

def is_all_english(input_string):
    return input_string.isalpha()

def tts(text):
    cleaned_text = clean_text_for_tts(text)
    model = "eleven_turbo_v2" if is_all_english(cleaned_text) else "eleven_multilingual_v2"
    audio = client.generate(
        text=cleaned_text,
        voice="Alexander Kensington - Studio Quality",
        model=model,
        stream=True
    )
    stream(audio)
