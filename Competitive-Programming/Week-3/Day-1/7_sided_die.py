import random

def rand5():
    return random.randint(1, 5)

def rand7():
    while True:
        r1 = 5 * (rand5() - 1)
        r2 = rand5()
        r = r1 + r2
        if r <= 21:	return r % 7 + 1

print ('Rolling 7-sided die...')
print (rand7())