import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('residential_rent.csv', sep=';')

plt.rc('figure', figsize=(14, 6))

print(data[data['Valor'] >= 500000])

value = data['Valor']
Q1 = value.quantile(.25)
Q3 = value.quantile(.75)
IIQ = Q3 - Q1
lower_limit = Q1 - 1.5 * IIQ
upper_limit = Q3 + 1.5 * IIQ

selection = (value >= lower_limit) & (value <= upper_limit)
new_data = data[selection]
new_data.boxplot(['Valor'])

data.hist(['Valor'])
new_data.hist(['Valor'])

plt.show()
