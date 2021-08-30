import datetime as dt
import time
import when

# datetime(year, month, day, hour, minute, second, microsecond)
time_then = dt.datetime(2018, 3, 27, 11, 59, 32, 343001)
#time_then = dt.datetime.now()
print(time_then)
#time.sleep(10)
print(when.whenWasThat(time_then).natural)