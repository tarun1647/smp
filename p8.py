#8 rock papper scissors
print("player1 select any one of rock,papper,scissors")
p1=input()
print("player select any one of rock,papper,scissors")
p2=input()
if (p1=='rock' and p2=='scissors') or (p1=='scissors' and p2=='papper') or (p1=='papper' and p2=='rock'):
    print('player1 won the game ')
elif p1==p2:
    print("it's a tie")
    
else:
    print('player2 won the game ')
    
