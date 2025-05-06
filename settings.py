import os
import tomllib
from dotenv import load_dotenv
from typing import Dict, Any

def load_toml(path: str) -> Dict[Any, Any]:
    with open(path, "rb") as f:
        toml_data = tomllib.load(f)
    return toml_data

config_data = load_toml("config.toml")

LOGS_DIR = config_data["logs_dir"]
load_dotenv(config_data["env_path"])
token = os.getenv("TOKEN")
colours = config_data["colours"]
