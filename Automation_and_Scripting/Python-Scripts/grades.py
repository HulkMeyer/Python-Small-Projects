# Use this exact dictionary to complete this assignment (Do NOT alter this
# this dictionary - points will be deducted if dictionary is chaged):
grades = {'Biology':80, 'Physics':88, 'Chemistry':98, 'Math':89, 'English':79, 'Music':67, 'Hisory':68,'Art':53, 'Economics':95, 'Psychology':88}
# Create a program, that takes an arguement(Subject) and prints the average score excluding the Subject, to two decimals
# For example
#   If the arguement is Biology, it should print 80.56, If the argument is Chemistry, it should print 78.56

import sys

course = str(sys.argv[1])

def grade(course):
    sum_grades = 0
    for i in grades:
        if i == course:
            continue
        sum_grades = sum_grades + grades[i]
    average = sum_grades / 9
    print(round(average, 2))

grade(course)
