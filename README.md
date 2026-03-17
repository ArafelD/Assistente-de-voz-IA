# 🎙️ Assistente de Voz com IA em Tempo Real

### Streaming de Áudio + Whisper + LLM + Síntese de Voz

Um assistente de voz inteligente com **streaming de áudio em tempo real**, capaz de ouvir, compreender e responder usuários utilizando **modelos de IA modernos**.

Este projeto demonstra a construção de um **pipeline completo de inteligência artificial para voz**, integrando:

* captura de áudio diretamente do navegador
* transmissão de áudio em tempo real via WebSocket
* reconhecimento de fala multilíngue com Whisper
* geração de respostas com um modelo de linguagem (LLM)
* conversão das respostas em áudio usando Text-to-Speech

O resultado é um **assistente conversacional totalmente funcional**, com comunicação por voz do início ao fim.

---

# ✨ Funcionalidades

### 🎤 Captura de áudio em tempo real

O áudio é capturado diretamente do microfone do usuário usando a **MediaRecorder API** do navegador.

### ⚡ Streaming de voz via WebSocket

Os dados de áudio são enviados continuamente para o backend através de **WebSockets**, permitindo processamento com baixa latência.

### 🧠 Reconhecimento de fala multilíngue

Utilizamos o **Whisper**, um dos modelos de reconhecimento de fala mais avançados, capaz de:

* compreender múltiplos idiomas
* lidar com diferentes sotaques
* transcrever fala com alta precisão

### 🤖 Processamento com IA (LLM)

A transcrição é enviada para um **modelo de linguagem**, que:

* interpreta a intenção do usuário
* gera respostas contextualizadas
* permite interação conversacional natural

### 🔊 Conversão de texto em voz

As respostas geradas são convertidas em áudio utilizando **Text-to-Speech**, criando um fluxo completo de comunicação por voz.

### 🧩 Arquitetura modular

O sistema foi projetado de forma modular, facilitando:

* escalabilidade
* manutenção
* substituição de modelos de IA

---

# 🏗️ Arquitetura do Sistema

```
Microfone do Usuário
        │
        ▼
Captura de Áudio no Navegador
(MediaRecorder API)
        │
        ▼
Streaming de Áudio
(WebSocket)
        │
        ▼
Backend Python (FastAPI)
        │
        ▼
Reconhecimento de Fala
(Whisper)
        │
        ▼
Processamento de Linguagem
(LLM)
        │
        ▼
Conversão Texto → Voz
(Text-to-Speech)
        │
        ▼
Resposta em Áudio para o Usuário
```

---

# 🧰 Tecnologias Utilizadas

## Backend

* **Python**
* **FastAPI**
* **WebSockets**
* **Whisper / Faster-Whisper**
* **OpenAI API**

## Frontend

* **JavaScript**
* **MediaRecorder API**
* **WebSocket Streaming**

## Inteligência Artificial

* Speech Recognition (Whisper)
* Large Language Models
* Text-to-Speech

---

# 📁 Estrutura do Projeto

```
voice-stream-assistant
│
├── backend
│   ├── main.py
│   ├── websocket_server.py
│   ├── whisper_stream.py
│   ├── llm_client.py
│   └── tts_engine.py
│
├── frontend
│   ├── index.html
│   ├── app.js
│   └── style.css
│
├── docker
│   └── Dockerfile
│
├── requirements.txt
└── README.md
```

---

# 🚀 Instalação

## 1️⃣ Clonar o repositório

```
git clone https://github.com/ESTEREPOSITORIO/voice-stream-assistant.git
```

## 2️⃣ Entrar no diretório do projeto

```
cd voice-stream-assistant
```

## 3️⃣ Instalar dependências

```
pip install -r requirements.txt
```

## 4️⃣ Configurar a chave da API

Linux / Mac

```
export OPENAI_API_KEY="sua_chave"
```

Windows

```
setx OPENAI_API_KEY "sua_chave"
```

## 5️⃣ Executar o servidor

```
uvicorn backend.main:app --reload
```

## 6️⃣ Abrir no navegador

```
http://localhost:8000
```

---

# 🧪 Exemplos de Aplicação

Este projeto pode ser utilizado como base para diversos sistemas baseados em voz:

* assistentes virtuais inteligentes
* sistemas de atendimento automatizado
* interfaces de voz para aplicações web
* ferramentas de acessibilidade
* automação residencial
* plataformas educacionais com IA

---

# 📈 Melhorias Futuras

Algumas evoluções possíveis para o projeto:

* transcrição parcial em tempo real
* memória conversacional
* suporte a múltiplos usuários
* integração com modelos locais (LLM offline)
* streaming com WebRTC
* identificação de locutor
* análise de emoções na fala

---





# 📜 Licença

Este projeto está sob a licença **MIT**.
