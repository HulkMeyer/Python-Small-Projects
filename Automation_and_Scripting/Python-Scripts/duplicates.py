import sys
# IMPORTANT
# Your autotest cases will NOT work if you don’t load your sys.argv like below. For this assignment, load in your sys.argv like so:
duplicated_words = sys.argv[1:]
# The above duplicated_words is a list-type variable which contains whole bunch of lower-cased words (ex. ['hello', 'world', 'welcome', 'hello', 'again']).
# Create a program, duplicates.py. It should: Remove all duplicated words from the list Then print it in descending order of alphabets (from Z to A).
# Example 1 - If the list is ['hello', 'world', 'welcome', 'hello', 'again'], the program should print:
#   ['world', 'welcome', 'hello', 'again']

def dups(duplicated_words):
    word_list = []
    for i in duplicated_words:
        if i not in word_list:
            word_list.append(i)
    word_list.sort()
    word_list.reverse()
    print(word_list)

dups(duplicated_words)
