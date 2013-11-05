import sys

''' 
Given a range of integers:
	if integer is divisible by 3, prints 'Fizz'
	if integer is divisible by 5, prints 'Buzz'
	if integer is divisible by 3 and 5, prints 'FizzBuzz'
	else, prints the integer
'''

def fizzbuzz(range):
	for x in range:
		if x % 15 == 0:
			print("FizzBuzz")
		elif x % 5 == 0:
			print("Buzz")
		elif x % 3 == 0:
			print("Fizz")
		else:
			print(x)

fizzbuzz(range(1, 101))