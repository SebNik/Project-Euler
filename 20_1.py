import timeit
import math

def v20(x=100):
    number=str(math.factorial(x))
    quersumme=0
    for i in number:
        quersumme+=int(i)
    print(quersumme)
    return quersumme

#v20()
print(timeit.timeit(v20,number=10)/10)
#0.0004349451000000004sec