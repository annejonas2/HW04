#!/usr/bin/env python
# HW04_ex08_11

# The following functions are all intended to check whether a string contains 
# any lowercase letters, but at least some of them are wrong. For each function, 
# describe what the function actually does (assuming that the parameter is a
# string).

# Do not merely paste the output as a counterexample into the documentation 
# string, explain what is wrong.

################################################################################
# Body


def any_lowercase1(s):
    """This function only looks at the first character in s.[[why??]]"""
    for c in s:
        if c.islower():
            return True
        else:
            return False

def any_lowercase2(s):
    """The string of 'c' is different than the character c - the former is 
    by definition lowercase, making the function always return True."""
    
    for c in s:
        if 'c'.islower():
            return 'True'
        else:
            return 'False'

def any_lowercase3(s):
    """Returns the answer only for the last letter in the string, 
    instead of any letter.
    """
    for c in s:
        flag = c.islower()
    return flag

def any_lowercase4(s):
    """nothing??
    """
    flag = False
    for c in s:
        flag = flag or c.islower()
    return flag

def any_lowercase5(s):
    """only works if all lowercase, because if it hits an uppercase it returns False
    """
    for c in s:
        if not c.islower():
            return False
    return True

################################################################################
def main():

    # Remove print("Hello World!") and for each function above that is wrong, 
    # call that function with a string for which the function returns
    # incorrectly.
    # ex.: any_lowercase_("thisstringmessesupthefunction")

    print any_lowercase1('StRING')
    print any_lowercase2('STRING')
    print any_lowercase3('ccE')
    print any_lowercase4('cannot figure this one out')
    print any_lowercase5('stArs')

if __name__ == '__main__':
    main()