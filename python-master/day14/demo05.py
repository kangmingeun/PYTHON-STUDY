import pandas as  pd

df = pd.read_csv('day14/emp.csv')


output_file = 'day14/output/new_output.csv'
# 1. comm -> NaN => 0 출력 (df.to_csv)
# 2. clerk은 제외하고 출력

df['comm'] = df.comm.fillna(0) # 대체해라 
# output_file = df.to_csv(output_file, na_rep = 0) # 원본데이터 유지 출력할때만바뀜
df = df[df['job'] != 'clerk']
df.to_csv(output_file, index = False ,na_rep=0)