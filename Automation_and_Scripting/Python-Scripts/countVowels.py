# Create a program called countVowels.py that has a function that takes in a
# string then prints the number of unique vowels in the string (regardless of
# upper or lower case).

import sys

# Declare countVowels Function
def countVowels(input_str):
    # Declare an Empty List
    vowels=[]

    # Use a for loop to iterate
    for i in input_str:
        # Check if it is a vowel or not
        if i in ['a','e','i','o','u','A','E','I','O','U']:
            # If it already present in the list or not
            if i.upper() not in vowels:
                # If it is not present in the list, add it to the list
                vowels.append(i.upper())

    # Return the length of the list
    return len(vowels)

# Take input from command line
input_str=str(sys.argv[1])

# Call the function and print result
print(countVowels(input_str))
