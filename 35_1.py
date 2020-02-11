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

def find_circular_permutations(number):
    circular_per=[number]
    for i in range(0,len(str(number))-1):
        number = (number%10)*10**(len(str(number))-1)+number//10
        #print(number)
        circular_per.append(number)
    return circular_per


#find all permutation not the circluar ones
# def find_permutations(num):
#     permutations=[0]
#     num_list=[]
#     for i in str(num):
#         num_list.append(i)
#     start=num
#     switched=[0]
#     adding='0'
#     while int(start)!=permutations[-1]:
#         if (len(str(start))==1):
#             l=[num]
#             return l
#         last=num_list[-1]
#         count=len(num_list)-1
#         while count!=0:
#             switched=num_list
#             switched.pop(count)
#             switched.insert(count-1,last)
#             count-=1
#             adding=''
#             for i in switched:
#                 adding+=i
#             permutations.append(int(adding))
#         #print(int(start),permutations[-1],permutations,switched,adding)
#         num_list=switched
        
#     permutations.remove(0)
#     per=[]
#     for r in permutations:
#         #print(r)
#         if (int(r) not in per):
#             per.append(r)
#     #print(per)
#     return per

def v35_1(max=1000000):
    dic=find_primes(max)
    curios_nums=[]
    for i in dic:
        #print(i)
        if (dic[i]):
            per=find_circular_permutations(i)
            count=0
            goal=len(per)-1
            for x in per:
                if (dic.get(x)):
                    if (x!=i):
                        count+=1
            if (goal==count):
                curios_nums.append(i)
                #print(curios_nums)
    return len(curios_nums)+1

#print(find_primes(1000)[197])
#print(find_circular_permutations(197))
#print(v35_1())-->55
print(timeit.timeit(v35_1,number=10)/10)
#0.8874000253000304sec