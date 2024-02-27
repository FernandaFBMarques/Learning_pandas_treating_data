import pandas as pd

data_ = pd.read_csv('aluguel.csv', sep=';')

print(data_.head(10))

real_estate_type = data_['Tipo']  # serve para selecionar a variavel desejada

# verifica o tipo da variavel
print(type(real_estate_type))

# agrupa todos os tipos de imoveis que tem na Series
# so coleta primeiro item de cada tipo
# o argumento inplace faz com que a modificação seja feita direto na variavel
real_estate_type.drop_duplicates(inplace=True)

print(real_estate_type)
