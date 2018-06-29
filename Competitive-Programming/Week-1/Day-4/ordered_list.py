def contains(lst, key):
    low = 0
    high = len(lst)-1
    if lst == []: return False  
    while low<=high:
        mid = low + ((high-low)/2)
        if key<lst[mid]: 
            high = mid-1
        elif key>lst[mid]: 
            low = mid+1
        else: return True
    return False

# Tests

result = contains([], 1)
expected = False
print(result == expected)

result = contains([1], 1)
expected = True
print(result == expected)

result = contains([1], 2)
expected = False
print(result == expected)

result = contains([2, 4, 6], 4)
expected = True
print(result == expected)

result = contains([2, 4, 6], 5)
expected = False
print(result == expected)

result = contains([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 8)
expected = True
print(result == expected)

result = contains([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 0)
expected = False
print(result == expected)

result = contains([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 1)
expected = True
print(result == expected)

result = contains([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10)
expected = True
print(result == expected)