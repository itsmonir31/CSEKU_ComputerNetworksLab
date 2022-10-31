import array as arr
from dataclasses import dataclass
from re import L

remain=0
dropped=0

bucket_size =500# int(input("Bucket Size: "))
output_datarate =200# int(input("Output Data-rate: "))

# arr = arr.array('i');


count =2# int(input("How many data packets you want to send? "))

# for i in range(count):
#     print("No. of packets coming at sec-", i+1 , ": ")
#     packet_size = int(input())

#     arr.append(packet_size)

arr = arr.array('i', [600, 400])

print("Time\tReceived\tSent\tDropped\tRemaining")
# print(arr)

k=0
while k < count or remain > 0:
    if k < count:
        l = arr[k]
        if l > output_datarate:
            passs = output_datarate
            rem = l-output_datarate
            remain += rem
        else:
            passs = l
        
        if remain > bucket_size:
            dropped = remain - bucket_size
            remain = remain - dropped
        else:
            dropped = 0

    else:
        l=0
        if remain > output_datarate:
            passs = output_datarate
            remain = remain - output_datarate
        else:
            passs = remain
            remain = remain - passs
        
        if rem > bucket_size:
            dropped = remain - bucket_size
            remain = remain - dropped
        else:
            dropped = 0

    print(k+1, "\t", l, "\t", passs, "\t", dropped, "\t", remain)

    k +=1




    

