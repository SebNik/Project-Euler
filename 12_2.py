import timeit
import math

def find_dividors(number):
    x=1
    count=0
    while x<=int((math.ceil(number/2))):
        if number%x==0:
            count+=1
        x+=1
        if count>500:
            break
    count+=1
    return count

def triangular_numbers(number,triangular_number):
    tri_number=0
    tri_number=int(triangular_number[-1])
    a=len(triangular_number)
    while number>=a:
        a=a+1
        tri_number=a+tri_number
    triangular_number.append(tri_number)
    return triangular_number

def v12(dividors=500):
    t=[1,3,6,10,15]
    dividors_test=0
    st_number=5
    while dividors_test<=dividors:
        t=triangular_numbers(st_number,t)
        if t[-1]>500:
            dividors_test=find_dividors(t[-1])
            print(dividors_test, t[-1])
        st_number=st_number+1
    print('Triangular Number is:',t[-1],'It has :',dividors_test,'dividors.')

v12()