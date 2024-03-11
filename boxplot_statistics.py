import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('aluguel_amostra.csv', sep=';')

plt.rc('figure', figsize=(14, 6))
print(data[data['Valor'] >= 500000])

data.boxplot(['Valor'], by=['Tipo'])
group_type = data.groupby('Tipo')['Valor']

Q1 = group_type.quantile(.25)
Q3 = group_type.quantile(.75)
IIQ = Q3 - Q1
lower_limit = Q1 - 1.5 * IIQ
upper_limit = Q3 + 1.5 * IIQ

print(upper_limit['Apartamento'])

for tipo in group_type.groups.keys():
    print(tipo)

data_new = pd.DataFrame()
for tipo in group_type.groups.keys():
    is_type = data['Tipo'] == tipo
    is_inside_of_limit = (data['Valor'] >= lower_limit[tipo]) & (data['Valor'] <= upper_limit[tipo])
    selection = is_type & is_inside_of_limit
    print(data[selection])
    data_selection = data[selection]
    data_new = pd.concat([data_new, data_selection])

print(data_new)
data_new.boxplot(['Valor'], by=['Tipo'])
data_new.to_csv('residential_rent_without_outliers.csv', sep=';', index=False)
