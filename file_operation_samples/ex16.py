#!/usr/bin/python

from sys import argv

script, filename = argv

print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

raw_input("? ")

print "Opening the file..."
target = open(filename, 'a+')

# file modes: 
# b - binary operation
# r or rb - read only
# w or wb - write only (will truncate the original file)
# a or ab - append only
# r+ or rb+ - read and write (file pointer points to the first character, may overwrite existing content)
# w+ or wb+ - write only (will truncate the original file)
# a+ or ab+ - read and append (file pointer points to new line at end of file)

print "Truncating the file. Goodbye!"
#target.truncate()

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print "And finally, we close it."
target.close()
