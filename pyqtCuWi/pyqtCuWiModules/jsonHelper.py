#          Custom Widgets For PyQt5 Module           #
#          GPL 3.0 - myygunduz - pyqtCuWi            #
#        https://github.com/myygunduz/pyqtCuWi       #

import json

def writeJ(contents, file, indent: int = 2):
    with open(file, "w") as f:
        json.dump(contents, f, indent=indent, ensure_ascii=False)


def readJ(file:str):
    json_file = open(file, "r")
    contents = json.load(json_file)
    json_file.close()
    return contents