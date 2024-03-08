import pandas as pd

data = pd.read_csv('aluguel.csv', sep=';')

s = pd.Series(list('asdadeadesdasesda'))
print(s)

print(s.unique())
print(s.value_counts())

types = data.Tipo.unique()
print(types)

how_many_types = data.Tipo.value_counts()
print(how_many_types)
