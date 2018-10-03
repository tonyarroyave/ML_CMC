#!/usr/bin/python3

"""This script will execute the scraper.js,
    after that is going to process the data for later consuption"""

import os
import json
import datetime
import numpy as np
import pandas as pd
from Naked.toolshed.shell import execute_js
import warnings

warnings.filterwarnings("ignore")
Trading_ID = "BTC-USDT"
Testing = True

# scraper.js execution
if Testing:
    success_scraper = execute_js('scrape_hood.js', arguments=Trading_ID)
    if success_scraper:
        success_combine = execute_js('combine_hood.js', arguments=Trading_ID)
        if not success_combine:
            print('Error executing combine.js')
            raise Error('combine.js')
    else:
        print('Error executing scrape.js')
        raise Error('scrape.js')

print('Parsing json file...')


def dt_func(seconds):
    return datetime.datetime.utcfromtimestamp(seconds)


the_path = os.getcwd()
comb_data_path = os.path.join(the_path, '../data/combined-data/')
file_name = 'Cobinhood-' + Trading_ID + '.json'
file_path = comb_data_path + file_name
with open(file_path, 'r') as handle:
    parsed = json.load(handle)

print('Creating DataFrame...')

df = pd.DataFrame(columns=['Timestamp', 'Open', 'High', 'Low', 'Close',
                           'Volume (BTC)', 'Volume (Currency)', 'Weighted Price (USD)'], data=parsed)

df['Timestamp'] = df['Timestamp'].map(lambda x: dt_func(x))

df['Average'] = (df['High']+df['Low']+df['Open']+df['Close'])/4
df['Date'] = pd.to_datetime(df['Timestamp'])

with pd.option_context('mode.use_inf_as_null', True):
    df.loc[df.isnull().any(axis=1), 1:9] = np.nan
    df.fillna(method='pad', inplace=True)

print('Saving CSV...')

new_df = df[['Date', 'Average']].copy()
new_df.to_csv(os.path.join(the_path, '../data/') +
              'processed-data/' + Trading_ID + '-processed.csv')
print('DONE!')
