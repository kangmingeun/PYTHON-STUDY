import numpy as np

matrix= np.array([
    [10,20,30,40], 
    [50,60,70,80]
])

print(matrix)

m = np.array([
    [0,1,2,3,4],
    [5,6,7,8,9],
    [10,11,12,13,14]
])

print(m[1,2])
print(m[2, 4])
print(m[1, 1:3])
print(m[1:3, 2:4])

arr = np.array( [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])

print(arr[arr % 3 == 0])
print(arr[arr % 4 == 1])
print(arr[(arr % 3 == 0) & (arr % 4 == 1)])


