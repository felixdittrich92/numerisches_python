import numpy as np

x = np.array([[45, 43, 67],
              [45, 18, 42],
              [36, 78, 99],
              [33, 55, 77],
              [21, 36, 77],
              [46, 98, 102]])

print(x.shape)
print("---------------------")

# Shape ändern
x.shape = (3, 6)
print(x)
print("---------------------")
x.shape = (2, 9)
print(x)

# Shape dreidimensionales Array
B = np.array([ [[111, 112], [121, 122]],
               [[211, 212], [221, 222]],
               [[311, 312], [321, 322]] ])  

print(B.shape)