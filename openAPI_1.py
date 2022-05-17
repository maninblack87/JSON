import requests
import xmltodict
import json
import pandas as pd

key = "aKvmHpFI2%2BTNf3LepeF8Whu34R7222pR%2FvJ43DIO4w75ZJ%2FT3xlde342akR7IENdds1rFokGa5yW4VzjMJcO0w%3D%3D"
url = "http://apis.data.go.kr/1192000/select0020List/getselect0020List?serviceKey={}&pageNo=1&numOfRows=100".format(
    key)

content = requests.get(url).content
dict = xmltodict.parse(content)
jsonString = json.dumps(dict['responseXml']['body'], ensure_ascii=False)
jsonObj = json.loads(jsonString)

for item in jsonObj['item']:
    print(item)
    print("사업장주소 >", item["addr"], "우편번호 >", item["zip"])

df = pd.DataFrame(jsonObj['item'])
print(df.count())
    
