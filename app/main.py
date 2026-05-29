import asyncio
import os
import sys

from app.schemas.request import ChatRequest
from app.services.chat_services import ChatService
from app.core.logger import setup_logging, get_logger
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("--provider", default="ollama")
parser.add_argument("--thinking", default="false")
parser.add_argument("--timeout" , default="30")
args = parser.parse_args()

setup_logging()

logger = get_logger(__name__)
logger.info("Application started")

def center(text: str, width: int = 80):
    return text.center(width)


def print_ui_header():
    print("\n" * 2)
    print(center("WELCOME TO AI CHAT ASSISTANT"))
    print(center("Type 'exit' to quit"))
    print("\n" * 2)


async def main():
    service = ChatService()

    print_ui_header()

    while True:
        try:
            user_input = input("\nYou : ").strip()
        except (KeyboardInterrupt, EOFError):
            logger.error("User interrupted the application")
            print("\nGoodbye !!!!!!")
            sys.exit(0)

        if not user_input:
            continue

        if user_input.lower() == "exit":
            print("\nGoodbye !!!!!!!")
            break

        if args.thinking.lower()=="true":
            print("\nThinking...\n")
        print("AI: ", end="", flush=True)

        response = await service.chat(ChatRequest(prompt=user_input, provider=args.provider, thinking=args.thinking, timeout=args.timeout))

        if args.thinking.lower()=="false":
            print(f"{response}")

if __name__ == "__main__":
    asyncio.run(main())