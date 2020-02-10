import timeit
import math

def abundant_numbers(max_number):
    abundant_nmber=[]
    for i in range(11,max_number):
        dividor=2
        dividors=[1]
        n=math.ceil(math.sqrt(i))
        while dividor<n:
            if i%dividor==0:
                dividors.append(dividor)
                dividors.append(i//dividor)
            dividor+=1
        if n**2==i:
            dividors.append(n)
        #print(i,dividors)
        sum_dividors=sum(dividors)
        if sum_dividors>i:
            abundant_nmber.append(i)
    #print(abundant_nmber)
    return abundant_nmber


def v23(max=28123):
    abudants=abundant_numbers(max)
    all_numbers=[]
    for j in range(1,max+1):
        all_numbers.append(j)
    variations=[]
    y=0
    x=0
    while y!=len(abudants):
        variations.append(abudants[x]+abudants[y])
        x+=1
        if x==len(abudants):
            x=0
            y+=1
    for w in variations:
        if w > max:
            continue
        if w in all_numbers:
            all_numbers.remove(w)
    #print(variations)
    print(sum(all_numbers))

v23()