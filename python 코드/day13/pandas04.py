import sys
import csv
import pandas as pd
import re

input_file = 'day13\\csv\\supplier_data.csv'
output_file = 'day13\\csv\\output\\pandas_output.csv'

data_frame = pd.read_csv(input_file)
# iloc -> index, 숫자로 데이터 검색
# loc -> 이름(key,값) 데이터 결재
# ix -> index, 이름 사용 가능


new_data_frame = data_frame.ix[data_frame['Invoice Number']\
                                        .str.startswith('001-'), :]
           

new_data_frame.to_csv(output_file, index = False)
print('Pandas Done.')
