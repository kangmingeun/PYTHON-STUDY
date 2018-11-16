import numpy as np

data = np.loadtxt('./day15/ex2.csv',delimiter=',', dtype=np.int)
print(data[:3,:3]) #상위 3개
print('-'*20)
# 배열의 크기
print(data.shape)
print('-'*20)
# 데이터 검사
print(np.unique(data[:,1]))
print('-'*20)
# 전국 대상의 가구수 합
print("부산의 모든현황 : ",data[data[:,1] == 8])
print('-'*20)
print('전국 합계 : ', np.sum(data[:,2]))
print('증감률 :' , np.min(data[:,5]))
print('400이상 발생 건수 :' , data[data[:,2] >= 400])