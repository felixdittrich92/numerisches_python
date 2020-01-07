import numpy as np

print("----identity Funktion----")

print(np.identity(4))
print("-----------------------------")
print(np.identity(4, dtype=int))

print("----eye Funktion----")

print(np.eye(5, 8, k=1, dtype=int))
print("-----------------------------")
print(np.eye(5, 8, k=3, dtype=int))