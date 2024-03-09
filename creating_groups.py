import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('residential_rent.csv', sep=';')
print(data.head(10))

mean_value = data['Valor'].mean()
print(mean_value)

neighborhoods = ['Barra da Tijuca', 'Copacabana', 'Ipanema', 'Leblon', 'Botafogo', 'Flamengo', 'Tijuca']
selection = data['Bairro'].isin(neighborhoods)
data = data[selection]
print(data.head(10))

print(data['Bairro'].drop_duplicates())

groups_neighborhoods = data.groupby('Bairro')

for neighborhoods, data in groups_neighborhoods:
    print(neighborhoods)


for neighborhoods, data in groups_neighborhoods:
    print('{} -> {}'.format(neighborhoods, data.Valor.mean()))

groups_neighborhoods_mean = groups_neighborhoods['Valor'].mean()
print(groups_neighborhoods_mean)

groups_neighborhoods_mean = groups_neighborhoods[['Valor', 'Condominio']].mean().round(2)
print(groups_neighborhoods_mean)

print(groups_neighborhoods['Valor'].describe().round(2))

print(groups_neighborhoods['Valor'].aggregate(['min', 'max', 'sum']).rename(columns={'min': 'Minimum',
                                                                                     'max': 'Maximum',
                                                                                     'sum': 'Sum'}))

plt.rc('figure', figsize=(20, 10))
fig = groups_neighborhoods['Valor'].std().plot.bar(color='blue')
fig.set_ylabel('Rent Value')
fig.set_title('Rent Value by Neighborhood', {'fontsize': 22})
plt.show()

fig2 = groups_neighborhoods['Valor'].mean().plot.bar(color='orange')
fig2.set_ylabel('Rent Value')
fig2.set_title('Average Rent Value by Neighborhood', {'fontsize': 22})
plt.show()
