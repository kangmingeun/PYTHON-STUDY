from xlrd import open_workbook
from xlwt import Workbook


input_file = 'day14/sales_2017.xlsx'
output_file = 'day14/output/2output.xls'

output_workbook = Workbook()
output_workbook = output_workbook.add_sheet('jan_2017_output')

with open_workbook(input_file) as workbook:
    worksheet = workbook.sheet_by_name('january_2017')
    for row_index in range(worksheet.nrows):
        
        for col_index in range(worksheet.ncols):
            print("{0}: {1},{2}".format(row_index, col_index,\ 
                                                worksheet.cell_type(row_index, col_index))

            output_worksheet.write(row_index, col_index,worksheet.cell_value(row_index, col_index)

output_workbook.save(output_file)
print('Done')