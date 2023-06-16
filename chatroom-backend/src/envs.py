import os

from dotenv import load_dotenv

load_dotenv()

DATABASE_URL: str | None = os.getenv("DATABASE_URL")
SALT_KEY: str | None = os.getenv("SALT_KEY", "")
