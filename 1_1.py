import timeit
import time

def v1(max=1000):
    print('We will check which Numbers are multiples of 3 5')
    print('Then we will sum them up')
    numbers=[]
    numbers_sum=0
    for x in range(0,max):
        a=x%3
        b=x%5
        if a==0:
            numbers.append(x)
            numbers_sum+=x
        elif b==0:
            numbers.append(x)
            numbers_sum+=x
    #print('These are all of the numbers:')
    #print(numbers)
    print('This is the sum:', numbers_sum)
# start=time.time()
# v1(1000)
# end=time.time()
# z=end-start
# print(z)
# 0.0009965896606445312
print(timeit.timeit(v1,number=10)/10)
#0.0007442967000000002sec