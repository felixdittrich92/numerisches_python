import numpy as np

x = np.array([11,22])
y = np.array([18,7,6])
z = np.array([1,3,5])
c = np.concatenate((x, y, z), axis=0)
print(c)

print('-------------------------------')

x = np.array(range(12))
x = x.reshape((3,4))
print(x)
print('---------------------')
y = np.array(range(100,112))
y = y.reshape((3,4))
print(y)
print('---------------------')
z = np.concatenate((x, y))
print(z)

print('---------------Zusammenfügen----------------')

z = np.concatenate((x, y), axis=1)
print(z)