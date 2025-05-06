import tomllib
from typing import Dict, Any

def load_toml(path: str) -> Dict[Any, Any]:
    with open(path, "rb") as f:
        toml_data = tomllib.load(f)
    return toml_data

config_data = load_toml("config.toml")

