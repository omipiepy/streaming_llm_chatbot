# Streaming LLM Chatbot

A modular and extensible chatbot system that supports multiple large language model providers such as Ollama and Google Gemini. The system is designed with a clean architecture that separates concerns between service, provider, and utility layers.

---

## Overview

This project provides a unified interface for interacting with different LLM providers. It includes retry handling, timeout control, and a CLI-based interaction system.

The architecture is designed to be easily extensible for adding new providers without modifying the core service logic.

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


llm_chatbot/
│
├── app/
│ ├── core/
│ ├── providers/
│ ├── schemas/
│ ├── services/
│ ├── utils/
│ ├── main.py
│
├── tests/
├── logs/
├── pyproject.toml
└── README.md

---

## Installation


git clone https://github.com/omipiepy/streaming_llm_chatbot.git
cd streaming_llm_chatbot

python -m venv .venv
.venv\Scripts\activate   # Windows
source .venv/bin/activate  # Linux/Mac

pip install -r requirements.txt

uv sync
Usage
python -m app.main --provider ollama
python -m app.main --provider gemini
CLI Interaction
You: hello
AI: Hello. How can I assist you today?

Type exit to quit.

## Architecture

User Input
→ ChatService
→ Provider Factory
→ Selected LLM Provider

Adding a New Provider
Create provider in app/providers/
Implement:
async def generate(self, prompt: ChatRequest) -> str
Register in factory:
providers = {
    "ollama": OllamaProvider,
    "gemini": GeminiProvider
}
## Logging

Logs are stored in logs/:

app.log
error.log

Logs are excluded via .gitignore.

Testing
pytest
Notes
Configure API keys in environment or config file
Adjust retry and timeout in ChatService