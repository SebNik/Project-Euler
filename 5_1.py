import timeit
#Der direkt Vergleich ergab v1=61,098sec und v2=40,021sec


# def v5_1():
#     #o=[19,16,7,8,9,11,13,17,20]
#     a=1
#     x=1
#     y=0
#     while x<20:
#         y = a % x
#         #print(x)
#         if y==0:
#             x+=1
#         else:
#             a+=1
#             x=1
#     print('This number is: ')
#     print(a)
#
# #v5()
# print(timeit.timeit(v5_1,number=10)/10)

def v5_2():
    o=[19,16,7,8,9,11,13,17,20]
    a=20
    x=0
    y=0
    while x<len(o):
        y = a % o[x]
        #print(x)
        if y==0:
            x+=1
        else:
            a+=1
            x=0
    print('This number is: ')
    print(a)

#v5()
print(timeit.timeit(v5_2,number=10)/10)