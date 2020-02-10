# In unserem Beispiel ist die Lösung 3 + 7 + 4 + 9 = 23
import timeit
import sys

def read(datei='18_Text.txt'):
    try:
        d=open(datei)
        datei_inhalt=d.readlines()
        d.close()
        return datei_inhalt
    except:
        print('Fehler beim öffnen der Datei:', datei)
        sys.exit(0)

def format(datei_inhalt):
    triangle=[]
    for i in range(0,len(datei_inhalt)):
        row=datei_inhalt[i]
        row.strip()
        row_full=[]
        for j in range(0,len(row)):
            value=row[j:j+2]
            if value==' ':
                continue
            value=value.replace(' ','')
            value=value.strip()
            if len(value)>=2:
                row_full.append(value)
        row_full_int=[]
        for x in row_full:
            row_full_int.append(int(x))
        triangle.append(row_full_int)
    return triangle

def path(triangle,way):
    # In the Triangle we move from top to bottom
    # We always move down
    # We have to optins right or left
    # Right==1 && Left==0
    # Way first number always 1 or 0 anything
    way_string=str(way)     # To work
    path=[]                 # Shows every step in traingle
    sum_path=0              # Sum of Path
    position_x=0            # Shows Position x
    position_y=0            # Shows Position y
    #Abfrage ob Pfad möglch ist noch machen
    for i in range(0,len(triangle)):
        if i==0:
            sum_path+=triangle[i][i]
            path.append(triangle[i][i])
        else:
            if way_string[i]=='0':
                position_y+=1
                position_x=position_x
                if position_x<0:
                    position_x=0
                sum_path+=triangle[position_y][position_x]
                path.append(triangle[position_y][position_x])
            if way_string[i]=='1':
                position_y+=1
                position_x+=1
                if position_x>len(triangle[i]):
                    position_x=len(triangle[i])
                sum_path+=triangle[position_y][position_x]
                path.append(triangle[position_y][position_x])
    return sum_path,path

def brut_force(triangle):
    max=[0]
    path_len=len(triangle)-1
    path_max_bin='0b'+path_len*'1'
    path_max=eval(path_max_bin)
    #print('Maximum is: ', path_max)
    bin_number='1'
    for i in range(0,path_max+1):
        bin_number='1'
        x=str(bin(i))
        bin_number+=x[2:].zfill(path_len)
        bin_number=int(bin_number)
        check=path(triangle,bin_number)
        #print(check)
        if check[0]>max[0]:
            max=[]
            max=check
    return max

def v18():
    datei_inhalt=read()
    #print(datei_inhalt)
    triangle=format(datei_inhalt)
    #print(triangle)
    #Oriantion in Triangle triangle[row(y)][value(x)]
    best_path=brut_force(triangle)
    print('Best Way: ',best_path)
      

v18()
#print(timeit.timeit(v18,number=10)/10)
#0.4386891558sec