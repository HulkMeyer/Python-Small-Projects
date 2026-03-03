import sys
# IMPORTANT
# Your autotest cases will NOT work if you don't load your sys.argv lke below.
# For this assignemtn, load your varables like this:
set_a = sys.argv[1:]
set_b = ['apple', 'banana', 'mango', 'orange']
# The above set_a is a list-type variable which contains words.
# Your program should: Find the common words between set_a and setb.
# Print the output in a set format
answer = []
def common(set_a):
    for i in set_a:
        if i in set_b:
            answer.append(i)
    print(set(answer))

common(set_a)
