import timeit

def v15():
    possibilities=[] #Gibt die Summe der Möglichkeiten an
    #zero == right
    #one == down
    #Die Maxiamale Zahl kann sein 11111(*20)000000(*20) --> Im deziaml 1099510579200
    for x in range(1048574,1099510579201):
        number_binary=bin(x)[2:].zfill(40)
        number_binary_string=str(number_binary)
        zeros=number_binary_string.count('0')
        ones=number_binary_string.count('1')
        #print(number_binary_string, zeros, ones)
        if zeros==20 and ones==20:
            possibilities.append(number_binary_string)
    print(len(possibilities))

print(timeit.timeit(v15,number=5)/5)            