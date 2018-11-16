import numpy as np

matrix1 = np.arange(1,31).reshape(5,6)
print(matrix1)

print(np.max(matrix1))
print(np.sum(matrix1, axis =1)) # col 단위
print(np.sum(matrix1, axis =0)) # row 단위
