#Note this code is AI generated and may contain errors. Please review it carefully before using it in production. i will make my own in future but this is just wotking placeholder so please don hate on me THANKS >

import json
from pathlib import Path


class I18n:
    def __init__(self, language="sk"):
        self.language = language
        self.translations = {}
        self.load()

    def load(self):
        path = Path(__file__).parent / "language" / f"{self.language}.json"

        with open(path, "r", encoding="utf-8") as file:
            self.translations = json.load(file)

    def get(self, key, **kwargs):
        text = self.translations.get(key, key)

        if kwargs:
            text = text.format(**kwargs)

        return text