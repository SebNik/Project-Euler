import math

def next_prime(p=[2], test=3):
    divider=2
    prime=True
    a=0
    while math.sqrt(test)>divider or math.sqrt(test)==divider:
        if test%divider!=0:
            if a+1>len(p)-1:
                break
            else:
                a+=1
                divider=p[a]
        else:
            prime = False
            break
    if prime:
        p.append(test)
    return p, prime


p =[2, 3, 5, 7]
truncatable_primes = []
counter = 10


while len(truncatable_primes)<= 10:

    p, added = next_prime(p, counter)
    if added:
        digits = list(str(p[-1]))
        if digits[0] in ['2','3','5','7'] and digits[-1] in ['2','3','5','7']:
            a = 1
            t = True
            while a<len(digits)-1:
                if int(''.join(digits[a:])) not in p or int(''.join(digits[:-1*a])) not in p:
                    t = False
                    break
                
                a+=1
            #print(p[-1])
            if t:
                truncatable_primes.append(p[-1])
           
    counter += 1

print(truncatable_primes)
    
print(sum(truncatable_primes))
