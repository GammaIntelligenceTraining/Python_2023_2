import datetime
#
# d = datetime.date(2024, 1, 3)
# print(d)
# print(type(d))

today = datetime.date.today()
# print(today)
# print(today.year)
# print(today.month)
# print(today.day)
# print(f'{today.day}.{today.month}.{today.year}')
# print(d.weekday())
# print(d.isoweekday())
# print(type(today - d))
#
# # date1 - date2 = tdelta
# # date1 - tdelta = date2
#
# tdelta = datetime.timedelta(days=5, hours=10)
# print(today + tdelta)

# bday = datetime.date(2024, 3, 16)
# print((bday - today).total_seconds())
#
# tdelta = datetime.timedelta(days=12, minutes=13, hours=5).total_seconds()
# print(tdelta)
#

# t = datetime.time(12, 32, 45, 12312)
# print(t.hour)
# print(t.minute)
# print(t.second)
# print(t.microsecond)
#
# tdelta = datetime.timedelta(hours=3)
# print(t - tdelta)

# dt = datetime.datetime(2024, 1, 1, 12, 30, 32, 123123)
# print(dt)
# print(dt.date())
# print(dt.time())
#
# today = datetime.datetime.now()
# print(today - dt)
# tdelta = datetime.timedelta(days=2, hours=12, minutes=15)
# print(today + tdelta)

dt_today = datetime.datetime.now()
#
# print(dt_today)
# print(dt_today.strftime('%d/%B-%A*%Y asdas ( %I )'))
# print(dt_today.strftime('%c'))

dt_str = 'Märts 30, 2024 10:24PM'
dt_str = dt_str.replace('Märts', 'March')
dt = datetime.datetime.strptime(dt_str, '%B %d, %Y %I:%M%p')
print(dt)
print(type(dt))
print(dt.replace(year=2025))

dt_now = datetime.datetime.now()
print(dt_now.timestamp())
print(datetime.datetime.fromtimestamp(1704725394.871331))