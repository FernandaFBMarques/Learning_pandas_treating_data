import pandas as pd

data = pd.read_csv('residential_rent.csv', sep=';')

print(data[data['Valor'].isnull()])

A = data.shape[0]
data.dropna(subset=['Valor'])
B = data.shape[0]
print(A-B)