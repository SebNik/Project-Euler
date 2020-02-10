import timeit
def v7(number=10001):
    print('We will find the ', number, 'prime number')
    p=[2]
    a=2
    y=2
    while len(p)<=number:
        #print(p)
        if(a%y==0):
            a+=1
            y=2
        if y==(a-1):
            p.append(a)
            a+=1
            y=2
        else:
            y+=1
    print('These are all thr prime numbers I find: ', p, len(p))
    print('Thats is your prime number: ', p[number-1])

#v7(int(input('Your Prime Number: ')))
print(timeit.timeit(v7,number=10)/10)
#122.99257920509999sec
