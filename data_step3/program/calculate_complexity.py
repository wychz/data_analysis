import numpy as np
import pandas as pd

year_list = np.arange(2009, 2019).tolist()
codes = ['T01', 'T02', 'T03', 'T04', 'T05', 'T06', 'T07', 'T08', 'T09', 'T10', 'T11', 'T12', 'T13', 'T14', 'T15', 'T16', 'T17', 'T18', 'T19', 'T20', 'T21', 'T22']


for year in year_list:
    df_year = pd.read_excel("../data_processed/{}.xlsx".format(year))
    df_year = df_year.dropna()
    cur_dict = {'year': year, 'country': '技术复杂度'}
    for code in codes:
        dividend = 0
        divisor = 0
        for index, row in df_year.iterrows():
            dividend += row[code] / row['(TT)总出口额'] * row['(Y)人均GDP']
        for index, row in df_year.iterrows():
            divisor += row[code] / row['(TT)总出口额']
        res = dividend / divisor
        cur_dict[code] = res
    df_year = df_year.append(cur_dict, ignore_index=True)
    df_year.to_excel("../data_final/complexity_{}.xlsx".format(year), index=None)