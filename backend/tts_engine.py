from gtts import gTTS
import uuid

def generate_voice(text):
    filename = f"audio_{uuid.uuid4()}.mp3"
    tts = gTTS(text=text, lang="pt")
    tts.save(filename)
    return filename