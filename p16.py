#16 password
def password():
    m=0
    l=0
    k=0
    import re
    y=''
    while True:
        a=input("enter the password \n")
        n=len(a)
        if n<=9:
            print("you need at least 9 letters in the password")
            continue
            print("\n")
        elif a.find(' ')!=-1 :
            print("no spaces are allowed in the password")
            continue
            print("\n")
        for q in a:
            if q<="Z" and q>="A":
                m=m+1
        if m==0:
            print(("you need atleast one captial letter in your password"))
            continue
            print("\n")
        for w in a:
            if w<="z" and w>="a":
                l=l+1
        if l==0:
            print(("you need atleast one small letter in your password"))
            continue
            print("\n")        
        for e in a:
            if  ((chr(32)<=e and e<=chr(47)) or (chr(58)<=e and e<=chr(64)) or (chr(91)<=e and e<=chr(96)) or (chr(123)<=e and e<=chr(126))):
                k=k+1
        if k==0:
            print(("you need atleast one special character in your password"))
            continue
            print("\n")
        j=re.findall(r'[0-9]+',a)
        if len(j)==0:
            print ("\nyour password is hard but not strong")
            print ("do you want to change??\nif yes give 'yes' as input else give'no' \n")
            y=input()
            if y=="yes":
                continue
                print("\n")
            else:
                return "your password is set"
        else:
            return "your password is set and it is strong"
password()            
