def reverse(lst):
    i = 0   
    if len(lst) == 0 or len(lst) == 1:   return lst
    x = lst[0]
    for i in range(len(lst)//2):
        temp = lst[i]
        lst[i]=lst[-i-1]
        lst[-i-1]=temp
    return lst

# Tests

def test_empty_string():
    list_of_chars = []
    reverse(list_of_chars)
    expected = []
    print(list_of_chars == expected)

def test_single_character_string():
    list_of_chars = ['A']
    reverse(list_of_chars)
    expected = ['A']
    print(list_of_chars == expected)

def test_longer_string():
    list_of_chars = ['A', 'B', 'C', 'D', 'E']
    reverse(list_of_chars)
    expected = ['E', 'D', 'C', 'B', 'A']
    print(list_of_chars == expected)

test_empty_string()
test_single_character_string()
test_longer_string()