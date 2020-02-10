import timeit
import math

def prime(max_num):
    p=[2]
    test=3
    divider=2
    a=0
    while p[len(p)-1]<=max_num:
        while math.sqrt(test)>divider or math.sqrt(test)==divider:
            if test%divider!=0:
                if a+1>len(p)-1:
                    break
                else:
                    a+=1
                    divider=p[a]
            else:
                a=0
                divider=p[a]
                test+=1
            #print(p,test,divider,a)
        p.append(test)
        test+=1
        a=0
        divider=p[a]
    return p

def rechener(a,b,n):
    return n**2+(a*n)+b

def v27(max_all=1000):
    prime_liste_a_b=prime(max_all)
    prime_liste_a_b=prime_liste_a_b[:-1]
    #print(prime_liste_a_b)
    a=0
    b=len(prime_liste_a_b)-1
    max_numbers=[0,0,0] # n (anzahl Primes) a b
    prime_max_liste=prime(751000)
    while True:
        n=max_all
        for i in range(0,max_all):
            n=i
            zahl=rechener(int(str('-')+str(prime_liste_a_b[a])),prime_liste_a_b[b],n)
            if zahl in prime_max_liste:
                if n>max_numbers[0]:
                    max_numbers[0]=n
                    max_numbers[1]=a
                    max_numbers[2]=b
            if zahl not in prime_max_liste:
                break
        if b==0:
            a+=1
            b=len(prime_liste_a_b)-1
        if a==len(prime_liste_a_b)-1:
            #return max_numbers
            break
        b-=1
    #print(max_numbers)
    print('n**2+','(',(str('-')+str(prime_liste_a_b[max_numbers[1]])),'*n)+',prime_liste_a_b[max_numbers[2]])

print(timeit.timeit(v27, number=10)/10)
#36.3759552051