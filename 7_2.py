import timeit
def v7(number=100):
    #print('We will find the ', number, 'prime number')
    p=[2]
    test=2
    divider=2
    a=0
    while len(p)<=number:
        #print(p,test,divider,a)
        if a==len(p)-1:
            p.append(test)
            test+=1
            a=0
        if test%divider==0:
            test+=1
            a=0
            divider=p[a]
        else:
            a+=1
            divider=p[a]
    print('These are all thr prime numbers I find: ', p, len(p))
    print('Thats is your prime number: ', p[number])
v7()
#v7(int(input('Your Prime Number: ')))
#print(timeit.timeit(v7,number=10)/10)
#14.292961420999998sec & 13.9795271803sec & 14.903442289000001
#ohne Ausgabe 13.6211125646
