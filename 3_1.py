import timeit
def v3(n=600851475143):
    print('We will find the prime factors of ', n)
    max_suche=1000000
    x=1
    factors=[]
    max_factor=0
    while x < max_suche:
        y=n%x
        if y==0:
            factors.append(x)
            n=n/x
        x+=1
    max_factor=max(factors)
    print('The prime factors are: ', factors)
    print('The highest factor is', max_factor)

#v3(int(input('Gib deine Zahl ein : ')))
print(timeit.timeit(v3,number=10)/10)
#0.12245624480000002sec
