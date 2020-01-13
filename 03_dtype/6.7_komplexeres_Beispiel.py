import pickle

# pickle entpacken
fh = open("cities_and_times.pkl", 'br')
cities_and_times = pickle.load(fh)

for i in range(5):
    print(cities_and_times[i])

# umwandeln in strukturiertes Array
time_type = np.dtype([('city', 'U30'), 
                      ('day', 'U3'), 
                      ('time', [('h', int), ('min', int)])]])
                    
times = np.array(cities_and_times, dtype=time_type)
print(times[:4])

lst = []

for row in times:
    t = row[2]
    t = f'{t[0]:02d}:{t[1]:02d}'
    lst.append((row[0], row[1], t))

time_type = np.dtype([('city', 'U30'), 
                      ('day', 'U3'), 
                      ('time', 'U5')])

times2 = np.array(times[:10])

# in Datei schreiben
with open("cities_and_times.csv", "w") as fh:
    for city_data in times2:
        fh.write(",".join(city_data) + "\n")