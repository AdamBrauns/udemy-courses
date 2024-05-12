'''
Python has the datetime module to help deal with timestamps in
your code. Time values are represented with the time class. Times
have attributes for hour, minute, second, and microsecond. They
can also include time zone information. The arguments to initialize
a time instance are optional, but the default of 0 is unlikely to
be what you want.
'''
import datetime

# (hour, min, sec, microsec, timezone info)
t = datetime.time(5, 25, 1)

# Print various properties
print(t)
print(t.hour)
print(t.minute)
print(t.microsecond)

print()

# Print various properties
print(datetime.time.min)
print(datetime.time.max)
print(datetime.time.resolution)

print()

# Call today method and print various properties
today = datetime.date.today()
print(today)
print(today.timetuple())
print(today.year)
print(today.month)
print(today.day)

print()

# Print various properties
print(datetime.date.min)
print(datetime.date.max)
print(datetime.date.resolution)

print()

# Date arithmetic
d1 = datetime.date(2015, 3, 11)
print(d1)

d2 = d1.replace(year=1990)
print(d2)

print(d1 - d2)