import pandas as pd
from pytrends.request import TrendReq

pytrend = TrendReq()
# Create payload and capture API tokens. Only needed for interest_over_time(), interest_by_region() &related_queries()
#trendy_keywords = ('pijama')
kw_list = ['pijama', 'kot pantolon', 'sapka', 'panduf', 'bralet']
kw = kw_list
pytrend.build_payload(
    (kw_list), timeframe='2020-01-01 2020-12-24', geo="TR", cat=18)
# Related Queries, returns a dictionary of dataframes
related_queries_dict = pytrend.related_queries()
print(related_queries_dict)
# for rising related queries
related_queries_rising = related_queries_dict.get(kw).get('rising')
# for top related queries
related_queries_top = related_queries_dict.get(kw).get('top')
print('**************** RISING RELATED KEYWORDS **************')
print(related_queries_rising)
print('**************** TOP RELATED KEYWORDS *******************')
print(related_queries_top)

for i in kw:
    print(related_queries_rising)
    print(related_queries_top)
related_queries_top.to_csv(r'C:\Users\JJimbo\Desktop\GE.csv', index=False)
