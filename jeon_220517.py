# 라이브러리 불러오기
import requests
import xmltodict
import json
import pandas as pd
import math

# 반복문 실행을 위한 time값(크롤링할 페이지 개수) 설정
key = "aKvmHpFI2%2BTNf3LepeF8Whu34R7222pR%2FvJ43DIO4w75ZJ%2FT3xlde342akR7IENdds1rFokGa5yW4VzjMJcO0w%3D%3D"
url = "http://apis.data.go.kr/1192000/select0040List/getselect0040List?serviceKey={}&pageNo=1&numOfRows=100&baseDt=20220101".format(
    key)

cont = requests.get(url).content
dict = xmltodict.parse(cont)
jsonString = json.dumps(dict['responseXml']['header'], ensure_ascii=False)
jsonObj = json.loads(jsonString)

pageNumber = math.ceil(int(jsonObj['totalCount'])/100)
print(pageNumber)
print(dict['responseXml']['header'])

time = 0
while time < pageNumber:

    time = time+1
    timeStr = str(time)

    print("\n"+timeStr+"번째\n")

    # openAPI 데이터 가져오기
    key = "aKvmHpFI2%2BTNf3LepeF8Whu34R7222pR%2FvJ43DIO4w75ZJ%2FT3xlde342akR7IENdds1rFokGa5yW4VzjMJcO0w%3D%3D"
    url = "http://apis.data.go.kr/1192000/select0040List/getselect0040List?serviceKey={}&pageNo={}&numOfRows=100&baseDt=20220101".format(
        key,timeStr)

    cont = requests.get(url).content
    dict = xmltodict.parse(cont)
    jsonString = json.dumps(dict['responseXml']['body'], ensure_ascii=False)
    jsonObj = json.loads(jsonString)

    df = pd.DataFrame(jsonObj['item'])
    print(df.count())
    print(df)

    # openAPI 가져온 데이터 엑셀로 저장
    df.to_excel("jeon_220517_2nd_"+timeStr+".xlsx")