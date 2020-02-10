import timeit
import math

def dividieren_periode(num1,num2):
    #print('Ich teile nun die Zahlen: ',num1,' durch ',num2)
    rest=None
    ergebniss=int(num1/num2)
    if ergebniss==0:
        komma_zahl='0.'
    else:
        komma_zahl=str(ergebniss)
        komma_zahl+='.'
        if num1%num2==0:
            komma_zahl+='0'
    liste_der_reste=[]
    rest=num1
    status=False
    while rest!=0:
        neueZahl=int(str(rest)+'0')
        if neueZahl in liste_der_reste:
            #print('Es wurde eine Periode gefunden die Zahl lautete: ', komma_zahl)
            status=True
            break
        komma_zahl+=str(int(neueZahl/num2))
        rest=neueZahl%num2
        liste_der_reste.append(neueZahl)
    #print(komma_zahl)
    return komma_zahl[2:],num2,status

def prime():
    #print('We will find the ', number, 'prime number')
    p=[2]
    test=3
    divider=2
    a=0
    while p[len(p)-1]<=1000:
        while math.sqrt(test)>divider or math.sqrt(test)==divider:
        #while test**0.5>divider or test**0.5==divider:
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

def v26():
    max=[0,0]
    liste_prime=prime()
    #print(liste_prime)
    for x in range(0,len(liste_prime)-1):
        zahl=dividieren_periode(1,liste_prime[x])
        if zahl[2]==True:
            if int(max[0])<int(zahl[0]):
                max[0]=zahl[0]
                max[1]=zahl[1]
    print(max[1])

print(timeit.timeit(v26,number=50)/50)
#0.17486101964000003