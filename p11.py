#11
def prime(a):
    w=0
    if a==1:
        return "it is neither prime nor composite"
    elif a==2:
        return "it is a prime number"
    else:
        for n in range(2,a):
            if a%n==0:
                w=w+1
            if w==0:
                return "it is a prime number"
            else:
                return "it is not a prime"        
