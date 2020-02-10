import timeit

def v29(max=101):
    list_products=[]
    for a in range(2,max):
            for b in range(2,max):
                    c=a**b
                    if c not in list_products:
                            list_products.append(c)
    return len(list_products)

#print(v29())
print(timeit.timeit(v29, number=10)/10)
#0.6384788267