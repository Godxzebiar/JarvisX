from dotenv import load_dotenv
load_dotenv()

import os

OWNER_NAME = "Rishav"
JARVIS_NAME = "Jarvis X"

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

MODEL = "openai/gpt-oss-20b:free"

GREETING = f"Welcome Boss {OWNER_NAME}!"
VERSION = "JarvisX v1.1"

