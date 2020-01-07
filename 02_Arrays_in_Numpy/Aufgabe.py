import numpy as np

print("eindimensionales Array anlegen")
onedim = np.array([1, 2, 3, 4, 5, 6])
print(onedim)

print("Array was aus den ungeraden Indizes von onedim besteht")

un_onedim = onedim[::2]
print(un_onedim)

print("Array umdrehen")

onedim = onedim[::-1]
print(onedim)

print("wie sieht die Augabe aus ?")

a = np.array([1, 2, 3, 4, 5])
b = a[1:4]
b[0] = 200
print(a[1])

print("zweidimensionales Array anlegen")

twodim = np.array([[1, 2, 3], 
                   [4, 5, 6]])
print(twodim)

print("jede Zeile umdrehen")

print(twodim[::,::-1])

print("Array umdrehen")

print(twodim[::-1])

print("neues Array welches die Zeilen und Spalten in umgedrehter Reihenfolge beinhaltet")

m = twodim[::-1, ::-1]
print(m)

print("Erste Reihe und Spalte von m abschneiden")

print(m[1:-1, 1:-1])