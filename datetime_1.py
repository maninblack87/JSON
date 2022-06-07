import datetime

today=datetime.date.today()
formToday=today.strftime("%Y%m%d")
print(formToday)

diff_days=datetime.timedelta(days=10)

d_day=today-diff_days
formD_day=d_day.strftime("%Y%m%d")
print(formD_day)