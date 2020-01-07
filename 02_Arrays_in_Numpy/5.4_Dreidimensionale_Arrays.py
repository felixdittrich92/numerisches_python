import numpy as np

X = np.array([ [[3, 1, 2],
                [4, 2, 2]],
                
               [[-1, 0, 1],
                [1, -1, 2]],
                
               [[3, 2, 2],
                [4, 4, 3]],
                
               [[2, 2, 1],
                [3, 1, 3]] ])
print(X[:,:,:])
print(X.shape)

print("----------------------------------------")

print("Dimension 0 mit der Größe : ", X.shape[0])
for i in range(X.shape[0]):
    print(X[i,:,:])

print("----------------------------------------")

print("Dimension 1 mit der Größe : ", X.shape[1])
for i in range(X.shape[1]):
    print(X[:,i,:])

print("----------------------------------------")

print("Dimension 0 mit der Größe : ", X.shape[2])
for i in range(X.shape[2]):
    print(X[:,:,1])