import numpy as np

# komponentenweise
kalorientabelle = np.array([30,52,88,36,86,160,375,115,43,71])
verzehr_in_gramm = np.array([240,95,135,120,200,160,290,450,500,0])
kalorien_aufgenommen = kalorientabelle * verzehr_in_gramm / 100
print(kalorien_aufgenommen.sum())

A = np.array([[11,12,13], [21,22,23], [31,32,33]])
B = np.array([[5,4,2], [1,0,2], [3,8,2]])
print("Addition zweier Arrays: ")
print(A+B)
print("\nMultiplikation zweier Arrays: ")
print(A*B)