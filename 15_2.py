import timeit
import math

def v15(size=20):
    #possibilities #Gibt die Summe der Möglichkeiten an
    #zero == right
    #one == down
    a=math.factorial(size*2)
    b=math.factorial(size)*math.factorial(size)
    print(a/b)

print(timeit.timeit(v15,number=10)/10)
#7.93162e-05sec           