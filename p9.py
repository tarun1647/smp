#9
import random
while True:
    n=int(input("guess a number between 1-9 "))
    a=int(random.randint(1,9))
    print(f"Random integer is {a}")
    if n<a:
        print("too low")
    elif (n==a):
        print("its a correct gess")
    else:
        print("too high")
    p=input("if u want to continue give 'yes' as input else give 'exit' as input \n")
    if p=="yes":
        continue
    else:
        break
