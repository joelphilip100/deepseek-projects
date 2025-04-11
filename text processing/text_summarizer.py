import os

import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY")
DEEPSEEK_BASE_URL = os.getenv("DEEPSEEK_BASE_URL")


def summarize_text(text):
    payload = {
        "model": "deepseek-chat",
        "messages": [
            {
                "role": "system",
                "content": "You are a helpful assistant that summarizes text."
            },
            {
                "role": "user",
                "content": f"Summarize this text: {text} and add 3 interesting facts about it."
            }
        ],
        "stream": False
    }

    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {DEEPSEEK_API_KEY}'
    }

    response = requests.request("POST", f'{DEEPSEEK_BASE_URL}chat/completions', headers=headers, json=payload)

    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        raise Exception(f"Error: {response.text}")


if __name__ == "__main__":
    input_text = input("Enter text to summarize: ")
    print("Summary: " + summarize_text(input_text))
