import json
import os

default_config = {"prefix": ";", "token": "", "default_server": "default" ,  "webhook_url": "", "webhook_logging_enabled": False }


class Config:
    def __init__(self, filename="config.json"):
        self.filename = filename
        self.config = {}
        if not os.path.isfile(filename):
            with open(filename, "w") as file:
                json.dump(default_config, file)
        with open(filename) as file:
            self.config = json.load(file)
        self.prefix = self.config.get("prefix", default_config.get("prefix"))
        self.token = self.config.get("token", default_config.get("token"))
        self.default_server = self.config.get(
            "default_server", default_config.get("default_server")
        )
        

        self.webhook_url = self.config.get("webhook_url", default_config.get("webhook_url"))
        self.webhook_logging_enabled = self.config.get("webhook_logging_enabled", default_config.get("webhook_logging_enabled"))

    def store(self):
        c = {
            "prefix": self.prefix,
            "token": self.token,
            "webhook_url": self.webhook_url,
            "webhook_logging_enabled": self.webhook_logging_enabled
        }
        with open(self.filename, "w") as file:
            json.dump(c, file)
