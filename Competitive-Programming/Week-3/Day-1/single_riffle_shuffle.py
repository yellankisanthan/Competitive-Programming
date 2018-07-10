def is_single_riffle(half1, half2, shuffled_deck):
    len_half1 = len(half1)
    len_half2 = len(half2)
    len_full = len(shuffled_deck)
    half1_i = 0
    half2_i = 0

    if len_half1 + len_half2 != len_full:
        return False

    for i in shuffled_deck:
        if half1_i<len_half1 and i==half1[half1_i]:
            half1_i += 1
        elif half2_i<len_half2 and i==half2[half2_i]:
            half2_i += 1
        elif i!=half1[half1_i] or i!=half2[half2_i]:
            return False 
    return True

# Tests

result = is_single_riffle([1, 4, 5], [2, 3, 6], [1, 2, 3, 4, 5, 6])
expected = True
print(result == expected)

result = is_single_riffle([1, 5], [2, 3, 6], [1, 2, 6, 3, 5])
expected = False
print(result == expected)

result = is_single_riffle([], [2, 3, 6], [2, 3, 6])
expected = True
print(result == expected)

result = is_single_riffle([1, 5], [2, 3, 6], [1, 6, 3, 5])
expected = False
print(result == expected)

result = is_single_riffle([1, 5], [2, 3, 6], [1, 2, 3, 5, 6, 8])
expected = False
print(result == expected)