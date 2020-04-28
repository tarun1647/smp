#13
def Fibonnaci_series(n):
    fib=[]
    a=1
    fib.append(a)
    fib.append(a)
    if n==1:
        print(a)
    elif n==2:
        print(fib )
        
        
    else:
        
        for x in range(2,n):
            fib.append(fib[x-1]+fib[x-2])
        return fib
Fibonnaci_series(10)        
