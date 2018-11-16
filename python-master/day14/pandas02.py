import pandas as  pd


input_file = './day14/sales_2017.xlsx'
output_file = './day14/output/pandas_output.xls'

df = pd.read_excel(input_file, steetname = 'january_2017')
new_df = df[df['Customer Name'].str.startswith('j')]
print(new_df)
