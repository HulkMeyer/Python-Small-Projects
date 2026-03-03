# Use the german_credit_data.csv file to complete the following assignment.
# Create a file, german.py, that loads the .csv file and runs a regression predicting
# credit amount from age and duration, in that order. Add a constant using sm.add_constant(data).
# You will need to rename the column 'Credit amount' and should change
# it to 'Credit_amount'. Note: you will not need to upload the .csv to CodeGrade
# because I have pre-loaded it. Then, print the parameters and R-squared to 2 decimals using

import sys
import pandas as pd
import numpy as np
import statsmodels.api as sms

data = pd.read_csv('german_credit_data.csv', usecols = ['Age', 'Duration', 'Credit amount'])

independent = data[['Age', 'Duration']]
dependent = data[['Credit amount']]

independent = sms.add_constant(independent)

sm_model = sms.OLS(dependent,independent)
model = sm_model.fit()

print(model.params.round(2))
print(model.rsquared.round(2))
