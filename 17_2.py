import timeit

def v17():
    numbers0_19=['','one','two','three','four','five','six','seven','eight','nine','ten','eleven','twelve',
    'thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen']
    numbers10_90=['','','twenty','thirty','forty', 'fifty','sixty','seventy','eighty','ninety']
    hundred='hundred'
    and_word='and'
    one_thousand='one thousand'
    sum_all=''
    # numbers0_19 = [0,3,3,5,4,4,3,5,5,4,3,6,6,8,8,7,7,9,8,8]
    # numbers10_90 = [0,3,6,6,5,5,5,7,6,6]
    # hundred = 7
    # one_thousand = 8+3
    # and_word=3
    # sum_all=0
    for i in range(1,1000):
        single=int(i%10)
        tenths=int((i%100-single)/10)
        hundreds=int((i-single-tenths*10)/100)
        #print(i,hundreds,tenths,single)
        if hundreds!=0:
            sum_all+=numbers0_19[hundreds]+hundred
            if single!=0 or tenths!=0:
                sum_all+=and_word
        if tenths==0 or tenths==1:
            sum_all+=numbers0_19[single+tenths*10]
        else:
            sum_all+=numbers10_90[tenths]+numbers0_19[single]

    sum_all+=one_thousand
    sum_all=sum_all.replace(" ", "")
    print(len(sum_all))
    #print(sum_all)


#v17()
print(timeit.timeit(v17,number=10)/10)
#0.0010369461000000004