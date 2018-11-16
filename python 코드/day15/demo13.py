import numpy as np

data = np.loadtxt('./day15/ex01.csv',delimiter=',', dtype=np.int)
print(data[:5,:]) #상위 5개
print('-'*20)
# 배열의 크기
print(data.shape)
print('-'*20)
# 데이터 검사
print(np.unique(data[:,0]))
print('-'*20)
# 전국 대상의 가구수 합
print("전국 가구수의 합 : ", np.sum(data[:1]))
print('-'*20)
# 가구당 평균 전력사용량의 전국 평균
print('전국 평균 전력 사용량 : ', round(data[:,2].mean()),2)
# 평균 전력사용량이 400이 넘는 지역 과가구수
print('400 초과 지역 : ',data[data[:,2] > 400, 0:2])