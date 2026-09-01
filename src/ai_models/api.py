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

def send_prompt(content, messages):

    messages.append(
        {
            "role": "user",
            "content": content,
        }
    )


    data = {
        "model" : "qwen3.8-max",
        "messages": messages,
    }


    response = requests.post(
        url,
        headers=headers,
        json=data,
    )

    response.raise_for_status()

    response_data = response.json()

    assistant_message = response_data["choices"][0]["message"]["content"]

    messages.append(
        {
            "role": "assistant",
            "content": assistant_message
        }
    )

    return assistant_message



