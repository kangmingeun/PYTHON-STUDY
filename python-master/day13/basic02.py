import sys
import csv

input_file = 'day13\\csv\\supplier_data.csv'
output_file = 'day13\\csv\\output\\pandas_output2.csv'

with open(input_file,'r', newline='') as csv_in_file:
    with open(output_file,'w',newline='') as csv_out_file:
        filereader = csv.reader(csv_in_file)
        filewriter = csv.writer(csv_out_file)
        header = next(filereader)
        filewriter.writerow(header)    
        for row in filereader:    
            supplier = str(row).strip()
            cost = str(row[3]).strip('$').replace(',','')
            if supplier == 'Supplier Z' or float(cost) > 600:
                filewriter.writerow(row)
            
print('Done.')
