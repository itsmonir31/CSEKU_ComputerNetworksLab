
import threading
import time
from tkinter import Y

WINDOW_SIZE = 4

data_ = "ABCDEFGHIJK"
ack = "1101110111111"
ack_passer = 0
data_passer = 0
acknoledged_data = 0

def run(stop):
    global data_passer, acknoledged_data 
    delay_time = 5
    for x in range(delay_time):
        # print("Data->", data_[data_passer],"---", x+1)
        print("\t\t", x+1, "sec", end =" . . . ")
        time.sleep(1)
        if stop():
            print("\t\t\t\t##> Acknowledged data -> ", data_[acknoledged_data], " <##\n")
            if data_passer <= len(data_):
                print("Data sent -> ", data_[data_passer-1])
            acknoledged_data += 1
            break
        elif x==delay_time-1:
            data_passer -= WINDOW_SIZE
            send_window(data_passer)
                 
def main():
    global ack_passer, data_passer
    stop_threads = False
    t1 = threading.Thread(target = run, args =(lambda : stop_threads, ))
    t1.start()
    # time.sleep(1)\
    # x = input()
    # print(ack[ack_passer])
    if ack[ack_passer] == '1':
        
        data_passer += 1
        
        stop_threads = True
        # print("Data sent -> ", data_[data_passer-1])
        # print(ack_passer)
    # else:
        # send_window(data_passer-WINDOW_SIZE)
    t1.join()
    print('\n')
    
    ack_passer += 1

def send_window(start):
    print("\n")
    global data_passer
    
    for m in range(WINDOW_SIZE):
        print("Data sent -> ", data_[start+m])
    data_passer += 4


send_window(0)
for x in range(len(ack)):
    main()