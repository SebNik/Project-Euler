import timeit

def abundant_numbers(max_number=28123):
    abundant_nmber=[]
    for i in range(0,max_number):
        dividors=[]
        dividor=1
        while dividor<=(i/2)+1:
            test=i%dividor
            if test==0:
                dividors.append(dividor)
            dividor+=1
        sum_dividors=sum(dividors)
        if sum_dividors>i:
            abundant_nmber.append(i)
    #print(abundant_nmber)
    return abundant_nmber


def v23(max=281123):
    abudants=abundant_numbers(max)
    all_numbers=[]
    for j in range(1,max+1):
        all_numbers.append(j)
    #print(all_numbers)
    y=0
    x=0
    while y!=len(abudants):
        A=abudants[x]
        B=abudants[y]
        C=A+B
        x+=1
        if C in all_numbers:
            all_numbers.remove(C)
        if x==len(abudants):
            x=0
            y+=1
        #print(x,y,len(abudants))
    print(sum(all_numbers))

v23()