#addressBook.py
#Version 0
#Author: Stuart Topp stutopp@gmail.com
#Copyright 2016

def main():
	print("Welcome to the jbourne address book writer.")

	book = open('addressBook.txt', 'r+') #this program 1) assumes you already created a file named addressBook.txt and 2) are appending data to the file.

	newEntry = input("Would you like to add another entry to your address book? ")
	while str(newEntry) == "yes":
			entry = getInfo()
			newEntry = input("Would you like to add another entry to your address book? Please enter 'yes' or 'no'. )
	else:
		print("Thank you for using the jbourne addres book writer. Goodbye.")
	
def getInfo():
	first = input("Please enter the first name of your contact: ")
	last = input("Please enter the last name of your contact: ")
	home = input("Please enter the home phone number of your contact. Enter 'none' if there is no home number. ")
	cell = input("Please enter the cell phone number of your contact. Enter 'none' if there is no cell number. ")
	work = input("Please enter the work phone number of your contact. Enter 'none' if there is no work number. ")
	email = input("Please enter the e-mail address of your contact. Enter 'none' if there is no e-mail address. ")
n	street = input("Please enter the number and street name for your contact. Enter 'none' if there is no address. ")
	city = input("Please enter the city of your contact. Enter 'none' if there is address. ")
	state = input("Please enter the state of your contact. Enter 'none' if there is address. ")
	zipcode = input("Please enter the zip code of your contact. Enter 'none' if there is address. ")
	book.
	

if __name__ == "__main__": main()

