# -*- coding: utf-8 -*-


import pandas as pd

from pytrends.request import TrendReq
from pprint import pprint
import json
pytrend = TrendReq()


product_list = ["sweatshirt", "mont", "pijama"]
gender_list = ["erkek", "kadın", "çocuk"]
product_matrix = []
kw_list = ['sweatshirt', 'kadın sweatshirt', 'erkek sweatshirt', 'çocuk sweatshirt', 'mont',
           'kadın mont', 'erkek mont', 'çocuk mont', 'pijama', 'kadın pijama', 'erkek pijama', 'çocuk pijama']

for i in range(0, len(product_list)):
    for j in range(0, len(gender_list)):
        product_matrix.append(gender_list[j]+" " + product_list[i])
print(product_matrix)

#kw = kw_list

###########################################

dataframes = []

for i in range(0, len(product_matrix), 4):
    kw = product_matrix[i:i+4]
    pytrend.build_payload(kw, timeframe='now 7-d', geo="TR", cat='18')
    related_queries_dict = pytrend.related_queries()
    for key in related_queries_dict:
        df = related_queries_dict.get(key).get('rising')
        df['kw'] = key
        dataframes.append(df)
        df.to_csv(r'C:\Users\JJimbo\Desktop\GE.csv', index=False)
