import os
from dotenv import load_dotenv
import logging

# Load environment variables from .env file
load_dotenv()

# Reddit API credentials
REDDIT_CLIENT_ID = os.getenv('REDDIT_CLIENT_ID')
REDDIT_CLIENT_SECRET = os.getenv('REDDIT_CLIENT_SECRET')
REDDIT_USER_AGENT = os.getenv('REDDIT_USER_AGENT')
REDDIT_USERNAME = os.getenv('REDDIT_USERNAME')
REDDIT_PASSWORD = os.getenv('REDDIT_PASSWORD')

# OpenRoute API key
OPENROUTE_API_KEY = os.getenv('OPENROUTE_API_KEY')

# Logging setup
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s',
    handlers=[logging.StreamHandler()]
)

# Model definitions (example, update as needed)
MODELS = {
    'demographics': 'qwen/qwen3-235b-a22b:free',
    'communication': 'qwen/qwen3-235b-a22b:free',
    'interests': 'qwen/qwen3-235b-a22b:free',
    'technology': 'qwen/qwen3-235b-a22b:free',
    'quotes': 'qwen/qwen3-235b-a22b:free',
    'compiler': 'nvidia/llama-3.3-nemotron-super-49b-v1:free',
}
