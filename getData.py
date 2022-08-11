# -*- coding: utf-8 -*-
"""
Created on Thu Mar 24 22:41:26 2022

@author: Saurabh
"""

import requests
import json
import pandas as pd



url = 'https://api.covid19india.org/state_district_wise.json'

# get response as 'string'
response_text = requests.get(url).text

# convert string to JSON - here we get a JSON dict (where 37 states are present as 37 keys 
# in the dictionary)
parse_json = json.loads(response_text)


# Converting JSON dict (where 37 states are present as 37 keys 
# in the dictionary) to JSON Array (where 37 states are present as 37 rows)
json_array = [ {'StateName' : k, 'DistrictMetaData' : parse_json[k]} for k in parse_json]



# # this does not work with NESTED dicts. 
# # It will not unwrap the nested JSON objects
data_frame_array = pd.DataFrame(json_array)

# this works with NESTED dict
df_normalized_fromArray_level1 = pd.json_normalize(json_array, max_level=1) 

# Create new DataFrame by filtering out columns from the original DataFrame
df_filterColumns = df_normalized_fromArray_level1.loc[:,["StateName", "DistrictMetaData.districtData"]]

# Create an array of dicts(objects) with all the district-wise data
district_array = []

# Iterate over all the rows of filtered dataframe
df_filterColumns = df_filterColumns.reset_index()  # make sure indexes pair with number of rows
for index, row in df_filterColumns.iterrows():

    # Populate array with dict values(objects - key:value pairs)
    district_array +=  [ {'State' : row['StateName'], 'DistrictName' : k, 'CovidData' : row['DistrictMetaData.districtData'][k]} for k in row['DistrictMetaData.districtData']]
    
   
# create DataFrame from the Array of dicts       
df_district = pd.json_normalize(district_array)
