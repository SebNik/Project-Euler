import timeit
import math
import sys

def v10(max=2000000):
    print('We will find the sum of all primenumbers below:', max)
    sum=2
    p=[2]
    test=2
    divider=2
    a=0
    while test<=max:
        while math.sqrt(test)>=divider:
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
        p.append(test)
        sum+=test
        test+=1
        a=0
        divider=p[a]
    return sum

#print(v10())
print(timeit.timeit(v10,number=10)/10)
#13.053579569799998
