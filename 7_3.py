import timeit
import math

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
    #print('These are all thr prime numbers I find: ', p, len(p))
    print('Thats is your prime number: ', p[number-1])
v7()
#v7(int(input('Your Prime Number: ')))
#print(timeit.timeit(v7,number=10)/10)
#0.293919233 & 0.29697671960000005 &0.3030767778
