import pandas as pd
import numpy as np

T01_list = [1, 2, 3, 4 ,5]
T02_list = np.arange(6, 15).tolist()
T03_list = [15]
T04_list = np.arange(16, 25).tolist()
T05_list = [25, 26, 27]
T06_list = np.arange(28, 39).tolist()
T07_list = [39, 40]
T08_list = [41, 42, 43]
T09_list = [44, 45, 46]
T10_list = [47, 48, 49]
T11_list = np.arange(50, 64).tolist()
T12_list = [64, 65, 66, 67]
T13_list = [68, 69, 70]
T14_list = [71]
T15_list = np.arange(72, 84).tolist()
T16_list = [84, 85]
T17_list = [86, 87, 88, 89]
T18_list = [90, 91, 92]
T19_list = [93]
T20_list = [94, 95, 96]
T21_list = [97]
T22_list = [98, 99]
codes = ['T01', 'T02', 'T03', 'T04', 'T05', 'T06', 'T07', 'T08', 'T09', 'T10', 'T11', 'T12', 'T13', 'T14', 'T15', 'T16', 'T17', 'T18', 'T19', 'T20', 'T21', 'T22']
code_list = [T01_list, T02_list, T03_list, T04_list, T05_list, T06_list, T07_list, T08_list, T09_list, T10_list, T11_list, T12_list, T13_list, T14_list, T15_list, T16_list, T17_list, T18_list, T19_list, T20_list, T21_list, T22_list];
year_list = np.arange(2009, 2019).tolist()

columns = ['year', 'country']
columns.extend(codes)
columns.append('(TT)总出口额')
columns.append('(Y)人均GDP')
df_res = pd.DataFrame(columns=columns)

df_all = pd.read_excel("./各国对世界hs2分位产品出口额.xlsx")


for year in year_list:
    df_year = df_all[df_all['Year'].isin([year])]
    country_list = df_year['Reporter ISO'].unique().tolist()
    for country in country_list:
        df_year_country = df_year[df_year['Reporter ISO'] == country]
        country_dict = {'year': year, 'country': country}
        # country_array = [country]
        for index, code in enumerate(codes):
            cur_list = code_list[index]
            df_year_country_code = df_year_country[df_year_country['Commodity Code'].isin(cur_list)]
            cur_sum = df_year_country_code['Trade Value (US$)'].sum()
            # country_array.append(cur_sum)
            country_dict[code] = cur_sum
        df_res = df_res.append(country_dict, ignore_index=True)
        # df_res.append(country_array, ignore_index=True)

df_res.dropna(subset=['country'], inplace=True)
df_res['(TT)总出口额'] = df_res.iloc[:, 2:24].sum(axis=1)
df_res.to_excel('./data_processed/data.xlsx', index=None)

print(df_all)