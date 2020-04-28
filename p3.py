#3 
list_num=[]
l=[]
n=int(input('enter the length of the list'))
print(n)
print(f"enter the list of length {n}")
for a in range (n):
    k=int(input(f"enter the {a} number of the list"))
    list_num.append(k)
print(list_num)
for s in list_num:
    if s<5:
        l.append(s)
print(f"the numbers less than 5 in the list are {l}")
