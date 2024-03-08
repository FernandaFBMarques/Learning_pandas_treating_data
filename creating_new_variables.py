import pandas as pd

data = pd.read_csv('residential_rent.csv', sep=';')
print(data.head(10))

data['Valor Bruto'] = data['Valor'] + data['Condominio'] + data['IPTU']
print(data.head(10))

data['Valor m2'] = (data['Valor']/data['Area']).round(2)
print(data.head(10))

data['Valor Bruto m2'] = (data['Valor Bruto']/data['Area']).round(2)

casa = ['Casa', 'Casa de Condomínio', 'Casa de Vila']
data['Tipo Agregado'] = data['Tipo'].apply(lambda x: 'Casa' if x in casa else 'Apartamento')
print(data.head(10))

# Deleating variables
data_aux = pd.DataFrame(data[['Tipo Agregado', 'Valor m2', 'Valor Bruto', 'Valor Bruto m2']])
print(data_aux.head(10))

# del data_aux['Valor Bruto']
# print(data_aux.head(10))

# data_aux.pop('Valor Bruto m2')
# print(data_aux.head(10))

data.drop(['Valor Bruto', 'Valor Bruto m2'], axis=1, inplace=True)
print(data_aux.head(10))

data.to_csv('residential_rent.csv', sep=';', index=False)
