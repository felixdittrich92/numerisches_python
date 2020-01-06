import numpy as np

print("--------------------------------------")
print("arange")
print("erzeugen von Arrays")
print("--------------------------------------")

a = np.arange(1, 7)
print(a)

# im Vergleich dazu nun range:
x = range(1, 7)
print(x) #x ist ein Iterator
print(list(x))

# weitere arange-Beispiele: 
x = np.arange(7.3)
print(x)
x = np.arange(0.5, 6.1, 0.8)  # start-inklusiv, end-exklusiv, step, dtype
print(x)
x = np.arange(0.5, 6.1, 0.8, int)
print(x)

print("--------------------------------------")
print("linspace")
print("gleichmäßig verteilte Arrays erzeugen")
print("--------------------------------------")

# 50 Werte (Default) zwischen 1 und 10
print(np.linspace(1, 10))
# 7 Werte zwischen 1 und 10
print(np.linspace(1, 10, num=7))
# ohne Endpunkt
print(np.linspace(1, 10, num=7, endpoint=False))
# mit Wert der Abstandsweite -> liefert Tupel
samples, spacing = np.linspace(1, 10, num=5, endpoint=False, retstep=True)
print(samples, spacing) 

print("--------------------------------------")
print("Nulldimensionale Arrays")
print("--------------------------------------")

x = np.array(42)
print("x : " , x)
print("Der Typ von x : ", x.dtype)
print("Die Dimension von x : ", np.ndim(x))

print("--------------------------------------")
print("Eindimensionale Arrays")
print("--------------------------------------")

F = np.array([1.2, 3.5, 6.4, 7.7, 8.5])
print("F : " , F)
print("Der Typ von F : ", F.dtype)
print("Die Dimension von F : ", np.ndim(F))

print("--------------------------------------")
print("Mehrdimensionale Arrays")
print("--------------------------------------")

A = np.array([[1.2, 3.5, 6.4],
              [1.5, -6.3, 6.6],
              [4.6, -5.7, -4.5]])
print("A : " , A)
print("Der Typ von A : ", A.dtype)
print("Die Dimension von A : ", np.ndim(A))