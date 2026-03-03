# Create a program that has a function that takes one integer arguments
# The function will print a list of all values between 3000 and 5000 that
# is divisible by: the integer argument the integer +7 the integer arguement ^2
import sys

value = int(sys.argv[1])
#use modulos % to check the remanding

def inrange(value):
    base =[]
    for i in range(3000,5001):
        if (i % value == 0 and i % (value+7) == 0 and i % value**2 == 0):
            base.append(i)
        else:
            continue
    print(base)

inrange(value)
