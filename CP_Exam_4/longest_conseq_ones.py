def longest_conseq_ones(num):
	num = bin(num)[2:]
	num = str(num)
	count = 0
	maxcount = 0
	# print(num)
	for i in range(0,len(num)):
		if num[i] == '1':
			count+=1
		else:
			if(maxcount<count):
				maxcount = count
			count=0
			
	if(maxcount<count):
		maxcount = count
	print(maxcount)

longest_conseq_ones(0)
longest_conseq_ones(55)
longest_conseq_ones(-5)
longest_conseq_ones(12354)
longest_conseq_ones(6)
longest_conseq_ones(256)
