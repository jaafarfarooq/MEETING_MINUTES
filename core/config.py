import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()

class Settings:
    SECRET_KEY = os.getenv("openapi_apikey")

settings = Settings()