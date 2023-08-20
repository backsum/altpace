import time
from re import match

time_input = input("Insert time to countdown (H:M:S) ")
pattern = r'^(\d|0\d|1\d|2[0-3]):([0-5]?\d):([0-5]?\d)$' # Checking if the input is correct (h: 0-23, m: 0-59, s: 0-59)
if match(pattern, time_input):
    h, m, s = time_input.rsplit(sep=':') # Creating a list containing hours, minutes, seconds
    time_sec = int(h) * 3600 + int(m) * 60 + int(s)
    for _ in range(time_sec + 1): # Adding 1 to countdown to 0, because we indicate the starting time
        print(time.strftime("%H:%M:%S", time.gmtime(time_sec)))
        time_sec -= 1
        time.sleep(1)
else:
    print('''    Sorry, can't countdown from this :( 
    You can enter up to 23 hours, 59 minutes, and 59 seconds. 
    The required format is "hours:minutes:seconds".''')
