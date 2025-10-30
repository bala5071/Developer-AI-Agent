import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

# Ollama Configuration
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "llama3")
OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")

# GitHub Configuration
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN", "")
GITHUB_USERNAME = os.getenv("GITHUB_USERNAME", "")

# Project Paths
BASE_DIR = Path(__file__).parent
OUTPUT_DIR = BASE_DIR / "output" / "projects"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Agent Configuration
AGENT_VERBOSE = True
MAX_ITERATIONS = 15

# File Extensions for Different Project Types
PROJECT_EXTENSIONS = {
    "python": [".py", ".txt", ".md", ".yml", ".yaml", ".json"],
    "javascript": [".js", ".jsx", ".json", ".md", ".html", ".css"],
    "web": [".html", ".css", ".js", ".json", ".md"],
    "ml": [".py", ".ipynb", ".txt", ".md", ".pkl", ".h5"],
}

# Testing Configuration
TEST_TIMEOUT = 300  # seconds
RUN_TESTS = True