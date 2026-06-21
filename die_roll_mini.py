import random

num=int(input("enter no.of players: "))
players=[ ]
scores=[0]*num

for i in range(num):
    players.append(input(f"\nplayer{i+1} name: "))
    
while max(scores)<10:
        
        for j in range(num):
            
            choice=input(f"\n{players[j]}, do you wanna roll the die(y/n): \n").lower()
            
            if choice=="y":
                value=random.randint(1,6)
                
                if value!=1:
                    scores[j]+=value
                    print(f"{players[j]} got a {value}")
                    print(f"{players[j]} score:{scores[j]}")
                    
                else:
                    scores[j]=0
                    print(f"{players[j]} got a one, score set to 0!")
                                   
            elif choice=="n":
                  continue
            else:
                  print("invalid input!")

max_score=max(scores)
for k in range(num):
    if scores[k]==max_score:
        print(f"\n{players[k]} won the game!")
              
              
              
            
            


    
    
