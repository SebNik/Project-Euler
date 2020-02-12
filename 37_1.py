import timeit

def find_primes(max=1000000):
    #we are collecting alle primes below the max valuie
    #we are creating a dictonary of echa number under the max
    #the dictonary will contain ture and flase for primes
    dic_prime={}
    for i in range(2,max):
        dic_prime[i]=True
    #created a dictonary with all numbers
    #staring to sieve the primes out
    for x in range(2,max):
        #because lowest known prime
        if (dic_prime[x]):
            for j in range(x*2, max+1, x):
                dic_prime[j]=False
    return dic_prime

def get_all_cases(num):
    cases=[]
    for i in range(0,len(num)):
        cases.append(num[i:])
        if (i!=0):
            cases.append(num[:i])
    return cases

def v37_1(numbers_to_find=11):
    result=[]
    range_sieve=1000000
    start_end_nums=[3,7]
    numbers=[1,2,3,4,5,6,7,8,9,0]
    digits=2
    test=''
    while len(result)<3:
        for i in range(0,digits):
            primes=find_primes(str(9)*digits)
            if (i==0 or i==digits-1):
                for x in start_end_nums:
                    result.append()
                    if (len(x)==digits):
                        None
            else:
                None

            

#print(find_primes[123])
#print(get_all_cases('3797')) #works --> ['3797', '797', '3', '97', '37', '7', '379']