import sys
# For this assignment, use the president_heights.csv file found in the Brightspace module
# You WILL NOT NEED TO SUBMIT THE FILE TO CODEGRADE Create a program
# presidents.py, that takes two arguments. These arguments will
# correspond to the start and stop of a slice, respectively. It will slice the heights
# column in the president_heights.csv files.
# Then print off the average height, rounded to two decimals, of the selected presidents in the following form:
# The average height of presidents number x to y is z
# WHERE
# x = start of the slice y = end of the slice z = calculated average
import pandas as pd
import numpy as np

data = pd.read_csv('president_heights.csv')

start = int(sys.argv[1])
stop = int(sys.argv[2])


def avgheight(start, stop):
    height = data[start:stop]['height(cm)']
    averageheight = height.mean()
    averageheight = round(averageheight,2)
    print('The average height of presidents number ' + str(start) + ' to ' + str(stop) + ' is ' + str(averageheight))

avgheight(start, stop)
