def get_permutations(string):
    list_of_words = []
    rec(string,"",list_of_words)
    return set(list_of_words)

def rec(st, f, list_of_words):
    if len(st)==0:
        list_of_words.append(f)
        return
    for k in range(len(st)):	rec(st[0:k]+st[k+1:],f+st[k],list_of_words)

# Tests

actual = get_permutations('')
expected = set([''])
print(actual == expected)

actual = get_permutations('a')
expected = set(['a'])
print(actual == expected)

actual = get_permutations('ab')
expected = set(['ab', 'ba'])
print(actual == expected)

actual = get_permutations('abc')
expected = set(['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
print(actual == expected)