def change_possibilities(amount, denominations):

    res = [0]*(amount+1)
    res[0] = 1
    for coin in denominations:
        for i in range(coin,amount+1): 
            res[i] += res[i-coin]
    return res[amount]

# Tests

actual = change_possibilities(4, (1, 2, 3))
expected = 4
print(actual == expected)

actual = change_possibilities(0, (1, 2))
expected = 1
print(actual == expected)

actual = change_possibilities(1, ())
expected = 0
print(actual == expected)

actual = change_possibilities(5, (25, 50))
expected = 0
print(actual == expected)

actual = change_possibilities(50, (5, 10))
expected = 6
print(actual == expected)

actual = change_possibilities(100, (1, 5, 10, 25, 50))
expected = 292
print(actual == expected)