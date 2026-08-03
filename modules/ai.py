import requests
from config.settings import OPENROUTER_API_KEY, MODEL

URL = "https://openrouter.ai/api/v1/chat/completions"

SYSTEM_PROMPT = """
You are Jarvis X, a smart AI assistant.
Always reply in simple Hindi/Hinglish.
Always call the user 'Boss'.
Keep replies helpful and natural.
"""

def ask_ai(question):
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json",
        "HTTP-Referer": "https://jarvisx.app",
        "X-Title": "JarvisX v1.1"
    }

    payload = {
        "model": MODEL,
        "messages": [
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            },
            {
                "role": "user",
                "content": question
            }
        ]
    }

    try:
        response = requests.post(
            URL,
            headers=headers,
            json=payload,
            timeout=60
        )

        response.raise_for_status()
        data = response.json()

        return data["choices"][0]["message"]["content"]

    except Exception as e:
        return f"Error: {e}"

