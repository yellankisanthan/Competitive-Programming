def queue_reconstruction(people):
	new_people = sorted(people,key=lambda x:x[0],reverse=True)
	re_people = []
	for person in new_people:
		re_people.insert(person[1],person)
	return re_people

print(queue_reconstruction([[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]))
print(queue_reconstruction([[12,0],[6,3],[3,4],[9,2], [11,1],[1,5]]))
print(queue_reconstruction([[2,4], [5,1], [3,3], [1,5], [4,2], [6,0]]))