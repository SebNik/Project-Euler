import timeit

def check(a,b,c):
    sum_abc=str(a)+str(b)+str(c)
    status=[]
    for i in numbers:
        if str(i) in sum_abc and sum_abc.count(str(i))==1 and sum_abc.count(str(0))==0:
            status.append(True)
        else:
            status.append(False)
    if False in status:
        return False
    else:
        return True

def v32():
    global numbers
    numbers=[1,2,3,4,5,6,7,8,9]
    # a=1
    # b=25
    # c=346789
    # print(check(a,b,c))
    a=1
    b=1
    list_products=[]
    while True:
        c=a*b
        if len(str(a)+str(b)+str(c))==9:
            ergebnis=[]
            ergebnis=check(a,b,c)
            if ergebnis==True:
                if c not in list_products:
                    list_products.append(c)
                    #print(a,b,c)
        a+=1
        if len(str(a))>2:
            a=1
            b+=1
        if len(str(b))>4:
            break
    print(list_products,sum(list_products))

v32()
print(timeit.timeit(v32,number=10)/10)
#2.1463065091