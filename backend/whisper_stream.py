from faster_whisper import WhisperModel
import tempfile

model = WhisperModel("base", compute_type="int8")

def transcribe_stream(audio_chunks):
    with tempfile.NamedTemporaryFile(suffix=".wav") as f:
        for chunk in audio_chunks:
            f.write(chunk)

        segments, _ = model.transcribe(f.name)

        text = ""
        for segment in segments:
            text += segment.text

    return text