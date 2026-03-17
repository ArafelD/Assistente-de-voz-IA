# Assistente de Voz com IA em Tempo Real

Projeto de assistente de voz utilizando streaming de áudio, Whisper, LLM e síntese de voz.

## Tecnologias

- Python
- FastAPI
- WebSockets
- Whisper
- OpenAI API
- gTTS

## Executar

pip install -r requirements.txt

export OPENAI_API_KEY="sua_chave"

uvicorn backend.main:app --reload

Acesse:
http://localhost:8000