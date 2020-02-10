import timeit
import math
import matplotlib.pyplot as pl

def v7(number=10001):
    #print('We will find the ', number, 'prime number')
    p=[2]
    test=3
    divider=2
    a=0
    while len(p)<=number:
        while math.sqrt(test)>divider or math.sqrt(test)==divider:
        #while test**0.5>divider or test**0.5==divider:
            if test%divider!=0:
                if a+1>len(p)-1:
                    break
                else:
                    a+=1
                    divider=p[a]
            else:
                a=0
                divider=p[a]
                test+=1
            #print(p,test,divider,a)
        p.append(test)
        test+=1
        a=0
        divider=p[a]
    print('Thats is your prime number: ', p[number-1])
    l=[]
    for u in range(1,len(p)+1):
        l.append(u)
    pl.grid(True)
    pl.plot(l, p, 'r-')
    line1= pl.gca().lines
    pl.setp(line1, linewidth=1)
    pl.plot(l, p, 'm.')
    pl.show()
    return p
v7()
