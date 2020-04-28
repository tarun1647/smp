#12
def list_1(*args):
    a=list(args)
    b=[]
    b.append(a[0])
    b.append(a[-1])
    print(f"given list is {a} the new list is {b}")
list_1(1,2,3,4,5,6,7)
