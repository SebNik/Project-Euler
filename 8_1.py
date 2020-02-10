import os
import timeit

def v8(text='8.txt', numbers=13):
    f=open(text)
    t=f.readlines()
    print('Datei erfolgreich ausgelesen')
    f.close()
    l=[]
    for x in t:
        l+=x
#-------------------------------------------------------------------------------
    l.remove('\n')
    l = list(map(int, l))
    l_laenge=len(l)
    a=0
    b=0
    soloution=[1]
    zwischen_speicher=[]
#-------------------------------------------------------------------------------
    while b<l_laenge:
        z=1
        a=b
        for x in range(0,numbers):
            z*=l[a]
            zwischen_speicher.append(l[a])
            a+=1
            if a==l_laenge:
                break
        print(z, zwischen_speicher)
        if z>soloution[0]:
            soloution[0]=z
            soloution_numbers=[]
            soloution_numbers=zwischen_speicher
        b+=1
        zwischen_speicher=[]

#-------------------------------------------------------------------------------
    print('Höchste Zahl', soloution[0])
    print(soloution_numbers)

#t_datei=input('Textdatei: ')
#t_datei='8.txt'
#numbers=int(input('Numbers: '))
#v8(t_datei,numbers)
print(timeit.timeit(v8,number=10)/10)
#0.0796048481
