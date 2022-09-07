from time import *
import threading

def countdown():
    global timer_, forcekill

    timer_ = 5

    for x in range(5):
        timer_ = timer_ - 1
        sleep(1)
        if forcekill:
            break

    print("Out o time", timer_)

for x in range(5):
    forcekill = False
    countdown_thread = threading.Thread(target = countdown)
    countdown_thread.start()

    while timer_ > 0:
        print("ppopoj", x)
        sleep(1)
        # if x == 5:
        #     countdown_thread.join()
        x = input()
        if x=='y':
            forcekill = True
            # timer_ = 0;
            # print(x)
            countdown_thread.join()
            break

