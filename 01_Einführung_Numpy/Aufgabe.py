import numpy as np

# eindimensionales Array anlegen
onedim = np.array([1, 2, 3, 4, 5, 6])
print(onedim)

# ganze Array + 2
print(onedim + 2)

# Teilbereich ausgeben [Start-inklusiv:Stop-exklusiv:Schrittweite]
print(onedim[2:5:1])

# Array "umdrehen"
onedim = onedim[::-1]
print(onedim)

# zweidimensionales Array anlegen
twodim = np.array([[1, 2, 3], 
                   [4, 5, 6]])
print(twodim)


