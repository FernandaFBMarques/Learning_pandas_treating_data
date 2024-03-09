import pandas as pd

prices = pd.DataFrame([['Street Market', 'Onion', 2.5],
                       ['Market', 'Onion', 1.99],
                       ['Supermarket', 'Onion', 1.69],
                       ['Street Market', 'Tomato', 4],
                       ['Market', 'Tomato', 3.29],
                       ['Supermercado', 'Tomato', 2.99],
                       ['Street Market', 'Potato', 4.2],
                       ['Market', 'Potato', 3.99],
                       ['Supermarket', 'Potato', 3.69]],
                      columns=['Place', 'Product', 'Price'])

products = prices.groupby('Product')
print(products.describe().round(2))

statistics = ['mean', 'std', 'min', 'max']
names = {'mean': 'Mean', 'std': 'Standard Deviation', 'min': 'Minimum', 'max': 'Maximum'}
print(products['Price'].aggregate(statistics).rename(columns=names).round(2))
