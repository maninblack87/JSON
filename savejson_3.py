# JSON 파일을 읽고, 수정하고 다시 JSON 파일로 저장

import json

file_path = 'c:/jeon/json/savejson.json'

with open(file_path, 'r')as fp:
    data = json.load(fp)

data["test"] = False
data["hobby"][2] = 'coding'
# 다른 케이스 : data["jeon"]["hobby"] = data["jeon"]["hobby"]+["smart phone"]
data["hobby"] = data["hobby"]+["smart phone"]

with open(file_path, 'w', encoding='utf-8')as fp:
    json.dump(data, fp, indent=4)
    # ? load 와 loads 의 차이점
