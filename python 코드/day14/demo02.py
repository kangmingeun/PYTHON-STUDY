import pandas as pd

product_list = [

    {'name' : 'Mouse', 'price' : 100, 'company' : 'A'},
    {'name' : 'SSD', 'price' : 200, 'company' : 'B'},
    {'name' : 'KEY', 'price' : 300, 'company' : 'C'}
    
]
df = pd.DataFrame(product_list, columns = ['name','price','company'])
df['stock'] = 5
series = pd.Series(['10%', '5%', '7%'], index = [0,1,2])
df['D/C'] = series
df['read_price'] = df['price'] * (1 - (df['D/C'].str.rstrip('%').astype(float)/100))
print(df)