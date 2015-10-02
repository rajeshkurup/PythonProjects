#!/usr/bin/python

def get_number():
	while True:
		user_input = raw_input("Please enter a number: ")
		
		if not user_input.isdigit():
			print "ATTN: Please enter a number!"
		else:
			break
			
	return int(user_input)

def print_number(number):
	if number % 3 == 0 and number % 5 == 0:
		print "FizzBuzz"
	elif number % 3 == 0:
		print "Fizz"
	elif number % 5 == 0:
		print "Buzz"
	else:
		print number
	
def do_silver():
	print "Hi Silver"

	number = get_number()
	
	print_number(number)
	
do_silver()
