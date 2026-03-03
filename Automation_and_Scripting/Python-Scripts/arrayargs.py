import sys
# Create a program called array.py that has a function that takes four integer arguments.
# Those arguments should be put into an Numpy array.
# The function will have two print statements.
# The first will print the type of the array you create (which should be <class
# ‘numpy.ndarray’>). The second will print the multiplication of the four items in your array.
import numpy as np

array = np.array(sys.argv[1:])

print(type(array))

def times(array):
    result = 1
    for i in array:
        x = int(i)
        result = x * result
    print(result)

times(array)
