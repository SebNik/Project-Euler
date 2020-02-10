import timeit

def v24(number=1000000):
    a=0
    b=0
    c=0
    d=0
    e=0
    f=0
    g=0
    h=0
    i=0
    j=0
    k=0
    numbers=['0','1','2','3','4','5','6','7','8','9']
    variations=[]
    while True:
        x=numbers[k]+numbers[j]+numbers[i]+numbers[h]+numbers[g]+numbers[f]+numbers[e]+numbers[d]+numbers[c]+numbers[b]+numbers[a]
        for u in range(0,len(x)-1):
            count=x.count(str(u))
            count_zero=x.count('0')
            #print(x,u,count)
            if count>=2:
                None
            if count<2:
                if count_zero<0:
                    variations.append(x)
                    print(variations)
        if a==len(numbers)-1:
            a=0
            b+=1
        if b==len(numbers)-1:
            b=0
            c+=1
        if c==len(numbers)-1:
            c=0
            d+=1
        if d==len(numbers)-1:
            d=0
            e+=1
        if e==len(numbers)-1:
            e=0
            f+=1
        if f==len(numbers)-1:
            f=0
            g+=1
        if g==len(numbers)-1:
            g=0
            h+=1
        if h==len(numbers)-1:
            h=0
            i+=1
        if i==len(numbers)-1:
            i=0
            j+=1
        if j==len(numbers)-1:
            j=0
            k+=1
        if k==len(numbers)-1:
            break
        #print(a)
        a+=1
    
    variation=variations.sort()
    print(variations[number-1])

v24()