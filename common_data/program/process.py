import numpy as np
import pandas as pd

year_list = np.arange(2009, 2019).tolist()
codes = ['T01', 'T02', 'T03', 'T04', 'T05', 'T06', 'T07', 'T08', 'T09', 'T10', 'T11', 'T12', 'T13', 'T14', 'T15', 'T16', 'T17', 'T18', 'T19', 'T20', 'T21', 'T22']

for year in year_list:
    file_path = '../province_data/{}.xlsx'.format(year)
    df_file = pd.read_excel(file_path)
    df_file.fillna(0, inplace=True)
    df_file['地区复杂度'] = ''

    complexity_path = '../complexity_data/complexity_{}.xlsx'.format(year)
    df_complexity = pd.read_excel(complexity_path)
    complexity_series = df_complexity.iloc[-1]

    for index, row in df_file.iterrows():
        province = row['海关代码']
        cur_sum = 0
        for code in codes:
            cur = complexity_series[code]
            try:
                res = row[code] / row['总进口额（千美元）'] / 1000 * cur
            except KeyError:
                res = 0
            cur_sum += res
        df_file.loc[index, '地区复杂度'] = cur_sum

    df_file.to_excel('../data_processed/{}_processed.xlsx'.format(year), index=None)

print("success")


