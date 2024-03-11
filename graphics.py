import pandas as pd
import matplotlib.pyplot as plt

plt.rc('figure', figsize=(15, 8))

data = pd.read_csv('aluguel.csv', sep=';')
data.head()

area = plt.figure()
# 2 rows 2 columns in position 1
g1 = area.add_subplot(2, 2, 1)
g2 = area.add_subplot(2, 2, 2)
g3 = area.add_subplot(2, 2, 3)
g4 = area.add_subplot(2, 2, 4)

# scatterplot (grafico de dispersao)
g1.scatter(data.Valor, data.Area)
g1.set_title('Value X Area')

g2.hist(data.Valor)
g2.set_title('Histogram')

dados_g3 = data.Valor.sample(100)
dados_g3.index = range(dados_g3.shape[0])
g3.plot(dados_g3)
g3.set_title('Sample (Value)')

grupo = data.groupby('Tipo')['Valor']
label = grupo.mean().index
valores = grupo.mean().values
g4.bar(label, valores)
g4.set_title('Avarege Value per Type')

plt.show()

area.savefig('graphics.png', dpi=300, bbox_inches='tight')
