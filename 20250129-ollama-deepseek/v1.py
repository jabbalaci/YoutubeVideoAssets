#!/usr/bin/env python3

from ollama import ChatResponse, chat


def main():
    response: ChatResponse = chat(
        model="deepseek-r1:1.5b",
        messages=[
            {
                "role": "user",
                "content": "Why is the sky blue?",
            },
        ],
    )
    print(response["message"]["content"])
    # or access fields directly from the response object
    # print(response.message.content)


if __name__ == "__main__":
    main()
