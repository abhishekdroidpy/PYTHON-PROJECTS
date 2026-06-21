import random

number=random.randint(1,100)
attempt=1
max_attempt=5

def game():
	global attempt
	while True:
		if attempt>max_attempt:
			print('your attempts are over!')
			break
			reply=input("wanna try again?(y/n: ").lower
			if reply=="y":
				game()
			elif reply=="n":
				print('Game ended!')
				break
			else:
				print("invalid entry!")
			
		try:
			guess=int(input("guess an integer between 1 and 100: "))
			attempt+=1
			if guess>number:
					print('too high!')
			elif guess<number:
					print('too low!')
			else:
				print('you got it!')
				break
		except ValueError:
			print("invalid entry!")

game()

		
			
