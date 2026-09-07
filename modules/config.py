import json
from pathlib import Path

# Koreňový priečinok projektu
BASE_DIR = Path(__file__).resolve().parent.parent

# Config bude vždy v koreňovom priečinku
config_path = BASE_DIR / "config.json"


def load_language():
    if config_path.exists():
        with open(config_path, "r", encoding="utf-8") as file:
            config = json.load(file)
            return config.get("language", "en")
    else:
        with open(config_path, "w", encoding="utf-8") as file:
            json.dump({"language": "en"}, file, indent=4)
            return "en"


def edit_language(lang):
    if config_path.exists():
        with open(config_path, "r", encoding="utf-8") as file:
            config = json.load(file)
        config["language"] = lang
        with open(config_path, "w", encoding="utf-8") as file:
            json.dump(config, file, indent=4)
    else:
        with open(config_path, "w", encoding="utf-8") as file:
            json.dump({"language": lang}, file, indent=4)