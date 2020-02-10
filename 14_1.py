import timeit

def Collatz_sequence(start_number):
    n=start_number
    sequence=[n]
    while n!=1:
        if n%2==0:
            n=n/2
            sequence.append(n)
        else:
            n=3*n+1
            sequence.append(n)
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

print(timeit.timeit(v14,number=10)/10)
#28.524535890499997sec