from dotenv import load_dotenv
import os

load_dotenv()

DB_PASSWORD = os.getenv("DB_PASSWORD")
EMAIL_USERNAME = os.getenv("EMAIL_USERNAME")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
EMAIL_FROM = os.getenv("EMAIL_FROM")
MAIL_HOST = os.getenv("MAIL_HOST")
MAIL_BACKEND = os.getenv("MAIL_BACKEND")
MAIL_PORT = int(os.getenv("MAIL_PORT"))
MAIL_STARTTLS = bool(os.getenv("MAIL_STARTTLS"))
MAIL_USE_SSL = bool(os.getenv("MAIL_USE_SSL"))
MAIL_USE_TLS = bool(os.getenv("MAIL_USE_TLS"))