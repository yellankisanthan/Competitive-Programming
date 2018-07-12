def unique_morse_code(lst):
	dic = {'a': ".-", 'b':"-...", 'c':"-.-.", 'd':"-..", 'e':".", 'f':"..-.", 'g':"--.", 'h':"....", 'i':"..", 'j':".---", 
			'k':"-.-", 'l':".-..", 'm':"--", 'n':"-.", 'o':"---", 'p':".--.", 'q':"--.-", 'r':".-.", 's':"...", 't':"-",
			'u':"..-", 'v':"...-", 'w':".--", 'x':"-..-", 'y':"-.--", 'z':"--.."}

	dic2 = {}

	for i in range(0, len(lst)):
		s = ''
		for j in lst[i]:
			s += dic[j]
		if s in dic2:
			dic2[s] += 1
		else:
			dic2[s] = 1
		
	print(len(dic2))
	

unique_morse_code(["gin", "zen", "gig", "msg"])
unique_morse_code(["a", "z", "g", "m"])
unique_morse_code(["bhi", "vsv", "sgh", "vbi"]  )
unique_morse_code(["a", "b", "c", "d"]  )
unique_morse_code(["hig", "sip", "pot"]  )
