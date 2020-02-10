import timeit

def v16(bais=2,potenz=1000):
    number=str(bais**potenz)
    quersumme=0
    for i in number:
        quersumme+=int(i)
    print(quersumme,number)

#v16()
print(timeit.timeit(v16,number=10)/10)
#0.0003240479999999997sec