from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from websocket_server import router

app = FastAPI(title="Voice Streaming AI Assistant")

app.include_router(router)

app.mount("/", StaticFiles(directory="../frontend", html=True))