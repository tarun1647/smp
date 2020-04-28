#18 cows and bulls
def cows_and_bulls():
    import math
    print("Welcome to the Cows and Bulls Game! ")
    import random
    n=random.randint(1000,9999)
    o=n
    while True:
        n=o
        while True:    
            a=int(input("guess a 4-digit number "))
            if a>999 and a<=9999:
                break
            else:
                print("guess a four digit number")
                continue
        w=0
        for q in range(4):
            if n%10==a%10:
                w+=1
            n=math.floor(n/10)
            a=math.floor(a/10)
        print(f"{w} cows, {4-w} bulls")
        if w==4:
            return (f"your guess is correct the number is {o} \n")
        else :
            print("try again by using the clue")
            continue
    
        
cows_and_bulls()
