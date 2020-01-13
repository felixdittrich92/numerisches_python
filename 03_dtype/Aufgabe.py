import numpy as np

print('------------------Aufgabe 1-----------------------')

# strukturiertes Array mit 2 Spalten ( ID int32) und Produktpreis
my_type = [('ID', np.int32), ('Preis', np.float64)]

produkte = np.array([(12345, 670.89),
                     (34567, 18.99),
                     (78900, 250.00),
                     (13579, 999.99)], dtype=my_type)
# ProduktIDs ausgeben
print(produkte['ID'])
# erste Zeile ausgeben
print(produkte[0])
# Artikelpreis in 3ten Zeile ausgeben
print(produkte[2]['Preis'])

print('------------------Aufgabe 2-----------------------')

# neues Array erzeugen
verkaufszahlen = np.array([3, 5, 2, 1])
# Einnahmen für jedes Produkt errechnen
erlöse = produkte['Preis'] * verkaufszahlen

# Ausgabe
print('Erlöse pro Produkt : ', erlöse)
print('Gesamterlös : ', erlöse.sum())

print('------------------Aufgabe 3,4 und 5-----------------------')

time_temp_type = np.dtype([('time', [('h',int), ('min',int), ('sec',int)]), 
                           ('temperature',float)])

# Array füllen und Struktur zuordnen
time_temp=np.array( [((11,42,17),20.8),
                     ((13,19,3),23.2),
                     ((14,50,29),24.6)],dtype=time_temp_type)

print(time_temp)
print(time_temp['time'])
print(time_temp['time']['h'])
print(time_temp['temperature'])

with open("time_temp.csv","w") as fh:
    for row in time_temp:
        zeit = [f"{el:02d}" for el in row[0]] 
        zeit = ":".join(zeit)
        fh.write(zeit+" "+str(row[1])+"\n")