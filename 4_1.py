import timeit

def v4():
    print('We will find a palindrome number')
    print('The number ia as product of two numbers with 3 digits')
    a=999
    b=999
    status=False
    c_int=0
    c_sting=''
    c_list=[]
    while status is False:
        c_int=a*b
        c_sting=str(c_int)
        c_reverse=int(c_sting[::-1])
        if c_reverse==c_int:
            c_list.append(c_int)
        if a==100:
            b-=1
            a=999
        if b==100:
            status=True
        a-=1
    #print('The numbers are:', c_list)
    #print('The higest number is:')
    print('The highest number is: ')
    print(max(c_list))
#v4()
print(timeit.timeit(v4,number=10)/10)
#0.46900991799999997sec