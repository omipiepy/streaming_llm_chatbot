import argparse

def parse_args():
    parser = argparse.ArgumentParser()

    parser.add_argument("--provider", default="ollama")
    parser.add_argument("--thinking", default="false")

    return parser.parse_args()