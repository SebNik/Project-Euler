#Das Programm findet die ersten 100 Prim-zahlen und gibt die dann in einem Diagram aus

import timeit
import matplotlib.pyplot as pl
def v7(number=100):
    print('We will find the ', number, 'prime number')
    p=[2]
    a=2
    y=2
    while len(p)<=number:
        #print(p,a,y)
        if y==a-1:
            p.append(a)
            a+=1
            y=2
        if a%y==0:
            a+=1
            y=2
        else:
            y+=1
    #print('These are all thr prime numbers I find: ', p, 'Thasts are:', len(p))
    #print('Thats is your prime number: ', p[number-1])
    l=[]
    for u in range(1,len(p)+1):
        l.append(u)
    #pl.plot(l, p, 'r-')
    pl.plot(l, p, 'm.')
    pl.show()
v7()
