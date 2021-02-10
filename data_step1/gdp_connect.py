import numpy as np
import pandas as pd

data_file_path = "./data_processed/data.xlsx"
gdp_file_path = "./人均 GDP（现价美元）.xls"

df_data = pd.read_excel(data_file_path)
df_gdp = pd.read_excel(gdp_file_path, sheet_name=0, skiprows=3)
df_gdp.set_index("Country Code", inplace=True)

year_list = df_data['year'].unique().tolist()
country_list = df_data['country'].unique().tolist()

for index, row in df_data.iterrows():
    year = row['year']
    country = row['country']
    try:
        ans = df_gdp.at[country, str(year)]
    except KeyError:
        ans = None
    df_data.loc[index, '(Y)人均GDP'] = ans

df_data.to_excel('./data_processed/data_gdp.xlsx', index=None)

year_list = np.arange(2009, 2019).tolist()
for year in year_list:
    df_year = df_data[df_data['year'].isin([year])]
    df_year.to_excel('./data_processed/{}.xlsx'.format(year), index=None)
