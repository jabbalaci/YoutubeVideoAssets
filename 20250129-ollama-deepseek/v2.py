#!/usr/bin/env python3

from ollama import chat


def main():
    stream = chat(
        model="deepseek-r1:1.5b",
        messages=[{"role": "user", "content": "Why is the sky blue?"}],
        stream=True,
    )
    for chunk in stream:
        print(chunk["message"]["content"], end="", flush=True)


if __name__ == "__main__":
    main()
