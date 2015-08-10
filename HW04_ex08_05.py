#!/usr/bin/env python
# HW04_ex08_05

# The following program counts the number of times a letter appears in a string 


################################################################################
# Imports


# Body

def count(word, letter):
    index = 0
    result = 0
    while index < len(word):
    	if word[index] == letter: 
        	result = result + 1
        index = index + 1
    print result


################################################################################
def main():

    # Remove print("Hello World!") and add several functions calls to count()
    # below, passing various strings and letters

    count('apple', 'p')
    count('star', 'm')
    count('bob', 'b')

if __name__ == '__main__':
    main()