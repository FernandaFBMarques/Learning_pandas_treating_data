import pandas as pd

data_ = pd.read_csv('aluguel.csv', sep=';')

type(data_)  # mostra que a variavel data_ eh do tipo DataFrame
data_.info()  # esse eh um metdo de DataFrame

data_.head()  # printa so os 5 primeiros
data_.head(10)  # printa so os 10 primeiros
