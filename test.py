import datetime as dt
from src.WhenWasThat import when

# datetime(year, month, day, hour, minute, second, microsecond)
time_then = dt.datetime(2020, 3, 23, 0, 1, 1, 1)
#time_then = dt.datetime.now()
#time.sleep(10)
print(time_then)

first_date = dt.datetime(2006, 10, 27, 11, 59, 32, 343001)
last_date = dt.datetime(2016, 9, 30, 20, 21, 43, 561783)
print(when(time_then).weeks)
print(when(time_then).natural)

titanic = dt.datetime(1912, 4, 15, 2, 20, 0, 0)
print("The Titanic sunk %s days ago." % round(when(titanic).days))