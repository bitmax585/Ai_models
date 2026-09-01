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

    
    try:
        response = requests.post(
            url,
            headers=headers,
            json=data,
            timeout=60,
        )

        response.raise_for_status()

        response_data = response.json()

        assistant_message = response_data["choices"][0]["message"]["content"]



    except requests.exceptions.Timeout:
        messages.pop()
        return "Error: Request timed out."

    except requests.exceptions.ConnectionError:
        messages.pop()
        return "Error: Could not connect to the API"

    except requests.exceptions.HTTPError:
        messages.pop()
        return f"Error: API returned status code {response.status_code}."
    
    except requests.exceptions.RequestException:
        messages.pop()
        return "Error: Request failed."

    except (ValueError, KeyError, IndexError):
        messages.pop()
        return "Error: Invalid response from API."


    messages.append(
        {
            "role": "assistant",
            "content": assistant_message
        }
    )

    return assistant_message



