import numpy as np

print("--------------------------------------")
print("eindimensionale Arrays indizieren")
print("--------------------------------------")

F = np.array([1, 1, 2, 3, 5, 8, 13, 21])
# Ausgabe erstes Element
print(F[0])
# Ausgabe letzes Element
print(F[-1])

S = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
print(S[2:5])
print(S[:4])
print(S[6:])
print(S[:])

print("--------------------------------------")
print("Mehrdimensionale Arrays indizieren")
print("--------------------------------------")

#                  Spalte
#               0    1     2     
A = np.array([[3.4, 5.7, -3.2],  # 0
              [1.1, -3.8, 7.7],  # 1    Zeile
              [2.2, 5.9, -1.0]]) # 2 

# [Zeile][Spalte]
print(A[1][2])
# komplette Zeile
print(A[1])

#  Position : [0, 1][0, 1]
#                        Spalte
#                    0           1
B = np.array([ [[111, 112], [121, 122]],   # 0
               [[211, 212], [221, 222]],   # 1  Zeile
               [[311, 312], [321, 322]] ]) # 2 

# [Zeile][Spalte][Position]
print(B[1][1][1]) 

print("--------------------------------------")
print("Mehrdimensionale Arrays indizieren")
print("       Teilbereichoperator")
print("--------------------------------------")

A = np.array([
    [11, 12, 13, 14, 15],
    [21, 22, 23, 24, 25],
    [31, 32, 33, 34, 35],
    [41, 42, 43, 44, 45],
    [51, 52, 53, 54, 55] ])

# [start:stop:step]
# Spalte , Zeile   von(inklusive) : bis(exklusive)
print(A[:3, 2:])
print("------------------")
print(A[3:,:])
print("------------------")
print(A[:, 4:])
print("------------------")

X = np.arange(28).reshape(4, 7)
print(X)
print("------------------")
print(X[::2, ::3])
print("------------------")
print(X[::, ::3])
print("------------------")

# dreidimensionales Array
A = np.array([ [ [45, 12, 4], [45, 13, 5], [46, 12, 6] ], 
               [ [46, 14, 4], [45, 14, 5], [46, 11, 5] ],
               [ [47, 13, 2], [48, 15, 5], [46, 15, 1] ], ])

print(A[1:3, 0:2, :])


