def keys_Rooms(lis):
	dic = {}
	for i in range(0, len(lis)):
		if i==0:
			dic[i] = True
		else:
			dic[i] = False
	ll = 0
	for l in lis:
		if not dic[ll]:
			return False
		for i in range(0,len(l)):
			if not dic[i]:
				return False
			dic[l[i]] = True
		ll += 1
	return True






if(keys_Rooms([[1],[0,2],[3]])):
	print("Passed")
else:
	print("Failed")

if(keys_Rooms([[1,3], [3,0,1], [2], [0]])):
	print("Failed")
else:
	print("Passed")

if(keys_Rooms([[1,2,3], [0], [0], [0]])):
	print("Passed")
else:
	print("Failed")

if(keys_Rooms([[1], [0,2,4], [1,3,4], [2], [1,2]])):
	print("Passed")
else:
	print("Failed")

if(keys_Rooms([[1],[2,3],[1,2],[4],[1],[5]])):
	print("Failed")
else:
	print("Passed")

if(keys_Rooms([[1], [2], [3], [4], [2]])):
	print("Passed")
else:
	print("Failed")

if(keys_Rooms([[1], [1,3], [2], [2,4,6], [], [1,2,3], [1]])):
	print("Failed")
else:
	print("Passed")