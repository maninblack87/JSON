# JSON 파일을 읽어서 파이썬으로 접근 및 출력

import json

file_path = 'c:/jeon/json/savejson.json'

# 파일 읽어오기 (r 모드)
with open(file_path, 'r')as fp:
    data = json.load(fp)

print(json.dumps(data, indent=4))

# ? dump 와 dumps 의 차이점
# ? dumps의 상세 기능
