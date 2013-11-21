import sys

def FizzBuzz():
  if len(sys.argv) >= 2:
	val = int(sys.argv[1])
  else:
    val = 100

  for x in range(1, val + 1):
  	if x % 3 == 0 and x % 5 == 0:
  		print 'Fizz Buzz'  		
  	elif x % 3 == 0:
  		print 'Fizz'
  	elif x % 5 == 0:
  		print 'Buzz'
  	else:
  		print x

FizzBuzz()