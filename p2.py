#2
num=int(input("enter the number"))
if num%2==0:
    print("the number is even")
    if num%4==0:
        print("it is also a multiple of 4")
else:
    print("the num is odd")
