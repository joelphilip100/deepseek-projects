import os
import json

from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY")
DEEPSEEK_BASE_URL = os.getenv("DEEPSEEK_BASE_URL")

client = OpenAI(api_key=DEEPSEEK_API_KEY, base_url=DEEPSEEK_BASE_URL)


def extract_json(response):
    try:
        data = json.loads(response)
        return data
    except json.JSONDecodeError as e:
        raise ValueError("Failed to decode JSON.") from e


def extract_named_entities(text, entities, api=False):
    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {
                "role": "system",
                "content": "You are a helpful assistant that extracts named entities from text."
            },
            {
                "role": "user",
                "content": f"Extract all named entities ({entities}) from the text {text}. It should return a plain text response without any Markdown or formatting." if not api else
                           f"""
                                Extract all named entities ({entities}) from the text {text}.
                                Return a valid plain JSON object where each key is an entity type, and the value is a string or list of strings (entities of that type).
                                Format is as follows:
                                {{
                                    "name": ["entity1", "entity2", "entity3"],
                                    "place": "place1"
                                }}
                                ⚠️ Do NOT use triple backticks (```), the word "json", or any code block syntax. Just return the raw JSON object as plain text.
                           """
            }
        ],
        stream=False
    )

    if not api:
        return response.choices[0].message.content

    return extract_json(response.choices[0].message.content)


if __name__ == "__main__":
    input_text = input("Enter text to extract named entities: ")
    named_entities = input("Enter named entities to extract: ")
    print("Named Entities: \n" + extract_named_entities(input_text, named_entities))
