#!/usr/bin/python 

def fizzBuzz(range):

	for n in range:
		if (n == 0):
			print(n)
		elif (n % 3 == 0) and (n % 5 ==0):
			print("FizzBuzz")
		elif (n % 3 == 0):
			print("Fizz")
		elif (n % 5 == 0):
			print("Buzz")
		else:
			print(n) 

	

fizzBuzz(range(16))