import timeit

def v24(number=1000000):
    variations=[]
    x=1000000000
    while True: 
        y=str(x)
        status=True
        for i in range(0,9):
            c=y.count(str(i))
            #print(y,i,c)
            if c>1:
                status=False
        if status==True:
            variations.append(y)
            #print(y)
        x+=1
        if len(variations)>number:
            break
    variation=variations.sort()
    print(variations[number-1])

v24()