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
spaces(7,"ccc..cc","c....cc")