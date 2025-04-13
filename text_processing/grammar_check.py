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
        corrected_text = data.get("corrected_text", "")
        suggestions = data.get("suggestions", [])
        return corrected_text, suggestions
    except json.JSONDecodeError as e:
        raise ValueError("Failed to decode JSON.") from e


def check_grammar(prompt, api=False):
    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {
                "role": "system",
                "content": "You are a helpful assistant that checks and corrects the spelling and grammar of text and suggests improvements. Return your response in plain text only, without any Markdown or formatting."},
            {
                "role": "user",
                "content": f"Check the grammar of this text: {prompt} and point out the mistakes made in bullet points." if not api
                else f"""
                        Check the grammar of this text: {prompt}
                        Return the result as a valid JSON object with the following structure (no Markdown, no explanation, no extra formatting):
                        {{
                            "corrected_text": "The fully corrected version of the input text.",
                            "suggestions": [
                                "A list of individual grammar corrections or improvements, each as a string."
                            ]
                        }}

                        Only return the JSON object, without any additional text or formatting.
                     """
            }
        ],
        stream=False
    )

    if not api:
        return response.choices[0].message.content

    corrected_text, suggestions = extract_json(response.choices[0].message.content)
    return corrected_text, suggestions


if __name__ == "__main__":
    input_text = input("Enter text to check grammar: ")
    print("Corrected Text: " + check_grammar(input_text))
