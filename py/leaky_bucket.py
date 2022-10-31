import random

in_bucket = 0

no_of_queries = int(input("No. of queries"))

int_bucket = random.randint(1,10)

bucket_size = int(input("Bucket Size"))

input_pkt_size = 4

# no. of packets that exits the bucket at a time
output_pkt_size = 1
for i in range(0, no_of_queries): # space left

	size_left = bucket_size - in_bucket
	if input_pkt_size <= size_left:
	# update in_bucket
		in_bucket += input_pkt_size
	else:
		print("Packet loss = ", input_pkt_size)

	print(f"Buffer size= {in_bucket} out of bucket size = {bucket_size}")

	# as packets are sent out into the network, the size of the in_bucket decreases
	in_bucket -= output_pkt_size


# This code is contributed by Arpit Jain
# Improved by: rishitchaudhary
