import os
import pandas as pd

file_format = ".xlsx"
file_path = "c:/jeon/json"
file_list = [f"{file_format}/{file}" for file in os.listdir(file_path) if file_format in file]

merge_df = pd.DataFrame()

# .xlsx 이면
for file_name in file_list:
    file_df = pd.read_excel(file_name)

# .cvs 이면
# for file_name in file_list:
#     file_df = pd.read_csv(file_name, encoding='utf-8')

columns = list(file_df.columns)

temp_df = pd.DataFrame(file_df, colums=columns)