import timeit

def palindromic_check(number):
    return str(number)[::-1]

def v36_1(max=1000000):
    sum=0
    for x in range(0,max):
        #print(x,palindromic_check(x))
        x_reverse=int(palindromic_check(x))
        if (x==x_reverse):
            #print(x,x_reverse)
            x_reverse_bin=palindromic_check(bin(x)[2:])
            #print(bin(x)[2:],x_reverse_bin)
            if (int(x_reverse_bin)==int(bin(x)[2:])):
                sum+=x
    return sum

print(v36_1())
print(timeit.timeit(v36_1,number=10)/10)
#0.4229375935000462sec