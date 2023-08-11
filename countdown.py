import time

t = int(input("Enter time in seconds: "))

running = True
while(running):
    if(t != 0):
        secs = int(t % 60)
        min = int(t / 60) % 60
        hours = int( t / 3600)
        timer = " {:02d}:{:02d}:{:02d}".format(hours, min, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
    else:
        running =False
    
    # can use a function and pass "t" to it for betterment 