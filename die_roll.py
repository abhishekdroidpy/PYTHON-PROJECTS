import random
num=(1,2,3,4,5,6)
while True:
	decision=input("Do you wanna roll the die(y/n): ").lower()
	if decision=="y":
		print((random.choice(num),random.choice(num)))
	elif decision=="n":
		print("ok fine!")
		break
	else:
		print("can't you see that (y/n)?")
	