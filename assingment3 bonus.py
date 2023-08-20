import time

time_input = input("Insert time to countdown (H:M:S) ")

h, m, s = time_input.rsplit(sep=':') # creating a list containing hours, minutes, seconds
time_sec = int(h) * 3600 + int(m) * 60 + int(s)
    
for _ in range(time_sec + 1): # adding 1 to countdown to 0, because we indicate the starting time
    print(time.strftime("%H:%M:%S", time.gmtime(time_sec)))
    time_sec -= 1
    time.sleep(1)
