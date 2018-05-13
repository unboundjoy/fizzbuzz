def fizz_buzz(start,end):

	for i in range(start, end + 1):
		if i % 15 ==0:
			print "FizzBuzz"
		elif i % 3 == 0:
			print "Fizz"
		elif i % 5 ==0:
			print "Buzz"
		else:
			print i 

fizz_buzz(1, 1000000)
