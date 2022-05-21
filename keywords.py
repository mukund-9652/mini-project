import pandas as pd

df = pd.read_csv (r'csv\Dataset_Water.xlsx')
print (df)

spw_include=['no', 'not', 'none', 'unavailabe']
water=['water','clogged', 'stagnant', 'water', 'insufficient', 'logging']
electric=['power', 'no power', 'current', 'no current', 'power']
departments=['water board', 'electric board']