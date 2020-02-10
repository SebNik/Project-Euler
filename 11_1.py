import sys
import os

global matrix
matrix=[]
global number
number=4

def read(datei='11_1.txt'):
    try:
        d=open(datei)
        datei_inhalt=d.readlines()
        d.close()
        return datei_inhalt
    except:
        print('Fehler beim öffnen der Datei:', datei)
        sys.exit(0)

def formatierung(datei_inhalt):
    b=[]
    c=0
    for i in range(0,len(datei_inhalt)):
        a=datei_inhalt[i]
        a=a.strip('\n')
        a=a.replace(' ', '')
        c=len(str(a))
        z=2
        b=[]
        for j in range(0,c,2):
            b.append(a[j:z])
            z+=2
        matrix.append(b)
    print(matrix)
    print(matrix[0][2])
    return matrix

def grid_size(matrix):
    global x_size
    global y_size
    x_size=len(matrix[0])
    y_size=len(matrix)

def waagrecht(number,x_size,y_size):
    max=0
    x=0
    y=0
    x_start=0
    while y!=y_size-1 and x!=x_size-1:
        product=[1]
        x_start=x
        for i in range(0,number):
            product[0]*=int(matrix[y][x])
            product.append(matrix[y][x])
            x=x+1
            if x==x_size:
                y+=1
                x=0
                x_start=-1
        if product[0]>max:
            max_number=product
            max=max_number[0]
        x=x_start+1
    return max_number

def senkrecht(number,x_size,y_size):
    max=0
    x=0
    y=0
    y_start=0
    while y!=y_size-1 and x!=x_size-1:
        product=[1]
        y_start=y
        for i in range(0,number):
            product[0]*=int(matrix[y][x])
            product.append(matrix[y][x])
            y=y+1
            if y==y_size:
                x+=1
                y=0
                y_start=-1
        if product[0]>max:
            max_number=product
            max=max_number[0]
        y=y_start+1
    return max_number

def diagonal_rechts(number,x_size,y_size):
    moegliche_reihen=[]
    max=0
    x=0
    for i in range(0,x_size-1):
        if x+number<=x_size:
            moegliche_reihen.append(x)
        x+=1
    for j in range(0,len(moegliche_reihen)):
        x_start=moegliche_reihen[j]
        anzahl_rechnungen=0
        test=x_size
        test=test-x_start
        while test>=0:
            if test-4>=0:
                anzahl_rechnungen+=1
            test-=1
        for a in range(0,anzahl_rechnungen):
            x=x_start+a
            y=0+a
            product=[1]
            for b in range(0,number):
                product[0]*=int(matrix[y][x])
                product.append(matrix[y][x])
                y+=1
                x+=1
                if product[0]>max:
                    max_number=product
                    max=max_number[0]
    return max_number

def diagonal_links(number,x_size,y_size):
    moegliche_reihen=[]
    max=0
    x=x_size-1
    for i in range(0,x_size-1):
        if x+number>=x_size:
            moegliche_reihen.append(x)
        x-=1
    for j in range(0,len(moegliche_reihen)):
        x_start=moegliche_reihen[j]
        anzahl_rechnungen=0
        #test=x_size
        test=x_start+1
        while test>=0:
            if test-4>=0:
                anzahl_rechnungen+=1
            test-=1
        #print(anzahl_rechnungen)
        for a in range(0,anzahl_rechnungen):
            x=x_start-a
            y=0+a
            product=[1]
            for b in range(0,number):
                product[0]*=int(matrix[y][x])
                product.append(matrix[y][x])
                #print(product,x,y)
                y+=1
                x-=1
                if product[0]>max:
                    max_number=product
                    max=max_number[0]
    return max_number
def v11():
    datei_inhalt=read()
    formatierung(datei_inhalt)
    print('Das Grid liegt zur Verfügung, nun wir gerechnet.')
    grid_size(matrix)
    print('Grid Groeße (x,y): ',x_size,y_size)
    max_waagrecht=waagrecht(number,x_size,y_size)
    print('Maximum Waagrecht:',max_waagrecht)
    max_senkrecht=senkrecht(number,x_size,y_size)
    print('Maximum Senkrecht:',max_senkrecht)
    diagonal_rechts_max=diagonal_rechts(number,x_size,y_size)
    print('Maximum Diagonal Rechts:', diagonal_rechts_max)
    diagonal_links_max=diagonal_links(number,x_size,y_size)
    print('Maximum Diagonal Links:',diagonal_links_max)
    #print(max(diagonal_links[0],diagonal_rechts[0],max_senkrecht[0],max_waagrecht[0])
v11()
