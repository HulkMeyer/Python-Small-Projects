# Create a program, shortest.py, that has a function that takes in a string
# argument and prints a sentence indicating the shortest word in that string.
# If there is more than one word print only the first.  your print statement
# should read:
#       "the shortest word is x"
#       Where x = the shortest word. The word should be all uppercase

import sys

def shortest(input_str):
    words = input_str.split()
    tiny = words[0]
    for word in words:
        if len(word) < len(tiny):
            tiny = word
    print(f"The shortest word is {tiny.upper()}")

input_str = str(sys.argv[1])

shortest(input_str)
