#!/usr/bin/env python
# HW04_ex07_04

# The built-in function eval takes a string and evaluates it using the Python
# interpreter.
# For example:
    
#     >>> eval('1 + 2 * 3')
#     7
#     >>> import math
#     >>> eval('math.sqrt(5)')
#     2.2360679774997898
#     >>> eval('type(math.pi)')
#     <type 'float'>

# Write a function called eval_loop that iteratively prompts the user, takes the
# resulting input and evaluates it using eval, and prints the result.

# It should continue until the user enters 'done', and then return the value of
# the last expression it evaluated.

################################################################################
# Imports

import math

# Body

# eval_loop iteratively prompts the user, takes the
# resulting input and evaluates it, and prints the result.

def eval_loop():
	value = 'None'
	while True:
		line = raw_input('> ')
		if line == 'done':
			return value
		else:
			try:
				value = eval(line)
				print value
			except:
				print ('Needs to be something Python can evaluate.')
				

################################################################################
def main():
    
	eval_loop()


if __name__ == '__main__':
    main()