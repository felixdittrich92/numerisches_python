import numpy as np

x = np.array([2, 5, 18, 14, 4])
y = x[:, np.newaxis]
print(y)

# oder
"""
x = np.array([2, 5, 18, 14, 4])
y = x.reshape((x.shape[0], 1))
print(y)
"""