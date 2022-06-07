# 라이브러리 불러오기
import requests
import xmltodict
import json
import pandas as pd
import math
from datetime import datetime, timedelta

start = "2022-01-01"
last = "2022-01-02"

start_date = datetime.strptime(start, "%Y-%m-%d")
last_date = datetime.strptime(last, "%Y-%m-%d")

while start_date <= last_date:
    dates = start_date.strftime("%Y%m%d")
    print(dates)

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

        print("\n date>"+dates+"page>"+timeStr+"\n")

        # openAPI 데이터 가져오기
        key = "aKvmHpFI2%2BTNf3LepeF8Whu34R7222pR%2FvJ43DIO4w75ZJ%2FT3xlde342akR7IENdds1rFokGa5yW4VzjMJcO0w%3D%3D"
        url = "http://apis.data.go.kr/1192000/select0040List/getselect0040List?serviceKey={}&pageNo={}&numOfRows=100&baseDt={}".format(
            key,timeStr,dates)

        cont = requests.get(url).content
        dict = xmltodict.parse(cont)
        jsonString = json.dumps(dict['responseXml']['body'], ensure_ascii=False)
        jsonObj = json.loads(jsonString)

        df = pd.DataFrame(jsonObj['item'])
        print(df.count())
        print(df)

        # openAPI 가져온 데이터 엑셀로 저장
        df.to_excel("jeon_"+dates+"_"+timeStr+".xlsx")

    start_date += timedelta(days=1)


# 저장된 엑셀 병합
import os
import pandas as pd
import glob

def merge_excel_files(file_path, file_format, save_path, save_format, columns=None):
    merge_df = pd.DataFrame()
    file_list = glob.glob(f"{file_path}/*{file_format}")

    for file in file_list:
        if file_format == ".xlsx":
            file_df = pd.read_excel(file)
        else:
            file_df = pd.read_csv(file)

        if columns is None:
            columns = file_df.columns

        temp_df = pd.DataFrame(file_df, columns=columns)

        merge_df = merge_df.append(temp_df)

    if save_format == ".xlsx":
        merge_df.to_excel(save_path, index=False)
    else:
        merge_df.to_csv(save_path, index=False)

if __name__ == "__main__":
    merge_excel_files(file_path="./", file_format=".xlsx",save_path="./merge_excel_now.xlsx", save_format=".xlsx")