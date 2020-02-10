import os
import timeit

def read_file(text='13_Test_Text.txt'):
    f=open(text)
    t=f.readlines()
    print('Datei erfolgreich ausgelesen')
    f.close()
    return t

def v13(number=10,text='13_Text.txt'):
    data_file=read_file(text)
    #print(data_file)
    sum_all=0
    for line in data_file:
        line=int(line[:-1])
        #print(line)
        sum_all+=line
    sum_all=str(sum_all)
    print(sum_all[:number])
#v13(10)
print(timeit.timeit(v13,number=10)/10)
#0.0008646017999999992sec