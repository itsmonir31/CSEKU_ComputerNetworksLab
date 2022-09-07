
# Python program killing
# threads using stop
# flag
 
import threading
import time
from tkinter import Y

data_ = "AASDFG"
ack = "110001111"
ack_passer = 0
data_passer = 0

def run(stop):
    for x in range(5):
        # print("Data->"+ data_[data_passer] + "---" + x+1)
        print("Data->", data_[data_passer],"---", x+1)
        time.sleep(1)
        if stop():
            print("Acknowledged")
            break
                 
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
        # print(ack_passer)
    t1.join()
    print('\n')
    ack_passer += 1

for x in range(len(ack)):
    main()