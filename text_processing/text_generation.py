import requests
import os

from dotenv import load_dotenv

load_dotenv()

DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY")
DEEPSEEK_BASE_URL = os.getenv("DEEPSEEK_BASE_URL")


def generate_text(prompt, word_limit=100, language="English"):
    payload = {
        "model": "deepseek-chat",
        "messages": [
            {
                "role": "system",
                "content": "You are a helpful assistant that generates text."
            },
            {
                "role": "user",
                "content": f"Write a {word_limit} word text in {language} based on this prompt: {prompt}"
            }
        ],
        "stream": False,
        "temperature": 1.3
    }

    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {DEEPSEEK_API_KEY}'
    }

    response = requests.post(f'{DEEPSEEK_BASE_URL}/chat/completions', headers=headers, json=payload)

    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        raise Exception(f"Error: {response.text}")


if __name__ == '__main__':
    query = input("Enter a prompt: ")
    generated_text = generate_text(query)
    print(generated_text)