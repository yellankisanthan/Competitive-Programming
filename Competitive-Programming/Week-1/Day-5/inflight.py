def can_two_movies_fill_flight(movie_lengths, flight_length):
    dic = {}
    for ml in movie_lengths:
        diff = flight_length-ml
        if diff in dic: return True
        else: dic[ml] = True
    return False

# Tests

result = can_two_movies_fill_flight([2, 4], 1)
expected = False
print(result == expected)

result = can_two_movies_fill_flight([2, 4], 6)
expected = True
print(result == expected)

result = can_two_movies_fill_flight([3, 8], 6)
expected = False
print(result == expected)

result = can_two_movies_fill_flight([3, 8, 3], 6)
expected = True
print(result == expected)

result = can_two_movies_fill_flight([1, 2, 3, 4, 5, 6], 7)
expected = True
print(result == expected)

result = can_two_movies_fill_flight([6], 6)
expected = False
print(result == expected)

result = can_two_movies_fill_flight([], 2)
expected = False
print(result == expected)