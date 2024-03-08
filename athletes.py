import pandas as pd

athletes = pd.DataFrame([['Marcos', 9.62], ['Pedro', None], ['João', 9.69],
                        ['Beto', 9.72], ['Sandro', None], ['Denis', 9.69],
                        ['Ary', None], ['Carlos', 9.74]],
                        columns=['Runner', 'Best Time'])
print(athletes)

athletes.fillna(athletes["Best Time"].mean(), inplace=True)
print(athletes)
