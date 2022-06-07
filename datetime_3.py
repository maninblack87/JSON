from datetime import datetime, timedelta

start = "2021-01-01"
last = "2021-01-02"

start_date = datetime.strptime(start, "%Y-%m-%d")
last_date = datetime.strptime(last, "%Y-%m-%d")

while start_date <= last_date:
    dates = start_date.strftime("%Y%m%d")
    print(dates)

    start_date += timedelta(days=1)