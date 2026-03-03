# Create a program, palindrome.py that has a function that takes one string
# argument and prints a sentence indicating if the text is a palindrome.
# The function should consider only the alphanumeric characters in the string,
# and not depend on capitalization, punctuation, or whitespace.

import sys

string = str(sys.argv[1])

def palindrome(string):
    
    string_lower = string.lower().split()
    pal_test = lambda phrase: phrase == phrase[::-1]
    verdict = pal_test(string_lower)

    if verdict == True:
        print("It's a palindrome!")
    elif string_lower[0][0] == string_lower[-1][-1]:
        print("It's a palindrome!")
    else:
        print("It's not a palindrome!")

palindrome(string)
