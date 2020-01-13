import numpy as np 

kalorientabelle = np.array([30,52,88,36,86,160,375,115,43,71])
jouletabelle = kalorientabelle * 4.1868
print(jouletabelle)
print('--------------------------------------------------')

# Nachkomma entfernen
jouletabelle = np.round((kalorientabelle*4.1868),0)
print(jouletabelle)
print('--------------------------------------------------')

# in Integer umwandeln
jouletabelle = jouletabelle.astype(np.int16)
print(jouletabelle)
print('--------------------------------------------------')

verzehr_in_gramm = np.array([240,95,135,120,200,160,290,450,500,0])
verzehr_in_kg = verzehr_in_gramm / 1000
print(verzehr_in_kg)

# Diät, 10 % weniger essen:
reduzierter_verzehr_in_kg = verzehr_in_kg * 0.9
print(reduzierter_verzehr_in_kg)