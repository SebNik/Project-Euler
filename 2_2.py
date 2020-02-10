import timeit

def fib(n):
    if n<2:
        return n
    else:
        return fib(n-1)+fib(n-2)

def v2_2(max=4000000):
    f_sum_ev=0
    f=[]
    f_ev=[]
    n=1
    a=0
    while a<max:
        a=fib(n)
        if a%2==0:
            f_ev.append(a)
            f_sum_ev+=a
            f.append(a)
            n+=1
        else:
            n+=1
            print(f_sum_ev)
            f.append(a)

print(timeit.timeit(v2_2,number=10)/10)
#5,95sec
