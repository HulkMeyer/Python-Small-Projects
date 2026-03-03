import sys
import numpy as np
np.random.seed(42)
# Create program that has a function that takes in three arguments and prints
# the integer that was indexed as "Your random value is x" where x = that result
# of the indexing.  The program should not crash if the third value is larger
# than the first
size = int(sys.argv[1])
factor = int(sys.argv[2])
selection = int(sys.argv[3])

def reallyrandom(size, factor, selection):
    thing = np.random.randint(0,10, size=size)
    thing = thing*factor
    if (selection < size):
        value = str(thing[selection])
        print('Your random value is '+ value)
    else:
        print()

reallyrandom(size, factor, selection)
