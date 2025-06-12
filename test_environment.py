from dotenv import load_dotenv
import os

load_dotenv()  # Loads from .env by default

token = os.getenv("CAPSTONE_TEST")
print(token)
