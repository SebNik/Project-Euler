#import timeit

def v17():
    numbers0_19=[' ','one','two','three','four','five','six','seven','eight','nine','ten','eleven','twelve',
    'thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen']
    numbers10_90=['zero','ten','twenty','thirty','forty', 'fifty','sixty','senventy','eighty','ninety']
    hundret='hundred'
    and_word='and'
    one_thousand='one thousand'
    tenths=1
    hundrets=0
    sum_1_20=''
    sum_20_100=''
    sum_all=''
    for i in range(1,1000):
        if i<20:
            #sum_1_20+=' '
            sum_1_20+=numbers0_19[i]
        if i<100 and i>=20:
            if i%10==0:
                tenths+=1
                #sum_20_100+=' '
                sum_20_100+=numbers10_90[tenths]
            if i%10!=0:
                #sum_20_100+=' '
                sum_20_100+=numbers10_90[tenths]
                #sum_20_100+='-'
                sum_20_100+=numbers0_19[i%10]
        if i>=100:
            if i%100==0:
                hundrets+=1
                sum_all+=sum_1_20+sum_20_100
                for j in range(0,99):
                    sum_all+=numbers0_19[hundrets]
                    #sum_all+=' '
                    sum_all+=hundret
                    #sum_all+=' '
                    sum_all+=and_word
                    #sum_all+=' '
    sum_all+=one_thousand
    #sum_all+=sum_1_20+sum_20_100
    sum_all=sum_all.replace(" ", "")
    sum_all=sum_all.replace("-", "")
    print(len(sum_all))
    #print(sum_all)
    #print(sum_1_20)
    #print(sum_20_100)
    #print(len(sum_1_20+sum_20_100))

v17()
