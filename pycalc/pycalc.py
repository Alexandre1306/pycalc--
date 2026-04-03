def add(a,b):
    res=a
    if b>0:
        while (b-1)>=0:
            b-=1
            res+=1
    elif b<0:
        while (b+1)<=0:
            b+=1
            res-=1
    return res
def subtract(a,b):
    res=a
    if b>0:
        while (b-1)>=0:
            b-=1
            res-=1
    elif b<0:
        while (b+1)<=0:
            b+=1
            res+=1
    return res
def multiply(a,b):
    res=0
    negative=False
    if b<0:
        b=-b
        negative=True
    while b>0:
        res=add(res,a)
        b-=1
    if negative:
        res=-res
    return res
def divide(a,b):
    if b==0:
        return "Division par zéro"
    res=0
    negative=(a<0)!=(b<0)
    a=abs(a)
    b=abs(b)
    while a>=b:
        a=subtract(a,b)
        res+=1
    if negative:
        res=-res
    return res
