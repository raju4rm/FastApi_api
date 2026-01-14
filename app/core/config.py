import os
from dotenv import load_dotenv

load_dotenv()  # loads .env into environment
print("os.getenv(SECRET_KEY):", os.getenv("SECRET_KEY"))
# raise SystemExit

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM", "HS256")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 60))
