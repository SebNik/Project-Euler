import timeit

def v30(digits=5):
    list_all=[]
    for x in range(2,6*(9**digits)):
        sum_numbers=0
        numbers=list(str(x))
        #print(x,numbers)
        for i in range(0,len(numbers)):
            a=int(numbers[i])**digits
            sum_numbers+=a
        #print(x,sum_numbers)
        if sum_numbers==x:
            list_all.append(x)
    print(list_all, sum(list_all))

#v30()
print(timeit.timeit(v30, number=10)/10)
#2.4309830351