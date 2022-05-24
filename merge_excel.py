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