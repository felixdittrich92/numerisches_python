import numpy as np

# Einsen
# float
E = np.ones((2, 3))
print(E)

print("---------------------------")

# int
F = np.ones((3, 4), dtype=int)
print(F)

print("---------------------------")

# Nullen
# float
Z = np.zeros((2, 4))
print(Z)

print("---------------------------")

# int
Z = np.zeros((3, 4), dtype=int)
print(Z)

print("---------------------------")

x = np.array([2, 5, 18, 14, 4])
E = np.ones_like(x)
print(E)

print("---------------------------")

Z = np.zeros_like(x)
print(Z)