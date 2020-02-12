import timeit

def v33_1():
    from fractions import Fraction
    #numerator/denominator
    fractions=1
    for a in range(10,100):
        for b in range(a+1,100):
            common_elements=list(set(str(a))&set(str(b)))
            if (len(common_elements)!=0):
                #print(a,b,common_elements)
                if (int(common_elements[0])!=0):
                    num=list(str(a))
                    den=list(str(b))
                    num.remove(common_elements[0])
                    den.remove(common_elements[0])
                    if (int(num[0])!=0 and int(den[0])!=0):
                        #print(a,b,num,den)
                        if (Fraction(a,b)==Fraction(int(num[0]),int(den[0]))):
                            fractions*=Fraction(int(num[0]),int(den[0]))
                            #print(Fraction(int(num[0]),int(den[0])),a,b)
    return fractions.denominator

#print(v33_1())
print(timeit.timeit(v33_1, number=10)/10)
#0.011208695200002694sec