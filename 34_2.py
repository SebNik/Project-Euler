import timeit
import math

def v34_2():
    sum_of_all=0
    list_nums=[]
    for z in range(0,10):
        list_nums.append(math.factorial(z))
    upper_limit=list_nums[9]*7
    #because 9!8 -> is also a 7 digit number
    for x in range(3,upper_limit):
        sum_factorial=0
        for a in str(x):
            sum_factorial+=list_nums[int(a)]
        if (sum_factorial==x):
            sum_of_all+=x
    return sum_of_all 

#print(v34_2()) #--> Answer 40730
print(timeit.timeit(v34_2,number=10)/10)
#5.0386900621sec