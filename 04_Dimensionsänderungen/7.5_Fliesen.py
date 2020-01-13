import numpy as np

x = np.array([ [1, 2], [3, 4]])
print(np.tile(x, (3, 4)))

print('---------------------------')

x = np.array([3.4])
y = np.tile(x, (5,))
print(y)

print('------------weitere Beispiele---------------')

x = np.array([[1,2], [3,4]])
print(np.tile(x,2))
print('---------------------------')
x = np.array([[1,2], [3,4]])
print(np.tile(x, (2,1)))
print('---------------------------')
x = np.array([[1,2], [3,4]])
print(np.tile(x, (2,2)))