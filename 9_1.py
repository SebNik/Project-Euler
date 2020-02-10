import timeit
import math
import sys
def v9(number=1000):
    a=1
    b=1
    status=0
    sum=0
    while sum != number:
        if b>number:
            print('Fehler')
            sys.exit(0)
            break
        if a==number:
            b+=1
            a=1
        else:
            a+=1
        c_test=a**2
        c_test+=b**2
        c_sollte=math.sqrt(c_test)
        sum=c_sollte+a+b
        #print('a:',a,'b:',b,'C_Sollte: ', c_sollte,' C_Test: ',c_test, ' Sum: ', sum)
        #if c_sollte-int(c_sollte)==0:
            #print('a:',a,'b:',b,'C_Sollte: ', c_sollte,' C_Test: ',c_test, ' Sum: ', sum)
            #print('Status: ---Erfüllt---')

    return number,a,b,c_sollte,c_test,sum
#print('Reihenfolge: Ziel a b C_Sollte C_Test summe')
#print(v9())
print(timeit.timeit(v9,number=10)/10)
#0,1879sec
