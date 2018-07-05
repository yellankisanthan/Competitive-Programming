import unittest
def reverse_words(words):
    k = 0
    for l in range(0,len(words)):
        if words[l] == ' ':
            reverse(words, k, l-1)
            k = l+1  
    reverse(words, k, len(words)-1);
    reverse(words, 0, len(words)-1);

def reverse(words, k, l):
    while k<l:
        t = words[k]
        words[k] = words[l]
        words[l] = t
        k += 1
        l -= 1

# Tests

def test_one_word():
    message = list('vault')
    reverse_words(message)
    expected = list('vault')
    print(message == expected)

def test_two_words():
    message = list('thief cake')
    reverse_words(message)
    expected = list('cake thief')
    print(message == expected)

def test_three_words():
    message = list('one another get')
    reverse_words(message)
    expected = list('get another one')
    print(message == expected)

def test_multiple_words_same_length():
    message = list('rat the ate cat the')
    reverse_words(message)
    expected = list('the cat ate the rat')
    print(message == expected)

def test_multiple_words_different_lengths():
    message = list('yummy is cake bundt chocolate')
    reverse_words(message)
    expected = list('chocolate bundt cake is yummy')
    print(message == expected)

def test_empty_string():
    message = list('')
    reverse_words(message)
    expected = list('')
    print(message == expected)

test_one_word()
test_two_words()
test_three_words()
test_empty_string()
test_multiple_words_same_length()
test_multiple_words_different_lengths()