import requests
import xmltodict
import json
import pandas as pd


# openAPI 데이터 가져오기
key = "aKvmHpFI2%2BTNf3LepeF8Whu34R7222pR%2FvJ43DIO4w75ZJ%2FT3xlde342akR7IENdds1rFokGa5yW4VzjMJcO0w%3D%3D"
url = "http://apis.data.go.kr/1192000/select0020List/getselect0020List?serviceKey={}&pageNo=3&numOfRows=100".format(
    key)

cont = requests.get(url).content
dict = xmltodict.parse(cont)
jsonString = json.dumps(dict['responseXml']['body'], ensure_ascii=False)
jsonObj = json.loads(jsonString)

for item in jsonObj['item']:
    print(item)

df = pd.DataFrame(jsonObj['item'])
print(df.count())
print(df)

# openAPI 가져온 데이터 엑셀로 저장
df.to_excel("jeon_220515.xlsx")
