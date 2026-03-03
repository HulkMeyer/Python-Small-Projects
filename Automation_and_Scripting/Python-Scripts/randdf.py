import sys
# Create a program, that has a function that takes two integer arguments
# and prints a Pandas dataframe. The two arguments will correspond to the number
# of rows and number of columns, respectively. The dataframe should be filled
# with random integers from 0 to 100. Set your random seed to 56.

import pandas as pd
import numpy as np
np.random.seed(56)

r = int(sys.argv[1])
c = int(sys.argv[2])

def createdataframe(r,c):
    df = pd.DataFrame(np.random.randint(0,100, size=(r,c)))
    print(df)

createdataframe(r,c)
