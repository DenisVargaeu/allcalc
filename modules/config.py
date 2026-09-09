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
def load_active_option():
    if config_path.exists():
        with open(config_path, "r", encoding="utf-8") as file:
            config = json.load(file)
            return config.get("active_option", "default")
    else:
        with open(config_path, "w", encoding="utf-8") as file:
            json.dump({"active_option": "default"}, file, indent=4)
            return "default"
def save_acive_option(option):
    if config_path.exists():
        with open(config_path, "r", encoding="utf-8") as file:
            config = json.load(file)
        config["active_option"] = option
        with open(config_path, "w", encoding="utf-8") as file:
            json.dump(config, file, indent=4)
    else:
        with open(config_path, "w", encoding="utf-8") as file:
            json.dump({"active_option": option}, file, indent=4)
def delete_active_option():
    if config_path.exists():
        with open(config_path, "r", encoding="utf-8") as file:
            config = json.load(file)
        if "active_option" in config:
            del config["active_option"]
        with open(config_path, "w", encoding="utf-8") as file:
            json.dump(config, file, indent=4) 

def new_user_check():
    if config_path.exists():
        with open(config_path, "r", encoding="utf-8") as file:
            config = json.load(file)
            return config.get("new", "default")
    else:
        with open(config_path, "w", encoding="utf-8") as file:
            json.dump({"new": "default"}, file, indent=4)
            return "default"
def edit_new(option):
    if config_path.exists():
        with open(config_path, "r", encoding="utf-8") as file:
            config = json.load(file)
        config["new"] = option
        with open(config_path, "w", encoding="utf-8") as file:
            json.dump(config, file, indent=4)
    else:
        with open(config_path, "w", encoding="utf-8") as file:
            json.dump({"new": option}, file, indent=4)
   