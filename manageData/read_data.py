import json

class ReadData:
    def __init__(self, path="data/client.json"):
        self.path = path

    def read_Client(self, key):
        with open(self.path, encoding="utf-8") as f:
            data = json.load(f)

        return data[key]