import pandas as pd

data = pd.read_csv('residential_rent.csv', sep=';')
print(data.head(10))

class_ = [0, 2, 4, 6, 100]

# rooms = pd.cut(data.Quartos, class_)
# pd.Series(rooms).value_counts()

# ( intervalo é aberto
# [ intervalo é fechado

labels = ['1 e 2 rooms', '3 e 4 rooms', '5 e 6 rooms', '7 rooms or more']
rooms = pd.cut(data.Quartos, class_, labels=labels, include_lowest=True)
print(pd.Series(rooms).value_counts())
