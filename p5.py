#5
l1=[]
l2=[]
j=[]
n1=int(input("enter the length of the list1 "))
n2=int(input("enter the length of the list2 "))
for l in range(n1):
    l1.append(int(input(f"enter the {l} number in the list1 ")))
print('\n')
for k in range(n2):
    l2.append(int(input(f"enter the {k} number in the list2 ")))
print(f"{l1} is the list1")
print(f"{l2} is the list2")
print("\n")
for q in l1:
    for w in l2:
        if w==q:
            j.append(q)
print(f"the common numbers in the lists {l1} and {l2} are \n {j} ")
            
