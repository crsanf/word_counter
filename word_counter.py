#For Regex
import re

source = "file_to_parse.txt"
#destination = "result.txt"

"""
This script will count the number of words in a file.
A word is defined as any group of characters surrounded
by white space on either side or the starting word of a string
or ending word of a string with a new line character at the end.

Christopher Sanfilippo March 12 2019 @ 11:16 AM

"""

#regex = "\w+"
regex = "[a-zA-Z]+"
word_count = 0

with open(source) as f:
	for line in f:
		new_line = line.rstrip(" \n")
		words = new_line.split(" ")
		print(words)
		word_count += len(words)

print (word_count)







