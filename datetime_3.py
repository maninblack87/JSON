from datetime import datetime, timedelta

start = "2022-06-02"
last = "2022-06-08"

start_date = datetime.strptime(start, "%Y-%m-%d")
last_date = datetime.strptime(last, "%Y-%m-%d")

# print(type(start_date))
# print(start_date)

while start_date <= last_date:
    dates = start_date.strftime("%Y%m%d")
    print(dates)

    start_date += timedelta(days=1)