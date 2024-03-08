import pandas as pd

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
