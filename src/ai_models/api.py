import requests
import json
import time
from ai_models.config import API_KEY, API_URL, MODEL

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
        "model" : MODEL,
        "messages": messages,
        "stream": True,
    }

    
    try:
        response = requests.post(
            API_URL,
            headers=headers,
            json=data,
            timeout=60,
            stream=True,
        )

        response.raise_for_status()

        assistant_message = ""

        for line in response.iter_lines():

            if not line:
                continue

            line = line.decode("utf-8")

            if line.startswith("data: "):
                line = line[6:]

            if line == "[DONE]":
                break

            chunk = json.loads(line)

            if not chunk.get("choices"):
                continue

            delta = chunk["choices"][0]["delta"]

            text = delta.get("content")

            if text:
                print(f"\033[96m{text}\033[0m", end="", flush=True)
                time.sleep(0.2)
                assistant_message += text
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



