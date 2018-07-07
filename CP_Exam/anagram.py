def My_anagram(s,t):
	s = s.lower()
	t = t.lower()
	dic1 = {}
	dic2 = {}
	for i in range(0,len(s)):
		if s[i]!= " ":
			if s[i] not in dic1:
				dic1[s[i]] = 1
			else:
				dic1[s[i]] += 1

	for i in range(0,len(t)):
		if t[i]!= " ":		
			if t[i] not in dic2:
				dic2[t[i]] = 1
			else:
				dic2[t[i]] += 1

	if len(dic2)!= len(dic1):
		return False

	for key in dic1:
		if key in dic2:
			if dic1[key] != dic2[key]:
				return False
		else:
			return False

	return True

if(My_anagram("anagram", "nagaram")):
	print("Passed")
else:
	print("Failed")

if(My_anagram("Keep", "Peek")):
	print("Passed")
else:
	print("Failed")

if(My_anagram("Mother In Law", "Hitler Woman")):
	print("Passed")
else:
	print("Failed")

if(My_anagram("School Master", "The Classroom")):
	print("Passed")
else:
	print("Failed")

if(My_anagram("ASTRONOMERS", "NO MORE STARS")):
	print("Passed")
else:
	print("Failed")

if(My_anagram("Toss", "Shot")):
	print("Failed")
else:
	print("Passed")

if(My_anagram("joy", "enjoy")):
	print("Failed")
else:
	print("Passed")

if(My_anagram("Debit Card", "Bad Credit")):
	print("Passed")
else:
	print("Failed")

if(My_anagram("SiLeNt CAT", "LisTen AcT")):
	print("Passed")
else:
	print("Failed")

if(My_anagram("Dormitory", "Dirty Room")):
	print("Passed")
else:
	print("Failed")


