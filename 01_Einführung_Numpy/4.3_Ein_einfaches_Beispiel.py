import numpy as np
import matplotlib.pyplot as plt

# Liste 
cvalues = [20.1, 20.8, 21.9, 22.5, 22.7, 21.8, 21.3, 20.9, 20.1]
print(cvalues, type(cvalues))

# Liste to Array
C = np.array(cvalues)
print(C, type(C))

# umrechnen in Grad Fahrenheit
fvalues = [x*9/5 + 32 for x in cvalues]   # List Comprehensions
print(fvalues, type(fvalues))

# Visualisierung
plt.plot(C)
plt.show()
