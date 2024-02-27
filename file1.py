# AULA 03

import pandas as pd

data_ = pd.read_csv('aluguel.csv', sep=';')

print(data_.head(10))

real_estate_type = data_['Tipo']  # serve para selecionar a variavel desejada

# verifica o tipo da variavel
print(type(real_estate_type))
# real_estate_type eh uma variavel do tipo Series

# agrupa todos os tipos de imoveis que tem na Series
# so coleta primeiro item de cada tipo
# o argumento inplace faz com que a modificação seja feita direto na variavel
real_estate_type.drop_duplicates(inplace=True)

print(real_estate_type)


# Structuring the visualization

real_estate_type = pd.DataFrame(real_estate_type)

# aplicacao do indice numerado
real_estate_type.index = range(real_estate_type.shape[0])

# nomeando a 1a coluna de id
real_estate_type.columns.name = 'id'
print(real_estate_type)
