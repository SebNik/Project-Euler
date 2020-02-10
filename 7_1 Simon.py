import timeit
def isprime(a):
    y = 3
    while a ** 0.5 > y:
        if a%2 == 0:
            #print("Die Zahl ist keine Primzahl" , a, 2)
            return a, 2
        if a%y == 0:
            #print("Die Zahl ist keine Primzahl" , a, y)
            return a, y
        else:
            y += 2
    #print(a, " ist eine Primzahl" ,a ,y)        
    return a, y


def f(y=2):
    howmanyifound = 4
    x = 10
    while howmanyifound < 10001:
        prime, y = isprime(x)
        #print("prime ist " , prime, " und y ist " ,y) 
        if prime % y != 0 or prime == y:
            howmanyifound += 1
            #print(prime, " ist eine Primzahl")
        #else:
            #print(prime, " ist keine")
        x += 1
    print(x-1)
    return x-1
print(timeit.timeit(f,number=10)/10)
