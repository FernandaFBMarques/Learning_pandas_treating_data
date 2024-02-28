# REPORT III

import pandas as pd

data = pd.read_csv('aluguel.csv', sep=';')

#  data visualization:
print(data.head(10))

print(list(data['Tipo'].drop_duplicates()))

# is the output of the last print with only the ones I need
residential = ['Quitinete', 'Casa', 'Apartamento', 'Casa de Condomínio', 'Casa de Vila']

# the output will have True on the list's elements that are in the DataFrame
print(data['Tipo'].isin(residential).head(10))

selection = data['Tipo'].isin(residential)

residential_data = data[selection]

list(residential_data['Tipo'].drop_duplicates())

dataFrame_len = residential_data.shape[0]
residential_data.index = range(dataFrame_len)
print(residential_data.index)
