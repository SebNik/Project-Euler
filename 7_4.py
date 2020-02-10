import timeit
import time
def sieve(limit=22):
  
  bools = []
  primes = []
  
  # generate a list of booleans all set to True initially
  # the list is indexed from 2 to limit representing all numbers
  # e.g. [True, True, True, True] = [2, 3, 4, 5]
  for i in range(1, limit):
    bools.append(True)
  print(bools)
  # loop from 2 to limit setting the composite numbers to False
  # we start from 2 because we know 1 is not a prime number
  for i in range(2, limit):
    if bools[i-2]:
      print(i)
      for j in range(i*2, limit+1, i):
        bools[j-2] = False
        #print(j-2)
        #print(str(i*2)+str(' ')+str(limit+1)+str(' ')+str(i))
        #print(bools)
        #time.sleep(2)
  print(bools)
  # now generate the list of primes only where
  # there is a True value in the bools list
  for p in range(0, len(bools)):
    if (bools[p]):
      primes.append(p+2)
      
  print(primes)

sieve()
print(timeit.timeit(sieve,number=10)/10)   
#0,1 sec
