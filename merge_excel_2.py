import pandas as pd
import glob

try:
    path = './'
    files = glob.glob(path + "*.xlsx")
    excel = pd.DataFrame()
    for file_name in files:
        df = pd.read_excel(file_name)
        excel = excel.append(df, ignore_index=True)
    print(excel)
    print(excel.count())

    excel.to_excel("jeon_220517_2nd.xlsx")

except Exception as ex:
    print('error'+str(ex))