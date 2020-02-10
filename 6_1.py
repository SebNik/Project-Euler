import timeit
def v6(max_number=101):
    y=0
    z=0
    for x in range(0,max_number):
        y+=(x**2)
        z+=x
    z=z**2
    u=z-y
    #print('The sum of the squares is:', y)
    #print('The square of the numbers is:', z)
    print('The diffrence is:', u)

#v6()
print(timeit.timeit(v6,number=10)/10)
#0.0003887408999999998sec
