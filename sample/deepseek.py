import requests

OLLAMA_URL = "http://localhost:11434/api/generate"


def query_deepseek(query):
    payload = {
        "model": "deepseek-r1:7b",
        "prompt": query,
        "stream": False
    }

    response = requests.post(OLLAMA_URL, json=payload)

    if response.status_code == 200:
        return response.json().get("response", "No response")
    else:
        raise Exception(f"Error: {response.status_code}")


query_deepseek("Write a program in python to add two numbers")