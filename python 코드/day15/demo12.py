import numpy as np

# a = np.loadtxt('./day15/mabang1.txt')
# print(a)

# b = np.loadtxt('./day15/mabang1.txt', dtype=np.int)
# print(b)

# c = np.loadtxt('./day15/mabang2.txt', dtype= np.str)
# print(c)

# d = np.loadtxt('./day15/mabang2.txt', dtype=np.int, delimiter=',')
# print(d)

e = np.arange(1,26).reshape(5,5)
print(e)
# np.savetxt('./day15/np_output1.txt',e)
np.savetxt('./day15/np_output3.csv',e,delimiter=',', fmt='%i')
f = np.loadtxt('./day15/np_output3.csv',dtype=np.int, delimiter=',')
print('Done')