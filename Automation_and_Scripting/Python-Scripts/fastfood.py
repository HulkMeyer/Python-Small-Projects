import sys

# Use the fastfood.csv file to complete the following assignment.
# Create a file, fastfood.py, that loads the .csv file and runs a regression
# predicting calories from total_fat, sat_fat, cholesterol, and sodium
# in that order. Add a constant using sm.add_constant(data). Note: you
# will not need to upload the .csv to CodeGrade because I have pre-loaded
# it. Then, print the following to two decimals

import pandas as pd
import numpy as np
import statsmodels.api as sms

data = pd.read_csv('fastfood.csv', usecols = ['total_fat', 'sat_fat', 'cholesterol', 'sodium', 'calories'])

x = data[['total_fat', 'sat_fat', 'cholesterol', 'sodium']]
y = data[['calories']]

x = sms.add_constant(x)

sm_model = sms.OLS(y,x)
model = sm_model.fit()

print(model.mse_total.round(2))
print(model.rsquared.round(2))
print(model.params.round(2))
print(model.pvalues.round(2))
