# 라이브러리 불러오기

import requests
import xmltodict
import json
import pandas as pd
import math
from datetime import datetime, timedelta
import os
import glob



# 기준일자 시작과 끝 설정하기

# 상시 수정 필요 --> [ start(시작 기준일), last(마지막 기준일) ]
start = "2021-01-01"
last = "2021-01-02"
start_date = datetime.strptime(start, "%Y-%m-%d")
last_date = datetime.strptime(last, "%Y-%m-%d")



# 기준일 동안 반복문 실행(Open API마다 처리해야 될 데이터 수량 산출 및 엑셀 파일로 시각화)
while start_date <= last_date:
    dates = start_date.strftime("%Y%m%d")
    

    # 상시 수정 필요 --> [rows(1페이지 당 나타낼 데이터 열의 개수), key(인증키), url(서비스 url)]
    # 필히 해당 오픈 API의 참고문서 중 "1.1.다.1)d) 요청/응답 메시지 예제"항목 참고 부탁드리겠습니다.
    rows = "100"
    key = "aKvmHpFI2%2BTNf3LepeF8Whu34R7222pR%2FvJ43DIO4w75ZJ%2FT3xlde342akR7IENdds1rFokGa5yW4VzjMJcO0w%3D%3D"
    url = "http://apis.data.go.kr/1192000/select0040List/getselect0040List?type=xml&serviceKey={}&pageNo=1&numOfRows={}&baseDt={}".format(
        key,rows,dates)

    cont = requests.get(url).content
    dict = xmltodict.parse(cont)
    temp_str = dict['responseXml']['header']
    val = "totalCount" in temp_str
    if val:
        jsonString = json.dumps(dict['responseXml']['header'], ensure_ascii=False)
        jsonObj = json.loads(jsonString)
    else:
        jsonString = json.dumps(dict['responseXml']['body'], ensure_ascii=False)
        jsonObj = json.loads(jsonString)

    # 페이지 개수 결과
    pageNumber = math.ceil(int(jsonObj['totalCount'])/int(rows))


    # 페이지 개수동안 반복문 실행(엑셀 파일로 시각화)
    time = 0
    while time < pageNumber:

        time = time+1
        timeStr = str(time)

        print("\n 날짜>"+dates+" 페이지 개수>"+timeStr+"\n")

        # 상시 수정 필요 --> [rows(1페이지 당 나타낼 데이터 열의 개수), key(인증키), url(서비스 url)]
        # 필히 해당 오픈 API의 참고문서 중 "1.1.다.1)d) 요청/응답 메시지 예제"항목 참고 부탁드리겠습니다.
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


    # 다음날로 점프

    start_date += timedelta(days=1)



# xlsx(엑셀 형식) 하나로 병합

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