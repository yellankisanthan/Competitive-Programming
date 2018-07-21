def counting_bits(num):
	i = 0
	lis = []
	while(i<=num):
		n = bin(i)[2:]
		n = str(n)
		count = n.count("1")
		lis.append(count)
		i+=1
	print(lis)


counting_bits(15)
counting_bits(16)
counting_bits(1)
counting_bits(25)
counting_bits(5)
counting_bits(6)

