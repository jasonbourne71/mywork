#sentenceGenerator.py
#Version 0 for Python 2.7.x
#Author: Stuart Topp stutopp@gmail.com
#Copyright 2016

"""
This script only works in Python 2.7.x because of Tkinter. 
Removing the pop-up box feature will allow the script to run in Python 3.X
"""

#import ctypes #stackoverflow.com/questions/2963263/how-can-i-create-a-simple-message-box-in-python
from Tkinter import *
from tkMessageBox import *
import random

def main():
	proceed=qBox("Welcome!","Would you like to generate a sentence?")
	
	if proceed == 'no':
		sys.exit("Thanks for playing! Goodbye!")

	subjlist = ["Bob", "Sally", "Jimmy", "Rover"]
	verblist = ["throws","catches"]
	objlist = ["the ball", "a football", "an iPad"]

	subj=word(subjlist)
	verbie=word(verblist)
	obj=word(objlist)
	print(subj, verbie, obj)
	print(subjlist[subj] + " " + verblist[verbie] + " " + objlist[obj] + ".")
def qBox(title,text):
	return askquestion(title,text)

def word(listo):
	ceiling=len(listo)-1
	return random.randint(0,ceiling)

if __name__ == "__main__": main()

