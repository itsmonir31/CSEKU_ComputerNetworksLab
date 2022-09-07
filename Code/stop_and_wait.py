import _thread
from multiprocessing.connection import wait
import random
import string

flag = 1
data = ''
i = 0


def sender(a):
    global flag
    global data
    global i
    file_create()
    while(True):
        if data[i] == '1':
            break
        if flag == 1:
            print("Sending  : ", data[i])
            wait(1000)
            i += 1
            flag = 0


def receiver(a):
    global flag
    global i

    while(True):
        if flag == 0:
            print("Recieved : ", data[i-1])
            flag = 1
            if data[i] == '1':
                break


def file_create():
    file = open('prac4_input.txt', 'w')
    n = random.randint(10, 20)
    res = ''.join(random.choices(string.ascii_uppercase, k=n))
    res = res + '1'
    file.write(res)
    # print("hi")


if __name__ == '__main__':

    file_create()
    file = open("Prac4_input.txt", "r")
    data = file.readline()
    print("The data is : ", data)
    a = 0
    t1 = _thread.start_new_thread(sender, (a,))
    t2 = _thread.start_new_thread(receiver, (a,))