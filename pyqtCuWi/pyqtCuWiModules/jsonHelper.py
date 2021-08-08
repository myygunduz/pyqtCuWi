import json


def writeJ(contents, file, indent: int = 2):
    with open(file, "w") as f:
        json.dump(contents, f, indent=indent, ensure_ascii=False)


def readJ(file:str):
    json_file = open(file, "r")
    contents = json.load(json_file)
    json_file.close()
    return contents