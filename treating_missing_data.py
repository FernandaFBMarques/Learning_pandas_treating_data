import pandas as pd

data = pd.read_csv('residential_rent.csv', sep=';')

print(data[data['Valor'].isnull()])

A = data.shape[0]
data.dropna(subset=['Valor'])
B = data.shape[0]
print(A-B)

print(data[data['Condominio'].isnull()].shape[0])

selection = (data['Tipo'] == 'Apartamento') & (data['Condominio'].isnull())

A = data.shape[0]
data = data[~selection]
B = data.shape[0]
print(A-B)

print(data[data['Condominio'].isnull()].shape[0])

data.fillna(0, inplace=True)
# Option 2: data = data.fillna({'Condominio': 0, 'IPTU': 0})
print(data.info())

data.to_csv('residential_rent.csv', sep=';', index=False)
