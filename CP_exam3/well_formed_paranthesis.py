def print_parens(left, right, s, n):
		if right == n:
			lis.append(s)
			
		if right < left:
			print_parens(left, right + 1, s + ")", n)

		if left < n:
			print_parens(left + 1, right, s + "(", n)

def well_formed_paranthesis(n):
	global lis
	lis = []
	print_parens(0, 0, "" , n)
	print(lis)
	print(len(lis))

lis = [] 
well_formed_paranthesis(2)
well_formed_paranthesis(3)
well_formed_paranthesis(5)
well_formed_paranthesis(4)
well_formed_paranthesis(1)
well_formed_paranthesis(6)
