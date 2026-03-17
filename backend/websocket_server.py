from fastapi import APIRouter, WebSocket
from whisper_stream import transcribe_stream
from llm_client import ask_llm
from tts_engine import generate_voice

router = APIRouter()

@router.websocket("/ws/audio")
async def audio_stream(websocket: WebSocket):
    await websocket.accept()
    audio_buffer = []

    while True:
        data = await websocket.receive_bytes()
        audio_buffer.append(data)

        if len(audio_buffer) > 15:
            text = transcribe_stream(audio_buffer)
            response = ask_llm(text)
            voice_file = generate_voice(response)

            await websocket.send_json({
                "transcription": text,
                "response": response,
                "voice": voice_file
            })

            audio_buffer = []