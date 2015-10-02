#!/usr/bin/python

from sys import argv

script, filename = argv

txt = open(filename)

print "Here's your file %r: " % filename
content = txt.read()
txt.close()
print content

print "Type the filename again:"
file_again = raw_input("> ")

txt_again = open(file_again)
content_again = txt_again.read()
txt_again.close()
print content_again
