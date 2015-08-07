#!/usr/bin/env python
# HW04_ex00

# Create a program that does the following:
#     - creates a random integer from 1 - 25
#     - asks the user to guess what the number is
#     - validates input is a number
#     - tells the user if they guess correctly
#         - if not: tells them too high/low
#     - only lets the user guess five times
#         - then ends the program
################################################################################
# Imports
from random import randint

# Body
answer = randint(1,25)       #create a random integer from 1 - 25
attempt = 1                  #start with first guess
def guessing(attempt):       #function to allocate guesses and evaluate answers
	user_guess = raw_input('Guess an integer from 1-25 (inclusive). You have five tries.\n') #ask the user to guess the number
	try:
		int_user_guess = int(user_guess) 		#convert their guess to an integer
	except:
		print ('Needs to be an integer.')		#if it can't be converted, scold them
		guessing(attempt)						#and try again
	if int_user_guess == answer:
		print ("That's correct!")				#when user guesses the correct number, applaud them
	elif (int_user_guess < 1):					#scold them if it's not in range, try again
		print ('Your guess is out of range - it is smaller than 1.')
		guessing(attempt)
	elif (int_user_guess > 25):					#scold them if it's not in range, try again
		print ('Your guess is out of range - it is bigger than 25.')
		guessing(attempt)
	else:
		if int_user_guess > answer:				
			print ("That answer is too high. Try something lower.") #give a hint
			attempt += 1
			if attempt < 6:
				guessing(attempt)	#try again
			else:					
				print ('Sorry, you are out of guesses.') #end the chances and send them away
		else: 
			print ("That answer is too low. Try something higher.") #give a hint
			attempt += 1
			if attempt < 6:
				guessing(attempt) #try again
			else:
				print ('Sorry, you are out of guesses.') #end the chances and send them away

################################################################################
def main():
	
    guessing(1) 

if __name__ == '__main__':
    main()