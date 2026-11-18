import os
from dotenv import load_dotenv

load_dotenv()  # читаем секреты из внешнего файла .env

DJANGO_SECRET_KEY = os.getenv("DJANGO_SECRET_KEY")
DB_PASSWORD = os.getenv("DB_PASSWORD")
API_KEY = os.getenv("API_KEY")

def masked(v):
    return (v[:3] + "***") if v else "<MISSING>"

print("Secrets loaded from environment (.env / env vars):")
print("  DJANGO_SECRET_KEY:", masked(DJANGO_SECRET_KEY))
print("  DB_PASSWORD:      ", masked(DB_PASSWORD))
print("  API_KEY:          ", masked(API_KEY))

if not all([DJANGO_SECRET_KEY, DB_PASSWORD, API_KEY]):
    raise SystemExit("Some secrets are missing — set them in .env")
print("All secrets present (nothing hardcoded in source)")
