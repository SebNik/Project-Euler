import timeit
def v2(max=4000000):
    a=1
    b=2
    c=0
    f_sum=3
    f=[1,2]
    f_ev=[]
    f_ev_sum=2
    while c<max:
        c=a+b
        if c%2==0:
            f_ev.append(c)
            f_ev_sum+=c
        f_sum+=c
        f.append(c)
        a=b
        b=c
    f_sum-=c
    print('We find out Fibonacci Numbers:')
    print(f)
    print('The sum of the numbers is:',f_sum, 'Thats are: ', len(f))
    print(len(f_ev), ' Numbers are even valued')
    print('The sum of this numbers are:', f_ev_sum)

#v2()
print(timeit.timeit(v2,number=10)/10)
#0,0514sec
