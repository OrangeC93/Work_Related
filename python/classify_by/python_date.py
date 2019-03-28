from datetime import datetime, date, timedelta
# strftime() is used to convert a time to string. 
# strptime is used to convert a date string to a datetime object.
from time import strftime, strptime # similar as datetime
from dateutil.rrule import rrule, DAILY, MONTHLY

# generate now() in date and datetime format
print(f'date format: {date.today()}, datetime format: {datetime.now()}\n')


# calculat the date difference
now = date.today() 
yesterday = now + timedelta(days=-1)
print(f'today date: {now}, yesterday date: {yesterday}\n')


# convert from date to string, vice versa
# strftime: creates a string representation of date or time from a datetime or time object.
now = date.today() 
string_now = now.strftime('%Y-%m-%d')
string_now_2 = str(now).split()[0]
print(f'convert date to string: {string_now}')
# strptime: creates a datetime or time object from a string.
date_now = datetime.strptime('Mon Feb 15 2010', '%a %b %d %Y')
print(f'convert string to datetime: {date_now}\n')


# convert datetime to date, vice versa
# .date()
now = datetime.today()
date_now = now.date()
print(f'convert datetime to date: {date_now}')
# convert date to string and then string to datetime
now = date.today()
datetime_now = datetime.strptime(now.strftime('%Y-%m-%d'), '%Y-%m-%d')
print(f'convert date to datetime: {datetime_now}\n')


# time loop
start = date(2018, 8, 25)
end = date(2018, 8, 29)
print(f'start: {start}, end: {end}')
for dt in rrule(freq=DAILY, dtstart=start, count=3): #until=end
    print(f'time loop: {dt.date()}')