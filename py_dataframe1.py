import pandas as pd

data = {
    'apples': [3, 2, 0, 1],
    'oranges': [0, 3, 7, 2]
}
purchase = pd.DataFrame(data, index=['June', 'Robert', 'Lily', 'David'])
print(purchase.loc['Robert'])
