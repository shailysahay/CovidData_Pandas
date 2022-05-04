# -*- coding: utf-8 -*-
"""
Created on Tue Apr  5 22:51:40 2022

@author: Saurabh
"""

import getData as gd
import numpy as np


# # Take a look at the first few rows
# print (gd.df_district.head())


###### Handle Missing/Null values #########


# Include 'Unassigned' and 'Unknown' district as 'Missing Values'
# So, replacing all 'Unasiigned' and 'Unknown' district values with 'NaN'
gd.df_district = gd.df_district.replace(['Unassigned','Unknown'],np.nan)

# Copy gd.df_district into a local variable to see in debug window
df_districtWithNull = gd.df_district

# Count missing values in each column
print (df_districtWithNull.isnull().sum())


# Delete rows with 'Unassigned' and 'Unknown' district values
df_districtWithNull.dropna(inplace= True, axis=0)


## Replace negative values with '0' ##

## if all columns of DF is 'int', use the below method:
#df_districtWithNull[df_districtWithNull < 0] = 0

#If some columns are 'int', use below method:
num = df_districtWithNull._get_numeric_data()
num[num < 0] = 0

print (df_districtWithNull.isnull().sum())






