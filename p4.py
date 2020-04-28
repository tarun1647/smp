#4
n=int(input("enter a number"))
l=[]
for a in range(1,n+1):
    if n%a==0:
        l.append(a)
print(f"the divisors of {n} are {l}")
