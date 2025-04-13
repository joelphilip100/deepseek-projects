import os

from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY")
DEEPSEEK_BASE_URL = os.getenv("DEEPSEEK_BASE_URL")

client = OpenAI(api_key=DEEPSEEK_API_KEY, base_url=DEEPSEEK_BASE_URL)


def analyze_sentiment(text):
    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {
                "role": "system",
                "content": "You are a helpful assistant that analyzes sentiment."
            },
            {
                "role": "user",
                "content": f"Analyze the sentiment of the following text: {text} and classify them as 'positive', 'negative', or 'neutral' and return the result as a plain text response without any Markdown or formatting."
            }
        ]
    )
    return response.choices[0].message.content


if __name__ == "__main__":
    input_text = input("Enter text to analyze sentiment: ")
    print("Sentiment: " + analyze_sentiment(input_text))