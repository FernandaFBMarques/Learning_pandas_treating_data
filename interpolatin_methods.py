import pandas as pd

data = [0.5, None, None, 0.52, 0.54, None, None, 0.59, 0.6, None, 0.7]
s = pd.Series(data)

print(s)
print(s.fillna(0))

# option 2:
print(s.fillna(s.bfill()))

# option 3:
print(s.fillna(s.mean()))

# option 4:
print(s.ffill(limit=2))

# option 5:
s1 = s.ffill(limit=1)
s1 = s1.bfill(limit=1)
print(s1)
