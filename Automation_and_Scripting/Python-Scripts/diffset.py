import sys
# IMPORTANT
# Your autotest cases will NOT work if you don't load your sys.argv like below
set_a = sys.argv[1:]
set_b = ['apple','banana', 'mango', 'orange']
# The above set_a is a list-type variable which contains words.
# Create a program, diffset.py.  Your program should: Find the words that exists
# in set_a but are not in set_b.  Print the output in a set format.

def diffset(set_a):
    not_included = []
    for i in set_a:
        if i not in set_b:
            not_included.append(i)
    print(set(not_included))

diffset(set_a)
