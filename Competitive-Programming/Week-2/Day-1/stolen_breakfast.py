def find_unique_delivery_id(ids):

	# Find the one unique ID in the list
	unique = 0
	for i in ids:
		unique ^= i
	return unique

# Tests

actual = find_unique_delivery_id([1])
expected = 1
print(actual == expected)

actual = find_unique_delivery_id([1, 2, 2])
expected = 1
print(actual == expected)

actual = find_unique_delivery_id([3, 3, 2, 2, 1])
expected = 1
print(actual == expected)

actual = find_unique_delivery_id([3, 2, 1, 2, 3])
expected = 1
print(actual == expected)

actual = find_unique_delivery_id([2, 5, 4, 8, 6, 3, 1, 4, 2, 3, 6, 5, 1])
expected = 8
print(actual == expected)