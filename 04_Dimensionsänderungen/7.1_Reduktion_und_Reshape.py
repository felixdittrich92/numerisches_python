import numpy as np

A = np.array([[[0,1],
               [2,3],
               [4,5],
               [6,7]],
              [[8,9],
               [10,11],
               [12,13],
               [14,15]],
              [[16,17],
               [18,19],
               [20,21],
               [22,23]]])

print('----------Funktion: flatten()----------')
# macht immer Kopie ravel nicht

Flattened_X = A.flatten()
print('Standard : ', Flattened_X)

print('C : ', A.flatten(order='C'))
print('F : ', A.flatten(order='F'))
print('A : ', A.flatten(order='A'))

print('----------Funktion: ravel()----------')

print('Standard : ', A.ravel())
print('C : ', A.ravel(order='C'))
print('F : ', A.ravel(order='F'))
print('A : ', A.ravel(order='A'))
print('K : ', A.ravel(order='K'))

print('----------Funktion: reshape()----------')
# reshape(Array, newshape, order)

A = np.array([[1,2,3],
              [4,5,6]])

B = A.reshape((6,))
print(B)
print('-------------------------')
X = np.array(range(24))
Y1 = X.reshape((3,4,2))
print(Y1) 
print('-------------------------')
new_shape = (2,3,4)
Y2 = Y1.reshape(new_shape)
print(Y2)



