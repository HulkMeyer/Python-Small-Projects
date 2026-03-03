import sys
# IMPORTANT Your autotest cases will NOT work if you don’t load your sys.argv like below. For this assignment, load in your sys.argv like so:
loop_list = sys.argv[1:]
# The above loop_list a list-type variable which contain numbers that are string-typed (ex. ['1', '2', '3', '4', '5'])
# Your program should: Convert these string-type integers into integer-type. For each of the numbers in the list, add its own index position.
# Example 1 - If the argument is ['5', '5', '5'], the program should print:
#   [5, 6, 7]

def loopindex(loop_list):
    for i in range(len(loop_list)):
        x = int(loop_list[i])
        x = x + i
        loop_list[i]=x
    print(loop_list)

loopindex(loop_list)
