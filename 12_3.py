import timeit
import math

def find_dividors(number):
    count=0
    #while x<=int((math.ceil(number/2))):
    for i in range(1,int(math.ceil(math.sqrt(number)))):
        if number%i==0:
            count+=2
        else:
            continue
    #count+=2
    return count

def v12(dividors=500):
    dividors_test=0
    t=0
    a=1
    while dividors_test<=dividors:
       t+=a
       a+=1
       dividors_test=find_dividors(t)
       #print(t,dividors_test)
    print('Triangular Number is:',t,'It has :',dividors_test,'dividors.')

print(timeit.timeit(v12,number=10)/10)
#3.2716479219sec