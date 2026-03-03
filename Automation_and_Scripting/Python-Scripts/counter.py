import sys
# You are given a single string argument. Print a dictionary where the keys are composed of each letter from a word and values are the sum of each letters’ appearances.
# Example 1 - If the word is “good”, the program should print:
# {'g': 1, 'o': 2, 'd': 1}
string = sys.argv[1]

def counter(string):
    letters = list(string)
    dictionary = dict()
    for i in letters:
        if i in dictionary:
            dictionary[i]+=1
        else:
            dictionary[i]=1
    print(dictionary)

counter(string)
