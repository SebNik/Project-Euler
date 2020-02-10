import timeit
import math

def find_dividers(number):
    divider=1
    dividers_sum=0
    while divider<number/2+1:
        if number%divider==0:
            dividers_sum+=divider
            #print(number,divider)
        divider+=1
    #dividers_sum+=1
        #print(divider,number)
    return dividers_sum,number

def v21(max_number=10000):
    amicable_numbers=[]
    for i in range(1,max_number):
        x=find_dividers(i)
        y=find_dividers(x[0])
        if x[0]==y[1] and x[1]==y[0] and x[0]!=x[1]:
            amicable_numbers.append(x[1])
            #amicable_numbers.append(x[0])
    amicable_numbers_sum=sum(amicable_numbers)
    print(amicable_numbers_sum,amicable_numbers)
    return amicable_numbers_sum

v21()