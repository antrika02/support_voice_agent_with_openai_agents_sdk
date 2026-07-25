import os
from dotenv import load_dotenv

load_dotenv()

def get_env_variable(name: str, default=None, required=False):
    value = os.getenv(name, default)

    if required and value is None:
        raise ValueError(f"Missing required environment variable: {name}")

    return value


FIRECRAWL_API_KEY = get_env_variable(
    "FIRECRAWL_API_KEY",
    required=True
)

HUGGINGFACE_API_KEY = get_env_variable(
    "HUGGINGFACE_API_KEY",
    required=True
)

QDRANT_URL = get_env_variable(
    "QDRANT_URL",
    required=True
)

QDRANT_API_KEY = get_env_variable(
    "QDRANT_API_KEY",
    required=True
)

COLLECTION_NAME = get_env_variable(
    "COLLECTION_NAME",
    default="docs_embeddings"
)

VOICE_NAME = get_env_variable(
    "VOICE_NAME",
    default="en-US-AriaNeural"
)