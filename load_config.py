import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get environment variables or raise error if missing
def get_required_env(var_name):
    value = os.environ.get(var_name)
    if not value:
        raise ValueError(f"Missing required environment variable: {var_name}")
    return value

# Get all required variables
GITHUB_TOKEN = get_required_env('GITHUB_TOKEN')
GITHUB_REPO_OWNER = get_required_env('GITHUB_REPO_OWNER')
GITHUB_REPO_NAME = get_required_env('GITHUB_REPO_NAME')
GITHUB_PR_NUMBER = get_required_env('GITHUB_PR_NUMBER') 