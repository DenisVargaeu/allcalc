import json
from pathlib import Path

# AllCalc config v používateľskom home
CONFIG_DIR = Path.home() / ".allcalc"
config_path = CONFIG_DIR / "config.json"


def ensure_config():
    CONFIG_DIR.mkdir(parents=True, exist_ok=True)

    if not config_path.exists():
        with open(config_path, "w", encoding="utf-8") as file:
            json.dump(
                {
                    "language": "en",
                    "active_option": "0",
                    "new": "1"
                },
                file,
                indent=4
            )


def load_language():
    ensure_config()

    with open(config_path, "r", encoding="utf-8") as file:
        config = json.load(file)

    return config.get("language", "en")


def edit_language(lang):
    ensure_config()

    with open(config_path, "r", encoding="utf-8") as file:
        config = json.load(file)

    config["language"] = lang

    with open(config_path, "w", encoding="utf-8") as file:
        json.dump(config, file, indent=4)


def load_active_option():
    ensure_config()

    with open(config_path, "r", encoding="utf-8") as file:
        config = json.load(file)

    return config.get("active_option", "0")


def save_acive_option(option):
    ensure_config()

    with open(config_path, "r", encoding="utf-8") as file:
        config = json.load(file)

    config["active_option"] = option

    with open(config_path, "w", encoding="utf-8") as file:
        json.dump(config, file, indent=4)


def delete_active_option():
    ensure_config()

    with open(config_path, "r", encoding="utf-8") as file:
        config = json.load(file)

    if "active_option" in config:
        del config["active_option"]

    with open(config_path, "w", encoding="utf-8") as file:
        json.dump(config, file, indent=4)


def new_user_check():
    ensure_config()

    with open(config_path, "r", encoding="utf-8") as file:
        config = json.load(file)

    return config.get("new", "1")


def edit_new(option):
    ensure_config()

    with open(config_path, "r", encoding="utf-8") as file:
        config = json.load(file)

    config["new"] = option

    with open(config_path, "w", encoding="utf-8") as file:
        json.dump(config, file, indent=4)