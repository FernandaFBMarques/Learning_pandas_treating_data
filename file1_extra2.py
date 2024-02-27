# AULA 3 EXTRA 2
# Concatenating DataFrames

import pandas as pd

# option 1
data = [[1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]]

index = ['Row' + str(i) for i in range(3)]
df1 = pd.DataFrame(data=data, index=index)
print(df1)

columns = ['Column' + str(i) for i in range(3)]
df2 = pd.DataFrame(data=data, index=index, columns=columns)
print(df2)

# option 2
data2 = {'Column1': {'Row0': 1, 'Row1': 4, 'Row2': 7},
         'Column2': {'Row0': 2, 'Row1': 5, 'Row2': 8},
         'Column3': {'Row0': 3, 'Row1': 6, 'Row2': 9}}

# option 3
data3 = [(1, 2, 3),
         (4, 5, 6),
         (7, 8, 9)]

df3 = pd.DataFrame(data=data3, index=index, columns=columns)
print(df3)

df1[df1 > 0] = 'A'
df2[df2 > 0] = 'B'
df3[df3 > 0] = 'C'

df4 = pd.concat([df1, df2, df3])
print(df4)

# connection by the rows
df5 = pd.concat([df1, df2, df3], axis=1)
print(df5)
