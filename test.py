from pathlib import Path
from dotenv import load_dotenv
import os

env_path = Path(__file__).parent / ".env"
print("looking at:", env_path)
print("exists:", env_path.exists())
print("contents:", env_path.read_text())  # see what's actually in it

load_dotenv(env_path)
print("MY_VAR:", os.getenv("MY_VAR"))