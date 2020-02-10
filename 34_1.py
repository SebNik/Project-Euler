import timeit
import math

def v34_1():
    sum_of_all=0
    upper_limit=math.factorial(9)*7
    #because 9!8 -> is also a 7 digit number
    for x in range(3,upper_limit):
        sum_factorial=0
        for a in str(x):
            sum_factorial+=math.factorial(int(a))
        if (sum_factorial==x):
            sum_of_all+=x
    return sum_of_all 

#print(v34_1())--> Answer 40730
print(timeit.timeit(v34_1,number=10)/10)
#5.940520286599996sec