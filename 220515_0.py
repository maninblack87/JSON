import urllib.request as request
import json

json_str = """[
{"name":"사과", "price":1000},
{"name":"바나나", "price":2000},
{"name":"배", "price":3000},
{"name":"귤", "price":4000}
]"""

# JSON 문자열 => 파이썬 자료형
output = json.loads(json_str)
print(type(output))
print(output)

# 파이썬 자료형 => JSON 문자열
text = json.dumps(output)
print(type(text))
print(text)
