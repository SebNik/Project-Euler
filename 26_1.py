import timeit

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

def v26():
    max=[0,0]
    for x in range(2,997):
        zahl=dividieren_periode(1,x)
        if zahl[2]==True:
            if int(max[0])<int(zahl[0]):
                max[0]=zahl[0]
                max[1]=zahl[1]
    print(max)

v26()