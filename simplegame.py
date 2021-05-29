import random
def humanguess():
	randomnum = random.randint(1,10)
	userinput = 0
	while randomnum != userinput:
		userinput = int(input("Enter the number: "))
		if userinput > randomnum:
			print("too high")
		elif userinput < randomnum:
			print("too low")
		
	print(f"correct {randomnum}")


def computerguess():
	low = 1
	high = 100
	randoms = ''
	while randoms != 'c':
		randomnum = random.randint(low, high)
		print(f"number: {randomnum}")
		randoms = input("Enter the feedback: ")
		if randoms == 'l':
			low = randomnum + 1
		elif randoms == 'h':
			high = randomnum - 1
	print("Correct !!")

def rockpaper():
	userinput = ''
	listes = ['s','p','c']
	while userinput != 'quit':
		userinput = input("Enter your choice: ").lower()
		compinput = random.choice(listes)
		if userinput == compinput:
			print(f"{userinput}<-->{compinput}")
			print("tie!!")
		elif userinput =='s' and compinput == 'p' or userinput =='s' and compinput == 'c' or userinput =='p' and compinput == 's':
			print(f"{userinput}-->{compinput}")
			print("you win !")
		elif userinput =='s' and compinput == 'p' or userinput =='c' and compinput == 's' or userinput =='p' and compinput == 'c':
			print(f"{userinput}<--{compinput}")
			print("you lost !")
	print("thanks for playing")

game = ""

while game != "quit":
	game = int(input("Enter what game want to play:\n 1->guess computer number\n 2->computer guess your number\n 3->stonepaper\n 4->quit\n"))
	if game == 1:
		humanguess()
	elif game == 2:
		computerguess()
	elif game == 3:
		rockpaper()
	elif game == 4:
		game = "quit"