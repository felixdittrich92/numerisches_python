from sys import getsizeof as size
import numpy as np

# Liste-Speicherbedarf
lst = [24, 12, 57]
size_of_list_object = size(lst)
size_of_elements = len(lst) * size(lst[0])

total_list_size = size_of_list_object + size_of_elements
print("Größe ohne Größe der Elemente : ", size_of_list_object)
print("Größe aller Elemente : ", size_of_elements)
print("Gesamtgröße der Liste : ", total_list_size)

lst = []

print("Speicherbedarf einer leeren Liste : ", size(lst))

# Numpy-Array-Speicherbedarf
a = np.array([24, 12, 57], np.int8)
print(size(a) - 96)
a = np.array([24, 12, 57], np.int16)
print(size(a) - 96)
a = np.array([24, 12, 57], np.int32)
print(size(a) - 96)
a = np.array([24, 12, 57], np.int64)
print(size(a) - 96)