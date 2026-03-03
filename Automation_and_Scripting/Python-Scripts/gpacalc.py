# Use the following dictionary to complete theis assignment:
grades = {'A':4.0, 'A-':3.66, 'B+':3.33, 'B':3.0, 'B-':2.66, 'C+':2.33, 'C':2.0, 'C-':1.66, 'D+':1.33, 'D':1.00, 'D-':.66, 'F':0}
# Create a program that takes four letter grades arguments and prints out the corresponding GPA, to two decimals.
# Your porgram should accept both upper-case and lower case arguements.
# Your program should print in the form:

import sys

letter1 = str(sys.argv[1])
letter2 = str(sys.argv[2])
letter3 = str(sys.argv[3])
letter4 = str(sys.argv[4])

def my_gpa():
    grade1 = grades[letter1.upper()]
    grade2 = grades[letter2.upper()]
    grade3 = grades[letter3.upper()]
    grade4 = grades[letter4.upper()]
    average = (grade1+grade2+grade3+grade4)/4
    print(f'My GPA is {average:.2f}')

my_gpa()
