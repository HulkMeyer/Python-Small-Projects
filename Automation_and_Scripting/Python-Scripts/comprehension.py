import sys
# IMPORTANT
# Your autotest case will not work if you don't load your sys.argv
#like below. For this assignment, load in your sys.argv like so:
my_int = sys.argv[1:]
# The above my_ints a list-type variable which contain numbers that are
# string-typed (ex. ['1', '2', '3', '4', '5'])
# Your program should: Convert these string-type integers into integer-type.
# If the number within the list is divisible by 3, multiply it by 10, then
# replace it.
def comprehension(my_int):
    answer = []
    for i in range(len(my_int)):
        x = int(my_int[i])
        if x%3 == 0:
            x=x*10
            answer.append(x)
        else:
            answer.append(x)
    print(answer)

comprehension(my_int)
