import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'dev-key-change-in-production')
    GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')
    GITHUB_USERNAME = os.getenv('GITHUB_USERNAME')
    SUBSTACK_URL = os.getenv('SUBSTACK_URL')
    DATABASE_PATH = os.path.join(os.path.dirname(__file__), 'personal_hub.db')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + DATABASE_PATH
    SQLALCHEMY_TRACK_MODIFICATIONS = False 