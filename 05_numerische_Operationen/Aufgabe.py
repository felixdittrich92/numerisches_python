import numpy as np

B = np.array([1, 2, 3])

B = B[np.newaxis, :]
print(B)
print('-----------------------------')

B = np.concatenate((B, B, B))
print(B)
print('-----------------------------')

#B = np.concatenate((B, B, B)).transpose()
print(B.transpose())
print('-----------------------------')

A = np.random.randint(-10, 10, (3,4))
print(A)
print('Spaltennminima : ', np.min(A, axis=0))
print('Zeilenminima : ', np.min(A, axis=1))
print('Absolutes Minimum : ', np.min(A))
