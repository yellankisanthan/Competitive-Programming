def hamming_distance(x, y):
	x = bin(x)[2:]
	y = bin(y)[2:]
	x = x+""
	y = y+""
	if len(x)<len(y):
		padding = len(y)-len(x)
		x_temp = ''
		for i in range(0,padding):
			x_temp += '0'
		x_temp += x
		x = x_temp
	elif len(y)<len(x):
		padding = len(x)-len(y)
		y_temp = ''
		for i in range(0,padding):
			y_temp += '0'
		y_temp += y
		y = y_temp
	count = 0
	for i in range(0,len(x)):
		if (x[i]!=y[i]):
			count += 1
	print(count)

hamming_distance(25,30)
hamming_distance(1,4)
hamming_distance(100,250)
hamming_distance(100,250)
hamming_distance(1,30)
hamming_distance(0,255)