import pandas as pd

# df = pd.DataFrame(data=[[100,80,90],[90,90,90],[80,90,500]], index=['kor','math','eng'], columns=['1번','2번','3번'])
# print(df)

# list = [

#     {'name' : 'kim', 'age' : 10, 'job' : 'desinger'},
#     {'name' : 'kyu', 'age' : 20, 'job' : 'engineer'},
#     {'name' : 'kang', 'age' : 30, 'job' : 'PM'}
# ]

# df = pd.DataFrame(list)
# print(df)
# print(df['name'])
# print(df[['name','age']])

list = [

    ['name' , ['kim', 'lee', 'park']],
    ['age' , [20,25,30]],
    ['job' , ['d','p','pm']]
]

df = pd.DataFrame(list)
print(df.info())
