#!/usr/bin/python

def get_number():
	while True:
		user_input = raw_input("Please enter a number: ")
		
		if not user_input.isdigit():
			print "ATTN: Please enter a number!"
		else:
			break
			
	return int(user_input)
	
def print_numbers(number):
	print "Printing Numbers"
	
	limit = number + 1
	for i in range(1, limit):
		print i

def do_bronze():
	print "Hi Bronze"
	
	number = get_number()
	
	print_numbers(number)

do_bronze()
