import json

#jsonファイルを読み込みjsonを返却
def readJsonFile(fileName):
    json_open = open(fileName, 'r')
    json_load = json.load(json_open)

    return json_load