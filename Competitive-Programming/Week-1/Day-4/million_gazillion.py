class Trie(object):

    # Implement a trie and use it to efficiently store strings
    def __init__(self,):
        self.Dict = {}

    def add_word(self, word):
        Dict = self.Dict
        for c in word:
            if c in Dict:
                Dict = Dict[c]
            else:
                Dict[c] = {}
                Dict = Dict[c]
        if '*' in Dict: return False
        Dict['*'] = {}
        return True

# Tests

trie = Trie()

result = trie.add_word('catch')
expected = True
print(expected == result)

result = trie.add_word('cakes')
expected = True
print(expected == result)

result = trie.add_word('cake')
expected = True
print(expected == result)

result = trie.add_word('cake')
expected = False
print(expected == result)

result = trie.add_word('caked')
expected = True
print(expected == result)

result = trie.add_word('catch')
expected = False
print(expected == result)

result = trie.add_word('')
expected = True
print(expected == result)

result = trie.add_word('')
expected = False
print(expected == result)