import os
import requests

from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("NOVAI_API_KEY")

url = "https://aiapi-pro.com/v1/chat/completions"

headers = {
    "Authorization" : f"Bearer {API_KEY}",
    "Content-Type" : "application/json"
}

def send_prompt(content):
    data = {
        "model" : "qwen3.8-max",
        "messages" : [
            {
                "role" : "user",
                "content" : content,
            },
        ],
    }

    response = requests.post(
        url,
        headers=headers,
        json=data,
    )

    return response.json()["choices"][0]["message"]["content"]

