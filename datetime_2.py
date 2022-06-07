import datetime

now = datetime.datetime.now()
f_now = now.strftime('%Y-%m-%d')
p_now = datetime.datetime.strptime(f_now, '%Y-%m-%d')
print(p_now)

dday = datetime.datetime(2022,6,13)
f_dday = dday.strftime('%Y-%m-%d')
p_dday = datetime.datetime.strptime(f_dday, '%Y-%m-%d')
print(p_dday)

wday = p_dday-p_now
print(wday)