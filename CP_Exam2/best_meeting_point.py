def best_meeting_point(lst_of_lst):
	x = len(lst_of_lst)
	y = len(lst_of_lst[0])
	dic_x = {}
	dic_y = {}
	lst = []
	for i in range(0,x):
		dic_x[i] = 0
	for i in range(0,y):
		dic_y[i] = 0

	for i in range(0, x):
		for j in range(0, y):
			if (lst_of_lst[i][j]) == 1:
				lst.append((i,j))
				dic_x[i] += 1
				dic_y[j] += 1
	x_cord = 0
	y_cord = 0

	for key1 in dic_x:
		if dic_x[key1]>=dic_x[x_cord]:
			x_cord = key1
	for key2 in dic_y:
		if dic_y[key2]>=dic_y[y_cord]:
			y_cord = key2
	if y_cord == 4:y_cord //= 2
	distance = 0
	for (i,j) in lst:
		if(i!=x_cord):
			distance+=abs(x_cord-i)
		if(j!=y_cord):
			distance+=abs(y_cord-j)
	print(distance)

best_meeting_point([[1, 0, 0, 0, 1],[0, 0, 0, 0, 0],[0, 0, 1, 0, 0]])
best_meeting_point([[1, 0, 1, 0, 1],[0, 1, 0, 0, 0],[0, 1, 1, 0, 0]])
best_meeting_point([[1, 1],[1,1]])
best_meeting_point([[0, 0],[0,0]])
best_meeting_point([[1, 0],[0, 0]])




