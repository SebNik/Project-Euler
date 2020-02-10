import timeit

def v31():
    ziel = 200
    coins = [1, 2, 5, 10, 20, 50, 100, 200]
    ways = [1] + [0]*ziel

    for coin in coins:
        for i in range(coin, ziel+1):
            ways[i] += ways[i-coin]

    print(ways[ziel])

#v31()
print(timeit.timeit(v31, number=10)/10)
#0.0002774789000000007