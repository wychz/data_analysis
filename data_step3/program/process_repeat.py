import pandas as pd
import numpy as np

df_data = pd.read_excel("../data/国家出口(1).xlsx")

country_dict = dict()
for index, row in df_data.iterrows():
    country_code = row['country']
    if country_code in country_dict:
        country_dict[country_code] = country_dict[country_code] + 1
    else:
        country_dict[country_code] = 1

country_list = []
for key, value in country_dict.items():
    if value >= 10:
        print(key, " : ", value)
        country_list.append(key)

for index, row in df_data.iterrows():
    if row['country'] not in country_list:
        df_data.drop([index], inplace=True)

df_data.to_excel("../data_processed/去重结果.xlsx", index=None)

year_list = np.arange(2009, 2019).tolist()
for year in year_list:
    df_year = df_data[df_data['year'].isin([year])]
    df_year.to_excel('../data_processed/{}.xlsx'.format(year), index=None)