import timeit

def v19():
    calibration_date=[1, 1, 1900, 1]
    start_date=[1, 1 ,1901]
    end_date=[31 ,12, 2000]
    count=0
    # First the day;Then the Month;Year;Day
    # Months Shortcuts
    # Year if year%4==0 special year
    months_normal=[0,31,28,31,30,31,30,31,31,30,31,30,31]
    months_lap_year=[0,31,29,31,30,31,30,31,31,30,31,30,31]
    status=False
    month=1
    day=1
    year=1900
    day_name=1
    while status==False:
        if status==True:
            break
        if day_name==7 and day>=start_date[0] and month>=start_date[1] and year>=start_date[2] and day==1:
            count+=1
            #print('count')
        day+=1
        day_name+=1
        if day_name>7:
            day_name=1
        if year%4==0:
            single=int(year%10)
            tenths=int((year%100-single)/10)
            #hundreds=int((year-single-tenths*10)/100)
            if year%400==0 and tenths==0 and single==0:
                if day>months_lap_year[month]:
                    month+=1
                    day=1
            if tenths!=0 or single!=0:
                if day>months_lap_year[month]:
                        month+=1
                        day=1
            else:
                if day>months_normal[month]:
                    month+=1
                    day=1
        else:
            if day>months_normal[month]:
                month+=1
                day=1
        if month>12:
            month=1
            year+=1
            day=1
        if day>=end_date[0] and month>=end_date[1] and year>=end_date[2]:
            status=True
            #print('Stop counting')
        #print(day,day_name,month,year)
    print(count)
#v19()
print(timeit.timeit(v19,number=10)/10)
#0.0129954763