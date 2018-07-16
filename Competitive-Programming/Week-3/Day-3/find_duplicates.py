import unittest
def find_duplicate(lis):
    n = len(lis)
    i,j = n,n
    while True:
        i = lis[i-1]
        j = lis[j-1]
        j = lis[j-1]
        if i == j:  break
    j = n
    while True:
        i = lis[i-1]
        j = lis[j-1]
        if i == j:  break
    return i