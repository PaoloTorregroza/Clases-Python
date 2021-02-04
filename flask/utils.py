import json


def readJson():
    with open("dataBase.json") as f:
        return json.load(f)
