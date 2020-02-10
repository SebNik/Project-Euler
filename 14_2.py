import timeit
import math

def Collatz_sequence(start_number):
    n=start_number
    sequence=[n]
    while n!=1:
        if n%2==0:
            n=n/2
            sequence.append(int(n))
        else:
            n=3*n+1
            sequence.append(int(n))
        if math.log(n,2)%2==0:
            #print('Abkürzung über logaritmus')
            #print(sequence)
            for i in range(0,int(math.log(n,2))):
                sequence.append(1)
            n=1
            #print(sequence)
        if n==40:
            #print('Abkützung über 40')
            for i in range(0,8):
                sequence.append(1)
            n=1
    #print(sequence)
    return sequence

def v14(max_number=1000000):
    max=[0]
    for x in range(1,max_number):
        sequence_check=Collatz_sequence(x)
        sequence_check_len=len(sequence_check)
        if sequence_check_len>max[0]:
            max=[0]
            max[0]=sequence_check_len
            max.append(sequence_check)
    print('Max Start number:', max[1][0], 'Sequenze is ', max[0], 'digets long' )
#v14()
print(timeit.timeit(v14,number=10)/10)
#90.915714355