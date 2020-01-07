import numpy as np

F = np.array([[11, 12, 13, 14],
              [11, 12, 13, 14],
              [11, 12, 13, 14]], order='F')

C = F.copy()
C2 = np.copy(F)

# Test F wurde kpiert und ist keine Instanz mehr von F
#C = C+C 

print("F array : \n", F)
print("C array : \n", C)

print("Ist F 'C continuous ? : ", F.flags['C_CONTIGUOUS'])
print("Ist C 'C continuous ? : ", C.flags['C_CONTIGUOUS'])
print("Ist C 'C continuous ? : ", C2.flags['C_CONTIGUOUS'])

            