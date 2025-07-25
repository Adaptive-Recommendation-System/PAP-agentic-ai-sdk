import os
from dotenv import load_dotenv

# Load variables from .env file at project root
load_dotenv()
MODEL_NAME = os.getenv("MODEL_NAME", "llama3")


