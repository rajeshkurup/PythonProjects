#!/usr/bin/python

def get_number():
	while True:
		user_input = raw_input("Please enter the length of the side of the triangle: ")
		
		if not user_input.isdigit():
			print "ATTN: Please enter a number!"
		else:
			break
			
	return int(user_input)

def print_triangle(height):
	print "Here is your triangle"
	
	for i in range(height, 0, -1):
		print "*" * i

def do_platinum():
	print "Hi Platinum"
	
	number = get_number()
		
	print_triangle(number)
	
do_platinum()
