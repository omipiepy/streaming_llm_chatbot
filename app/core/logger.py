import logging
import os

os.makedirs("logs", exist_ok=True)


def setup_logging():
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )

    info_handler = logging.FileHandler("logs/app.log")
    info_handler.setLevel(logging.INFO)
    info_handler.setFormatter(formatter)


    error_handler = logging.FileHandler("logs/error.log")
    error_handler.setLevel(logging.ERROR)
    error_handler.setFormatter(formatter)

    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(formatter)

    logging.basicConfig(
        level=logging.DEBUG,
        handlers=[
            info_handler,
            error_handler
        ]
    )


def get_logger(name: str) -> logging.Logger:
    return logging.getLogger(name)