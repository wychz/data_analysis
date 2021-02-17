import pandas as pd


yuan_to_dollar = [683.10, 676.95, 645.88, 631.25, 619.32, 614.28, 622.84, 664.23, 675.18, 661.74]

def process_data():

    for index in range(2009, 2019):
        file_name = 'data/' + str(index) + '.xlsx'
        df = pd.read_excel(file_name)
        df.fillna(0, inplace=True)
        row_length = df.shape[0]
        col_length = df.shape[1]
        df.loc[row_length, '海关代码'] = '进口技术复杂度：地区'

        for i in range(0, row_length):
            df.loc[i, '人均GDP（元）'] = df.loc[i, '人均GDP（元）'] / yuan_to_dollar[index - 2009] * 100
            df.loc[i, '总进口额（千美元）'] = df.loc[i, '总进口额（千美元）'] * 1000
        df.rename(columns={'人均GDP（元）': '人均GDP（美元）'}, inplace=True)
        df.rename(columns={'总进口额（千美元）': '总进口额（美元）'}, inplace=True)

        for col_name, col_content in df.iteritems():
            prody_j = 0
            column_name = col_name
            if not column_name.startswith('T'):
                continue
            # if df.loc[i, column_name] is None:
            #     continue
            for i in range(0, row_length):
                x_i = df.loc[i, '总进口额（美元）']  # x_i = df.loc[i, 21]
                y_i = df.loc[i, '人均GDP（美元）']  # y_i = df.loc[i, 22]
                x_ij = df.loc[i, column_name]
                x_numerator = x_ij / x_i

                x_denominator = 0
                for i_in in range(0, row_length):
                    x_denominator_ij = df.loc[i_in, column_name]
                    x_denominator_i = df.loc[i_in, '总进口额（美元）']  # x_denominator_i = df.loc[i_in, 21]
                    x_divide_in = x_denominator_ij / x_denominator_i
                    x_denominator += x_divide_in
                prody_j += x_numerator / x_denominator * y_i

            df.loc[row_length, column_name] = prody_j

        df['进口技术复杂度：产品'] = 0
        for i in range(0, row_length):
            M_sum = 0
            for col_name, col_content in df.iteritems():
                column_name = col_name
                if not column_name.startswith('T'):
                    continue
                prody_j = df.loc[row_length, column_name]
                M_ij = df.loc[i, column_name]
                M_i = x_i = df.loc[i, '总进口额（美元）']  # M_i = x_i = df.loc[i, 21]
                M_sum += M_ij / M_i * prody_j
            df.loc[i, '进口技术复杂度：产品'] = M_sum

        df.replace(0, '', inplace=True)
        df.to_excel('data_processed/' + str(index) + '_processed.xlsx')


if __name__ == '__main__':
    process_data()