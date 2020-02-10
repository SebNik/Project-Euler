import timeit

def ssq(n=100):
    answer = 0
    for i in range(101):
        answer += pow(i,2)
    return answer
def sqs(m):
    answer = 0
    for j in range(101):
        answer += j
    return pow(answer,2)
print (sqs(100) - ssq(100))
print(timeit.timeit(ssq,number=10)/10)
#7.136640000000028e-05sec
