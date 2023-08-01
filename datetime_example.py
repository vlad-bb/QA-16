import datetime
import calendar

some_date = "23.07.2016 22:55"
print(some_date, type(some_date))
same_date_dt = datetime.datetime.strptime(some_date, "%d.%m.%Y %H:%M")
print(same_date_dt, type(same_date_dt))

custom_date = same_date_dt.strftime("%B %A %Y-%b-%d %c %I:%M:%S:%f %p")
print(custom_date)
print(calendar.isleap(same_date_dt.year))