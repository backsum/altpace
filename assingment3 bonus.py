import time
from re import match

time_input = input("Insert time to countdown (h:m:s) ")
pattern = r'^(\d|0\d|1\d|2[0-3]):([0-5]?\d):([0-5]?\d)$' # Checking if the input is correct (h: 0-23, m: 0-59, s: 0-59)
if match(pattern, time_input):
    h, m, s = time_input.rsplit(sep=':') # Creating a list containing hours, minutes, seconds and assigning it to h, m, s
    time_sec = int(h) * 3600 + int(m) * 60 + int(s) 
    for _ in range(time_sec + 1): # Adding 1 for countdowning to 0, because we include the starting time in countdown
        # Second argument of strftime uses gmtime to convert seconds into a time tuple (y, m, d, h, m, s, wd, yd, isdst)
        # y: year, m: month, d: day, h: hour, m: minute, s: second, wd: weekday, yd: yearday, isdst: daylight saving time
        # First argument declares the format of the output (h:m:s), which is taken from the time tuple
        print(time.strftime("%H:%M:%S", time.gmtime(time_sec))) 
        print(time.gmtime(time_sec)) 
        time_sec -= 1
        time.sleep(1)
else:
    print('''\nSorry, can't countdown from this :( 
You can enter up to 23 hours, 59 minutes, and 59 seconds. 
The required format is "hours:minutes:seconds".''')
