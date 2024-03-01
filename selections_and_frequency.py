# AULA 5
# Selection and Frequency

# atalho = ctrl + /

# Select properties with an area between 60 and 100 square meters, including the limits
# Select properties with at least 4 bedrooms and with rent less than R$ 2,000.00

import pandas as pd

data = pd.read_csv('aluguel.csv', sep=';')
print(data.head(10))

# Select only properties classified as 'Apartamento':
selection = data['Tipo'] == 'Apartamento'
n1 = data[selection].shape[0]

# Select properties classified as 'Casa', 'Casa de Condomínio' and 'Casa de Vila'
selection = (data['Tipo'] == 'Casa') | (data['Tipo'] == 'Casa de Condomínio') | (data['Tipo'] == 'Casa de Vila')
n2 = data[selection].shape[0]
