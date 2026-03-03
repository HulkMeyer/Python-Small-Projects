# Use the sacramento.csv file to complete the following assignment.
# Create a file, sacramento.py, that loads the .csv file and runs a logistic
# regression. The regression should predict whether or not a house has
# 1 or more than one bathroom based on beds, sqft, and price, in that
# order. You will need to create a new variable from baths, and it should make
# it such that those observations of 1 bath correspond to a value of 0, and those
# with more than 1 bath correspond to a 1. Make sure to add a constant using
# sm.add_constant(X) Your file should print the results in this way:
import sys
import pandas as pd
import numpy as np
import statsmodels.api as sms

data = pd.read_csv('sacramento.csv', usecols = ['baths', 'beds', 'sqft', 'price'])

independent = data[['beds', 'sqft', 'price']]
dependent = np.select([data['baths'] == 1, (data['baths'] >= 1)], [0,1])

independent = sms.add_constant(independent)

model = sms.Logit(dependent, independent).fit()

print(model.params.round(2))
print(model.pvalues.round(2))
print('The smallest p-value is for sqft')
