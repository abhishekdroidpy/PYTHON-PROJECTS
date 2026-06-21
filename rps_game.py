import random

choices=['r','p','s']

maps={'r':'rock',
           's':'scissor',
           'p':'paper',
           'q':'quit'}
           
wins={'r':'s',
            'p':'r',
            's':'p'}
            
attempts=1
points=0
     
def game_rps():
	while True:
		global attempts
		global points
		
		user=input("rock,paper or scissors(r/p/s)!: ")
		comp=random.choice(choices)
		attempts+=1
	
		if user=='q':
			print('thanks for playing!')
			print(points)
			break
			
		if user not in choices:
			print('invalid choice')
			break
			
		if wins[user]==comp:
			print("you: ",maps[user],", computer: ",maps[comp])
			print("you won!")
			points+=1
			
		elif user==comp:
			print("tie")
			print("you: ",maps[user]," ,computer: ",maps[comp])
			
		else:
			print("you: ",user," ,computer: ",comp)
			print("you lost!")
			
		if attempts>3:
			print('your attempts are over!')
			print("points: ",points)
			break
			
			
game_rps()
		