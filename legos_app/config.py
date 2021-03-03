"""Initialize Config class to access environment variables."""
from dotenv import load_dotenv
import os

load_dotenv()

class Config(object):
    """Set environment variables."""

    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv('SECRET_KEY')
