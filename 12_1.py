import timeit

def v12(dividors=500):
    st_number=3 #immer minus eins
    numbers=[]
    count=0
    number=0
    a=1
    while dividors>count:
        count=0
        while a<st_number:
            number+=a
            a+=1
        numbers.append(number)
        n=number
        st_number+=1
        x=1
        while x<n:
            if n%x==0:
                count+=1
            x+=1
        #print(number,count)
    print(numbers)

v12()
