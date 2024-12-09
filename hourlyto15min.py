'''
Title: Hourly Demand Interpolation Script
Author: Sameer Bajaj
Date: 2024-11-27
Description: Takes in csv of demand values for every hour of a day and generates a csv of
demand values for every 15 minutes. Created for SMERC Lab @ UCLA.
'''

import pandas as pd
def interpolate_hourly_to_15min(input_csv):
    data = pd.read_csv(input_csv)
    data['Datetime'] = pd.to_datetime(data['Datetime'], format='%Y-%m-%d %H:%M:%S')
    data = data.sort_values('Datetime')
    data.set_index('Datetime', inplace=True)
    int_15 = pd.date_range(data.index.min(), data.index.max(), freq='15min')
    data_15 = data.reindex(int_15)
    data_15.reset_index(inplace=True)
    data_15["Demand"] = data_15["Demand"].interpolate(method = 'linear')
    data_15.rename(columns={'index':'Datetime'}, inplace=True)
    data_15.to_csv('interpolateddata.csv', index = False)
input_csv = 'codeinput.csv'
interpolate_hourly_to_15min(input_csv)
