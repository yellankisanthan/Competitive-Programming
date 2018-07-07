def couple_holding_hands(row):
  dic = {}
  for i in range(0, len(row)):
    dic[row[i]] = i
  count = 0
  for i in range(1, len(row), 2): 
    while row[i]^1!= row[i-1]:
      j = dic[row[i]^1]^1
      row[i], row[j] = row[j], row[i]
      count = count+1
  return count

print(couple_holding_hands([1,3,4,0,2,5]))
print(couple_holding_hands([3,2,0,1]))
print(couple_holding_hands([1,0]))