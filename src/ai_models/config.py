import os 

from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("NOVAI_API_KEY")

API_URL  = "https://aiapi-pro.com/v1/chat/completions"

MODEL = "qwen3.8-max"

