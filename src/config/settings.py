import os
from dotenv import load_dotenv
from pathlib import Path


class NotFoundEnv(Exception):
    pass

BASE_DIR = Path(__file__).resolve().parent

path = BASE_DIR / ".env"
load_dotenv(path) if os.path.exists(path) else load_dotenv()

ENVIRONMENT = {}

ENV_NAME = ["origin", "rate_limit", "global_rate_limit", "environment", "block", "block_limit", "path", "url"]
OPTIONAL = ["block", "block_limit"]

for name in ENV_NAME:

    env = os.getenv(name)
    if env is None and not name in OPTIONAL:

        raise NotFoundEnv(f"Expeted env {name}")

    ENVIRONMENT[name] = env



if ENVIRONMENT["block"] and not ENVIRONMENT["block_limit"]:

    raise KeyError(
        "if env block is not None, so exepeted env block_limit"
    )
 












