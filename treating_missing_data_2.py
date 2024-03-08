import pandas as pd

real_estate = pd.DataFrame([['Apartment', None, 970, 68],
                            ['Apartment', 2000, 878, 112],
                            ['House', 5000, None, 500],
                            ['Apartment', None, 1010, 170],
                            ['Apartment', 1500, 850, None],
                            ['House', None, None, None],
                            ['Apartment', 2000, 878, None],
                            ['Apartment', 1550, None, 228],
                            ['Apartment', 2500, 880, 195]],
                           columns=['Type', 'Value', 'Condominium', 'Tax'])

real_estate.dropna(subset=['Value'], inplace=True)

real_estate = real_estate.fillna({'Condominium': 0, 'Tax': 0})

real_estate.index = range(real_estate.shape[0])
print(real_estate)
