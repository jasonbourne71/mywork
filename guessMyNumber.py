#guessMyNumber.py
#Version 0
#Author: Stuart Topp stutopp@gmail.com
#Copyright 2016

import random

def main():
	number = random.randint(1,10)

	guess = int(input("Pick a number between 1 and 10: "))

	while guess != number:
		if guess > 10 or guess < 0:
			guess = int(input("You need to pick a number between 1 and 10. Please enter an appropriate guess. "))
		elif guess != number:
				guess = int(input("Wrong! Guess again! Pick a number between 1 and 10: "))

	if guess == number:
		print "You guessed correclty!"




if __name__ == "__main__": main()

