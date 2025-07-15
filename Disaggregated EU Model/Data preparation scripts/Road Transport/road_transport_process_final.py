# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 17:56:55 2024

@author: m.karmellos
"""

import pandas as pd
from pathlib import Path
import copy
from sys import exit

# Run a function that processes data for all countries
data_file = 'Country Codes.xlsx'
countries = pd.read_excel(data_file, header=0, index_col=0)

import road_transport_function
for k in countries.index:
    if __name__ == "__main__":
        road_transport_function.road_transport_function_final(k, countries['Code'].loc[k])
        print('Data Processing for country: ', k)

