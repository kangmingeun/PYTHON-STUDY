import pandas as pd

def is_wireless(row):
    if row == 'MOUSE' or row == 'KEYBOARD':
        return True
    else:
        return False


product_list = [

    {'name' : 'MOUSE', 'price' : 100, 'company' : 'A'},
    {'name' : 'SSD', 'price' : 200, 'company' : 'B'},
    {'name' : 'KEY', 'price' : 300, 'company' : 'C'}
    
]
df = pd.DataFrame(product_list, columns = ['name','price','company'])
df['stock'] = 5
series = pd.Series(['10%', '5%', '7%'], index = [0,1,2])
df['D/C'] = series
df['read_price'] = df['price'] * (1 - (df['D/C'].str.rstrip('%').astype(float)/100))
df['wireless'] = df.company.apply(is_wireless)
create_date = ['2017-09-27','2017-12-27','2018-09-27']
df['create_date'] = create_date
# df['year'] =df.create_date.apply(extract_year)
print(df)
df.drop([1])
df = df.drop(["wireless"],axis =1)
print(df)