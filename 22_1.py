import timeit
import sys

def v22(datei='22_Text.txt'):
    try:
        d=open(datei)
        datei_inhalt=d.readlines()
        d.close()
    except:
        print('Fehler beim öffnen der Datei:', datei)
        sys.exit(0)
    inhalt=datei_inhalt[0]
    inhalt=inhalt.split(',')
    abc={'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,'H':8,'I':9,'J':10,'K':11,'L':12,'M':13,'N':14,'O':15,'P':16,'Q':17,'R':18,'S':19,'T':20,'U':21,'V':22,'W':23,'X':24,'Y':25,'Z':26}
    datei_liste=[]
    for i in range(0,len(inhalt)):
        x=inhalt[i]
        x=x[1:-1]
        datei_liste.append(x)
    datei_liste.sort()
    score=0
    name_socore=0
    for j in range(0,len(datei_liste)):
        name_socore=0
        t=0
        name_socore+=j+1
        for u in datei_liste[j]:
            t+=abc.get(u)
        #print(datei_liste[j],name_socore,t)
        name_socore=t*name_socore
        score+=name_socore
    print(score)

#v22()
print(timeit.timeit(v22,number=10)/10)
#0.0099880935sec