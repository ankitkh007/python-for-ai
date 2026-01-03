import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.environ.get("API_KEY")
database_url = os.environ.get("DATABASE_URL")
print(f"The API KEY is: {api_key}")
print(f"The Database URL is: {database_url}")
