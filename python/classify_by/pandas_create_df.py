# https://pbpython.com/pandas-list-dict.html
import pandas as pd
from collections import OrderedDict
from datetime import date

# 1. dict -> row oriented
sales = [{'account': 'Jones LLC', 'Jan': 150, 'Feb': 200, 'Mar': 140},
         {'account': 'Alpha Co',  'Jan': 200, 'Feb': 210, 'Mar': 215},
         {'account': 'Blue Inc',  'Jan': 50,  'Feb': 90,  'Mar': 95 }]
df = pd.DataFrame(sales)
# 1.1 solve column order problem
df = df[['account', 'Jan', 'Feb', 'Mar']]
# 1.2 solve column order problem
sales = OrderedDict([ ('account', ['Jones LLC', 'Alpha Co', 'Blue Inc']),
          ('Jan', [150, 200, 50]),
          ('Feb',  [200, 210, 90]),
          ('Mar', [140, 215, 95]) ] )
df = pd.DataFrame.from_dict(sales)
df = pd.DataFrame(sales)
print(df)

# 2. dict -> column oriented
sales = {'account': ['Jones LLC', 'Alpha Co', 'Blue Inc'],
         'Jan': [150, 200, 50],
         'Feb': [200, 210, 90],
         'Mar': [140, 215, 95]}
df = pd.DataFrame.from_dict(sales)
df = pd.DataFrame(sales)
print(df)

# 3.1 list list -> row oriented
sales = [('Jones LLC', 150, 200, 50),
         ('Alpha Co', 200, 210, 90),
         ('Blue Inc', 140, 215, 95)]
labels = ['account', 'Jan', 'Feb', 'Mar']
df = pd.DataFrame.from_records(sales, columns=labels)
df = pd.DataFrame(sales, columns=labels)
print(df)
# 3.2 list tuple -> tow oriented
sales = [['Jones LLC', 150, 200, 50],
         ['Alpha Co', 200, 210, 90],
         ['Blue Inc', 140, 215, 95]]
labels = ['account', 'Jan', 'Feb', 'Mar']
df = pd.DataFrame.from_records(sales, columns=labels)
df = pd.DataFrame(sales, columns=labels)
print(df)

# 4. list -> column oriented
sales = [('account', ['Jones LLC', 'Alpha Co', 'Blue Inc']),
         ('Jan', [150, 200, 50]),
         ('Feb', [200, 210, 90]),
         ('Mar', [140, 215, 95]),]
df = pd.DataFrame.from_items(sales) # from_items is deprecated
df = pd.DataFrame.from_dict(OrderedDict(sales))
print(df)

