# solving problem 39 too late in the evening
def v39(m=1000):
    pre_record = 0
    pre_record_p = 0
    for i in range(m):
        solution = find_solutions(i)
        if solution > pre_record:
            pre_record = solution
            pre_record_p = i
    print(pre_record, pre_record_p)


def find_solutions(p=120):
    s = []
    for c in range( int(0.5*p), int(0.333*p), -1):
        c_s = c*c
        for a in range( c-1, int(0.5*(p-c)), -1):
            b = p-a-c
            if (a*a+b*b)==c_s:
                s.append([a,b,c])
            
    return len(s)

v39()