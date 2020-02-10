import timeit
from itertools import permutations as perm

def v24():
    print( ''.join(list(perm('0123456789',10))[999999]))
print(timeit.timeit(v24, number=10)/10)