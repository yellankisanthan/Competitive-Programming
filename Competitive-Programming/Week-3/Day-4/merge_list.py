import unittest
def merge_lists(lis, liss):
    m = len(lis)
    n = len(liss)
    i = j = 0
    merged_list = []
    while i < m and j < n:
        if lis[i] < liss[j]:
            merged_list.append(lis[i])
            i += 1
        else:
            merged_list.append(liss[j])
            j += 1
    while i < m:
        merged_list.append(lis[i])
        i += 1
    while j < n:
        merged_list.append(liss[j])
        j += 1
    return merged_list