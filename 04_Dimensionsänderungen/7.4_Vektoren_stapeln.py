import numpy as np
# geht leichter mit "tile"

A = np.array([[3,4,5]])
B = np.array([[1,9,0]])
C = np.dstack((A, B))

print("\nElemente von A:")

for i in range(C.shape[1]):
    print(C[0, i,0], end=", ")

print("\nElemente von B:")

for i in range(C.shape[1]):
    print(C[0, i,1], end=", ")

print("\nErster Eingabevektor, d.h. A:", C[:, :,0])
print("Zweiter Eingabevektor, d.h. B:", C[:, :,1])

A = np.array([3,4,5])
B = np.array([1,9,0])

print(np.row_stack((A, B)))
print(np.column_stack((A, B)))
print(np.shape(A))

A = np.array([[1,2],[3,4]])
X = np.column_stack((A, A, A))

print(np.row_stack((X, X, X)))