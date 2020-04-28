#20 
def num_list(*args):
    import math
    num=int(input("enter the number you want to search "))
    a=list(args)
    b=[]
    b.append(a.sort())
    n=len(b)
    while True:
        if(b[math.floor(n/2)]==num):
            return f"the number {num} is found in the list {a}"
        elif (b[math.floor(n/2)] >=num):
            b=b[math.floor(n/2):]
            n=math.floor(n/2)
            continue
        elif (b[math.floor(n/2)]<=num):
            b=b[0:math.floor(n/2)]
            n=math.floor(n/2)
            continue
        else:
            return (f"number {num} is not found in the list")
            
num_list(1,2,3,4,5,345,234,234,23423,4,6,7,89)            
