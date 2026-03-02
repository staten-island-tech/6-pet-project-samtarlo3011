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
    text=input("enter text here ")
    for i in text:
        print(i)
        if i != "H" and i != "h" and i != "O" and i != "o" and i != "N" and i != "n" and i != "I" and i != "i":
            i= "n/a"
    print (text)
honi()