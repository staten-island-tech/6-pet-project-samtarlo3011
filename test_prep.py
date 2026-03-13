def spaces(t, y, n):
    both=[]
    yest=list(y)
    now=list(n)
    a=0
    for i in range(t):
        if yest[a] == "c" and now[a] == "c":
            both.append(1)
        a=a+1
    x=sum(both)
    print(x)

def E_F():
    text=list(input("enter text here "))
    ss=0
    ts=0
    a=0
    for letters in text:
        if text[a]=="s" or text[a] == "S":
            ss+=1
        elif text[a]=="t" or text[a]== "T":
            ts+=1
        a+=1
    if ss>ts:
        print ("prolly french")
    elif ts>ss:
        print("prolly english")
    else:
        print("prolly french")

def honi():
    text=input("enter text ")
    honi=["H","h","O","o","N","n","I","i"]
    first=0
    second=1
    c=0
    for i in text:
        if i == honi[a] or i == honi[b]:
            a+=2
            b+=2
            c+=0.25
        if c.is_integer():
            a=0
            b=1
    print(int(c))

def internet(Mb, N, months: list[int]):
    a=0
    avail=[Mb]
    for i in range(N):
        NextM = avail[a] - months[a]
        NextM+=Mb
        avail.append (NextM)
        a+=1
    return (NextM)

def poor_ppl(q,m1,m2,m3):
    PC=0
    while q>0:
        m1+=1
        q-=1
        PC+=1
        if m1 == 35:
            q+=30
            m1=0
        if q == 0:
            return(PC)
        m2+=1
        q-=1
        PC+=1
        if m2 == 100:
            q+=60
            m2=0
        if q == 0:
            return(PC)
        m3+=1
        q-=1
        PC+=1
        if m3 == 10:
            q+=9
            m3=0
        if q == 0:
            return(PC)

def Village(N):
    y = []
    for i in range(N):
        x= int(input("loc of next vill"))
        y.append(x)
        villages = sorted(y)
    z=1
    villageN = []
    for i in villages[:-1]:
        villageN.append ((villages[z]-i)/2)
        z+=1
    final =[]
    z=1
    for i in villageN[:-1]:
        final.append(villageN[z]+i)
        z+=1
        print (final)
        real=sorted(final)
    return real[0]
print(Village(5))
