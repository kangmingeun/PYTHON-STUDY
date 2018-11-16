from xlrd import open_workbook, xldate_as_tuple
from xlwt import Workbook
from datetime import date


input_file = 'day14/sales_2017.xlsx'
output_file = 'day14/output/3output.xls'

output_workbook = Workbook()
output_workbook = output_workbook.add_sheet('jan_2017_output')

filter_column = 3
with open_workbook(input_file) as workbook: 
    worksheet = workbook.sheet_by_name('january_2017')
    for row_index in range(1, worksheet.nrows):
        sale_amount = worksheet.cell_value(row_index, filter_column)
        if sale_amount > 1400.0:
            for col_index in range(worksheet.ncols):
                cell_value = worksheet.cell_value(row_index, col_index)
                cell_type = worksheet.cell_type(row_index, col_index)

                if cell_type == 3:
                    date_cell = xldate_as_tuple(cell_value, workbook.datemode)
                    data_cell = date(*data_cell[0:3]).strftime('%m/%d/%Y')
                    # output_worksheet.write(row_index, col_index, data_cell)
                    row_info.append(data_cell)
                else:
                # output_worksheet.write(row_index, col_index, cell_value)
                row_info.append(cell_value)
            data.append(row_info) 
        # data에 있는 내용물 write
        # output_worksheet,write(row_index, col_index, cell_value)
    for row_index in range(len(data)):
        for col_index in range(len(data[row_index])):
            print(row_index, col_index, '=', (data[row_index][col_index]))

output_workbook.save(output_file)
print('Done')