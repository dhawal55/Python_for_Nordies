def fizzBuzz():
	''' prints 'fizz' if valueToCheck is evenly divisible by 3
	'buzz' if evenly divisible by 5, 'fizzbuzz' if both.
	'''

	for valueToCheck in xrange(1,100):
		retVal = ''   #start with empty string
		if valueToCheck % 3 == 0:
			retVal += 'fizz'
		if valueToCheck % 5 == 0:
			retVal += 'buzz'

		if retVal:  # retVal not empty string
			print(retVal)
		else:
			print(valueToCheck)


fizzBuzz()
