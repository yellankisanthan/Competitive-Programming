import unittest

def countRotations(words,l,h):
    if h<l: return 0
    if h==l: return l
    mid = l+(h-l)/2; 
    mid = int(mid)
    if (mid<h and words[mid+1]<words[mid]): return (mid+1)
    if (mid>l and words[mid]<words[mid - 1]): return mid
    if (words[h]>words[mid]): return countRotations(words, l, mid-1);
    return countRotations(words, mid+1, h)

def find_rotation_point(words):
    return countRotations(words,0,len(words)-1)

# Tests

actual = find_rotation_point(['cape', 'cake'])
expected = 1
print(actual == expected)

actual = find_rotation_point(['grape', 'orange', 'plum', 'radish', 'apple'])
expected = 4
print(actual == expected)

actual = find_rotation_point(['ptolemaic', 'retrograde', 'supplant', 'undulate', 'xenoepist', 'asymptote', 'babka', 'banoffee', 'engender', 'karpatka', 'othellolagkage'])
expected = 5
print(actual == expected)