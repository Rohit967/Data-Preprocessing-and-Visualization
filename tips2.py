#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
"""

import pandas as pd
import numpy as np

# Read the file into a DataFrame: df
tips = pd.read_csv('tips2.csv',index_col = 0)


# Define recode_sex()
def recode_sex(sex_value):

    # Return 1 if sex_value is 'Male'
    if  sex_value == 'Male':
        return 1
    
    # Return 0 if sex_value is 'Female'    
    elif sex_value == 'Female':
        return 0
    
    # Return np.nan    
    else:
        return np.nan

# Apply the function to the sex column
tips['sex'] = tips['sex'].apply(recode_sex)

# Print the first five rows of tips
print(tips.head())

# remove the '$' sign
tips['total_bill'] = tips['total_bill'].str.replace("$","")
tips['tip'] = tips['tip'].str.replace("$","")

# Convert 'total_bill' to a numeric dtype
tips['total_bill'] = pd.to_numeric(tips['total_bill'], errors ='coerce')

# Convert 'tip' to a numeric dtype
tips['tip'] = pd.to_numeric(tips['tip'], errors='coerce')

# Print the info of tips
print(tips.info())

x = tips.dropna() #drop all rows which include missing values with .dropna() method

# fill missing values with .fillna()

#tips['tip'] = tips['tip'].fillna(0) # fill missing value with 0
mean_value = tips['tip'].mean() # fill missing value with mean
tips['tip'] = tips['tip'].fillna(mean_value)

tips = tips.drop_duplicates() # drop duplicate values