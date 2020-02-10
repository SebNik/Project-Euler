import timeit

def v25(searched_digits=1000):
    a=1
    b=1
    fibs=[1,1]
    while True:
        c=a+b
        fibs.append(c)
        #print(fibs)
        digits=len(str(c))
        if digits>=searched_digits:
            print(fibs.index(c)+1)
            break
        a=b
        b=c

print(timeit.timeit(v25, number=10)/10)
#0.0543439431