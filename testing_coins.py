import pandas as pd

m1 = 'CCcCCccCCCccCcCccCcCcCCCcCCcccCCcCcCcCcccCCcCcccCc'
m2 = 'CCCCCccCccCcCCCCccCccccCccCccCCcCccCcCcCCcCccCccCc'
m3 = 'CccCCccCcCCCCCCCCCCcccCccCCCCCCccCCCcccCCCcCCcccCC'
m4 = 'cCCccCCccCCccCCccccCcCcCcCcCcCcCCCCccccCCCcCCcCCCC'
m5 = 'CCCcCcCcCcCCCcCCcCcCCccCcCCcccCccCCcCcCcCcCcccccCc'

events = {'m1': list(m1),
          'm2': list(m2),
          'm3': list(m3),
          'm4': list(m4),
          'm5': list(m5)}

coins = pd.DataFrame(events)
df = pd.DataFrame(data=['Head', 'Tails'], index=['c', 'C'], columns=['Faces'])
for item in coins:
    df = pd.concat([df, coins[item].value_counts()], axis=1)

print(df)
