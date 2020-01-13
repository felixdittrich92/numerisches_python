import numpy as np

print('--------Spaltennamen ändern--------')

dt = np.dtype([('country',np.unicode, 25),  
               ('density','i4'),
               ('area','i4'),
               ('population','i4')])

population_table = np.loadtxt('population_table.csv', delimiter=';', dtype=dt)

print(population_table.dtype.names)
print('---------------------------')
population_table.dtype.names = ('Land', 'Bevölkerungsdichte', 'Fläche', 'Bevölkerung')
print(population_table.dtype.names)
print('---------------------------')
print(population_table['Land'])

print('--------Spaltenwerte ändern--------')

lands = ['Niederlande','Belgien','Vereinigtes Königreich',
         'Deutschland','Liechtenstein','Italien','Schweiz',
         'Luxemburg','Frankreich','Österreich','Griechenland',
         'Irland','Schweden','Finnland','Norwegen']

population_table['Land'] = np.array(lands)
print(population_table)
