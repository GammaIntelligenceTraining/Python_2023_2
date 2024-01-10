
# Write a program that converts given string to datetime object
import datetime

sample1 = 'Jan 1 2014 2:43PM'
dt1 = datetime.datetime.strptime(sample1, '%b %d %Y %I:%M%p')
print(dt1)
sample2 = '14:20 10/12/22'  # YY/MM/DD
dt2 = datetime.datetime.strptime(sample2, '%H:%M %y/%m/%d')
print(dt2)
sample3 = 'Tuesday, September 24, 2019'
dt3 = datetime.datetime.strptime(sample3, '%A, %B %d, %Y').date()
print(dt3)
sample4 = '01.01.1970 - 00:00:01'
dt4 = datetime.datetime.strptime(sample4, '%d.%m.%Y - %H:%M:%S')
print(dt4)


# Write a program to print yesterdays, today and tomorrow dates
today = datetime.date.today()
yesterday = today - datetime.timedelta(days=1)
tomorrow = today + datetime.timedelta(days=1)
print('Yesterday', yesterday)
print('Today', today)
print('Tomorrow', tomorrow)


# Write a program to convert given timestamp to dd.mm.yyyy format
some_day = 1014163200
result = datetime.datetime.fromtimestamp(some_day)
print(result.strftime('%d.%m.%Y'))


# Write a function to subtract 2 weeks from timestamp and return new timestamp
# input: timestamp (float)
# output: timestamp (float)
def two_weeks_before(ts):
    delta = datetime.timedelta(days=14)
    # result = ts - delta.total_seconds()
    # return result
    result = datetime.datetime.fromtimestamp(ts)
    return  (result - delta).timestamp()

# x = two_weeks_before(1014163200)
# print(datetime.datetime.fromtimestamp(x))
