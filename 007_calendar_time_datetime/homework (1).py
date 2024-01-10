from datetime import datetime, timedelta, timezone

sample1 = 'Jan 1 2014 2:43PM'
# print(datetime.strptime(sample1, ''))
sample2 = '14:20 10/12/22'  # YY/MM/DD
sample3 = 'Tuesday, September 24, 2019'
sample4 = '01.01.1970 - 00:00:01'

def convert_to_datetime(date_str):
    formats = ['%b %d %Y %I:%M%p', '%H:%M %m/%d/%y', '%A, %B %d, %Y', '%m.%d.%Y - %H:%M:%S']
    for fmt in formats:
        try:
            return datetime.strptime(date_str, fmt)
        except ValueError:
            pass
    # raise ValueError(f"Unable to parse the date string: {date_str}")

def print_dates():
    today = datetime.now()
    yesterday = today - timedelta(days=1)
    tomorrow = today + timedelta(days=1)
    print(f"Yesterday: {yesterday.strftime('%Y-%m-%d')}")
    print(f"Today: {today.strftime('%Y-%m-%d')}")
    print(f"Tomorrow: {tomorrow.strftime('%Y-%m-%d')}")

some_day = 1014163200
def timestamp_to_date(timestamp):
    utc_datetime = datetime.fromtimestamp(timestamp, timezone.utc)
    return utc_datetime.strftime('%d.%m.%Y')

def subtract_two_weeks(timestamp):
    two_weeks_delta = timedelta(weeks=2)
    new_timestamp = timestamp - two_weeks_delta.total_seconds()
    return new_timestamp

sample1_date = convert_to_datetime(sample1)
sample2_date = convert_to_datetime(sample2)
sample3_date = convert_to_datetime(sample3)
sample4_date = convert_to_datetime(sample4)

# print_dates()
#
print(convert_to_datetime(sample1))

# some_day_date = timestamp_to_date(some_day)
# print(f"Converted timestamp: {some_day_date}")
#
# new_timestamp = subtract_two_weeks(some_day)
# print(f"New timestamp after subtracting 2 weeks: {new_timestamp}")

# print(datetime.strptime('30 Nov', '%d %m'))