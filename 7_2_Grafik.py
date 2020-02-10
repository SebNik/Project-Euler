import timeit
import matplotlib.pyplot as pl
def v7(max=100000):
    #print('We will find the', max,'prime number')
    p=[2]
    test=2
    divider=2
    a=0
    while test<=max:
        #print(p,test,divider)
        if a==len(p)-1:
            p.append(test)
            test+=1
            a=0
            divider=p[a]
        if test%divider==0:
            test+=1
            a=0
            divider=p[a]
        else:
            a+=1
            divider=p[a]
    #print('These are all thr prime numbers I find: ', p, 'Thasts are:', len(p))
    #print('Thats is your prime number: ', p[number-1])
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
