#Create a program, luke.py, using the follwing dictionary
relations = {'Darth Vader':'father','Leia':'sister','Han':'brother in law', 'R2D2':'droid','Rey':'Padawan','Tatooine':'homeworld'}
#The program will take one argument, corresponding to one of the
# relations' keys. The program will print out the statement:
#   Luke, I am your # XXX:
#   Where xxx = the relationship
#For example, if the argument is Leia, it should print out
#       Luke, I am your sister
# If the Key is Darth Vader you should instead print
#       No, I am your father

import sys

person = str(sys.argv[1])

def luke(person):
    if person == 'Darth Vader':
        print('No, I am your father')
    else:
        print(f'Luke, I am your {relations[person]}')

#person = str(sys.argv[1])

luke(person)
