# Streaming LLM Chatbot

A chatbot system that supports multiple large language model providers such as Ollama and Google Gemini. The system is designed with a clean architecture that separates concerns between service, provider, schemas and utility layers. This project is focused on handling asynchronous request for streaming LLM.

---

## Overview

This project provide unified interface for providers: ollama and gemini

We can choose one of the provider which is passed through arguments.

We have also implemented logging system where info of each steps are stored in *.log files .

We have also encoutered failure so there is a system for retrying 3 times if there is failure.

We have also implemented timeout of 30s.

---

## Features

- Support for multiple LLM providers (Ollama, Gemini)
- Factory-based provider selection
- Asynchronous request handling
- Retry mechanism for failed requests
- Timeout control for long-running requests
- CLI-based chat interface
- Structured logging with file output
- Modular and extensible architecture

---

## Project Structure

```
llm_chatbot/
├── app/
│   ├── core/
│   │   ├── config.py
│   │   └── logger.py
│   ├── main.py
│   ├── providers/
│   │   ├── base.py
│   │   ├── factory.py
│   │   ├── gemini.py
│   │   └── ollama.py
│   ├── schemas/
│   │   ├── request.py
│   │   └── response.py
│   ├── services/
│   │   └── chat_services.py
│   └── utils/
│       ├── retry.py
│       └── timer.py
├── main.py
├── pyproject.toml
├── README.md
├── tests/
│   ├── request_test.py
│   ├── stream_test.py
│   └── validation_test.py
└── uv.lock
```
---

## Installation

```
git clone https://github.com/omipiepy/llm_chatbot.git
cd llm_chatbot
```
```
uv init
uv .venv
.venv\Scripts\activate   # Windows
source .venv/bin/activate  # Linux/Mac
```
```
uv sync
```
---
### Setting up environment
- Make .env file and insert these things
```
LLAMA_API_URL = "http://localhost:11434"
GEMINI_API_URL = "https://generativelanguage.googleapis.com/v1beta/models"
GEMINI_API_KEY = "your_api_key"
GEMINI_MODEL_NAME = "gemini-2.5-flash"
OLLAMA_MODEL_NAME = "deepseek-r1:1.5b"
default_provider = "ollama"
```

### Running this application
you can pass an argument and in default it will be ollama for provider and false in thinking
```
python -m app.main --provider=ollama --thinking=true
python -m app.main --provider gemini --thinking=false
```
### CLI Interaction
```
You: hello
AI: Hello. How can I assist you today?

Type exit to quit.
```

## Architecture

### User Input
- ChatService
- Provider 
- Thinking or not

### Logging

- Logs are stored in logs/:
```
app.log
error.log
```

- Logs are excluded via .gitignore.

### Testing
Testing for validation and streaming
```
pytest -q
```

## Notes
- Configure API keys in environment or config file
- Adjust retry and timeout in ChatService
