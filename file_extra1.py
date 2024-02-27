# AULA 1 EXTRA DA AULA 03
# Creating Data Structures

import pandas as pd

data = {'Row' + str(i): i + 1 for i in range(5)}

s = pd.Series(data)
print(s)

# posso fazer operacoes

s1 = s + 2
print(s1)

s2 = s + s1
print(s2)
