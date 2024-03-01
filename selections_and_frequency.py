# AULA 5
# Selection and Frequency

# atalho = ctrl + /

import pandas as pd

data = pd.read_csv('aluguel.csv', sep=';')

selection = data['Tipo'] == 'Apartamento'
n1 = data[selection].shape[0]  # .shape[0] makes it only keeps the True values

selection = (data['Tipo'] == 'Casa') | (data['Tipo'] == 'Casa de Condomínio') | (data['Tipo'] == 'Casa de Vila')
n2 = data[selection].shape[0]

selection = (data['Area'] >= 60) & (data['Area'] <= 100)
n3 = data[selection].shape[0]

selection = (data['Quartos'] >= 4) & (data['Valor'] < 2000)
n4 = data[selection].shape[0]

print("Number of properties classified as 'Apartamento' -> {}".format(n1))
print("Number of properties classified as 'Casa', 'Casa de Condomínio' and 'Casa de Vila' -> {}".format(n2))
print("Number of properties with an area between 60 and 100 square meters, including the limits -> {}".format(n3))
print("Number of properties with at least 4 bedrooms and with rent less than R$ 2,000.00 -> {}".format(n4))
