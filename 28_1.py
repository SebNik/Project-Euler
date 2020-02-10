import timeit

def v28(max_num=1001):
    sum_diagonales=[1]
    rows=[]
    for k in range(1,max_num+1,2):
        rows.append(k)
    #print(rows)
    for i in range(1,len(rows)):
        for j in range(0,4):
            if j==0:
                num=rows[i]-2
                verschoben=sum_diagonales[len(sum_diagonales)-1]+1
                num=verschoben+num
                #print('altes Element: ',sum_diagonales[len(sum_diagonales)-1],'neues Element: ',num)
            else:
                num=(rows[i]-1)+sum_diagonales[len(sum_diagonales)-1]
            sum_diagonales.append(num)
    #print(sum_diagonales,sum(sum_diagonales))
    print(sum(sum_diagonales))

#v28()
print(timeit.timeit(v28,number=10)/10)
#0.0009388312499999999