# Created by: Aden Rao
# Created on: April 15, 2019
# This program lets the user enter two integers and it multiplies it using only addtion and loops.

# Variables and the inputs for each number
number1 = int(input("Enter the first factor: "))
number2 = int(input ("Enter the second factor: "))
addFunction = 0
answer = 0

# If statement and while loop to multiply the two numbers using only addition
if addFunction < number2:
	while True:
		answer = answer + number1
		addFunction = addFunction + 1
		if addFunction == number2:
			break
print ("The product is", answer)