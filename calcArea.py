#calcArea.py
#Version 0
#Author: Stuart Topp stutopp@gmail.com
#Copyright 2016

import math

def main():
	print("Welcome to the jbourne area calculator!")
	choice=input("Please type a shape from the following list in order to calcualte its area: square, rectangle, parallelogram, trapezoid, circle, ellipse, triangle. ")
	area=areaCalc(choice)
	try:
		int(area)
		print("The area of your " + choice + " is " + str(area) + ".")
	except Value	Error:
		print("You did not select a valid shape. Please try again later.")
	"""try:
		if area == "wrong":
			print("You did not select a valid shape. Please try again.")
	except SyntaxError:
		print("The area of your " + choice + " is " + str(area) + ".")"""

def areaCalc(shape):	
	if shape == "square":
		side1 = input("Please enter the length of the side of the square: ")
		tester = verifyNum(side1)
		while (tester == -1):
			side1=input("Please enter a valid number as the length of the side of the square: ")
			tester = verifyNum(side1)
		result = int(side1)**2

	elif shape == "rectangle":
		side1 = input("Please enter the length of the first side of the rectangle: ")
		tester = verifyNum(side1)
		while (tester == -1):
			side1=input("Please enter a valid number as the length of the first side of the rectangle: ")
			tester = verifyNum(side1)

		side2 = input("Please enter the length of the second side of the rectangle: ")
		tester = verifyNum(side2)
		while (tester == -1):
			side2=input("Please enter a valid number as the length of the second side of the rectangle: ")
			tester = verifyNum(side2)

		result = int(side1) * int(side2)

	elif shape == "parallelogram":
		side1 = input("Please enter the length of the base of the parallelogram: ")
		tester = verifyNum(side1)
		while (tester == -1):
			side1=input("Please enter a valid number as the length of the base of the parallelogram: ")
			tester = verifyNum(side1)

		side2 = input("Please enter the length of the height of the parallelogram: ")
		tester = verifyNum(side2)
		while (tester == -1):
			side2=input("Please enter a valid number as the height of the parallelogram: ")
			tester = verifyNum(side2)

		result = int(side1) * int(side2)

	elif shape == "trapezoid":
		side1 = input("Please enter the length of the base of the parallelogram: ")
		tester = verifyNum(side1)
		while (tester == -1):
			side1=input("Please enter a valid number as the length of the base of the parallelogram: ")
			tester = verifyNum(side1)

		side3 = input("Please enter the length of the top of the parallelogram: ")
		tester = verifyNum(side3)
		while (tester == -1):
			side3=input("Please enter a valid number as the top of of the parallelogram: ")
			tester = verifyNum(side3)

		side2 = input("Please enter the height of the parallelogram: ")
		tester = verifyNum(side2)
		while (tester == -1):
			side2=input("Please enter a valid number as the height of of the parallelogram: ")
			tester = verifyNum(side2)

		result = (int(side2)/2)*(int(side1)*int(side3))

	elif shape == "circle":
		side1=input("Please enter the radius of the circle: ")
		tester = verifyNum(side1)
		while (tester == -1):
			side1=input("Please enter a valid number as the radius of the circle: ")
			tester = verifyNum(side1)

		result = math.pi * (int(side1) ** 2)

	elif shape == "ellipse":
		side1=input("Please enter the first radius of the ellipse: ")
		tester = verifyNum(side1)
		while (tester == -1):
			side1=input("Please enter a valid number as the first radius of the ellipse: ")
			tester = verifyNum(side1)

		side2=input("Please enter the second radius of the ellipse: ")
		tester = verifyNum(side2)
		while (tester == -1):
			side2=input("Please enter a valid number as the second radius of the ellipse: ")
			tester = verifyNum(side2)

		result = math.pi * int(side1) * int(side2)

	elif shape == "triangle":
		side1=input("Please enter the height of the triangle: ")
		tester = verifyNum(side1)
		while (tester == -1):
			side1=input("Please enter a valid number as the height of the triangle: ")
			tester = verifyNum(side1)

		side2=input("Please enter the sbase of the triangle: ")
		tester = verifyNum(side2)
		while (tester == -1):
			side2=input("Please enter a valid number as the base of the triangle: ")
			tester = verifyNum(side2)

		result = .5 * int(side1) * int(side2)
	else:
		result = "wrong"
	return result 

def verifyNum(dingbat):
	try:
		if int(dingbat) > 0:
			pass
	except ValueError:
		dingbat = -1
	return int(dingbat)


if __name__ == "__main__": main()

