data_ = "AASDFG"
ack = "110001111"
ack_passer = 0
data_passer = 0

def run():
    for x in range(5):
        print("Data->", data_[data_passer],"---", x)


run()