#!/usr/bin/python

animals = ['bear', 'python', 'peacock', 'kangaroo', 'whale', 'platypus']
position = ['first', 'second', 'third', 'forth', 'fifth', 'sixth']

index = 0
for animal in animals:
	print "The %s animal is at %d and is a %s" % (position[index], index, animals[index])
	index += 1
