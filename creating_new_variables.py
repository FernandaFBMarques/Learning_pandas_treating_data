import pandas as pd

data = pd.read_csv('residential_rent.csv', sep=';')
print(data.head(10))

data['Valor Bruto'] = data['Valor'] + data['Condominio'] + data['IPTU']
print(data.head(10))

data['Valor m2'] = (data['Valor']/data['Area']).round(2)
print(data.head(10))

casa = ['Casa', 'Casa de Condomínio', 'Casa de Vila']
data['Tipo Agregado'] = data['Tipo'].apply(lambda x: 'Casa' if x in casa else 'Apartamento')
print(data.head(10))
