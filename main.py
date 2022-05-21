import numpy as np
import pandas as pd
import random

# dict = {
#     "country": ["Brazil", "Russia", "India", "China", "South Africa"],
#     "capital": ["Brasilia", "Moscow", "New Dehli", "Beijing", "Pretoria"],
#     "area": [8.516, 17.10, 3.286, 9.597, 1.221],
#     "population": [200.4, 143.5, 1252, 1357, 52.98] 
#        }

# brics = pd.DataFrame(dict)
# print(brics)

# tabelka = pd.read_csv('tabelka.csv')
# print(tabelka)
# print('tabelka csv--------')
# print(type(tabelka))

# print('--------')

# dates = pd.date_range("20130101", periods=10)
# print(dates)

# df = pd.DataFrame(np.random.randn(10, 4), index=dates, columns=list("ABCD"))
# print(df)

# df2 = pd.DataFrame(
#     {
#         "A": 1.0,
#         "B": pd.Timestamp("20130102"),
#         "C": pd.Series(1, index=list(range(4)), dtype="float32"),
#         "D": np.array([3] * 4, dtype="int32"),
#         "E": pd.Categorical(["test", "train", "test", "train"]),
#         "F": "foo",
#     }
# )

# print(df2)
# print('numpy_sort:' , np.sort(tabelka))



# Create 2 new lists height and weight
# height = [1.87,  1.87, 1.82, 1.91, 1.90, 1.85]
# weight = [81.65, 97.52, 95.25, 92.98, 86.18, 88.45]

# # Create 2 numpy arrays from height and weight
# np_height = np.array(height)
# np_weight = np.array(weight)

# print(np_height)
# print(np.sort(np_height))
# print('--------')
# print(np_weight)
# print(np.sort(np_weight))

# con = np.concatenate((np_height,np_weight))
# print(np.sort(con))
# print(np.ceil(con))

# for i in range(100):
#     print('Errorr', random.randint(100,400), 'something went wrong')

prices = {
    'bananas': [2.99, 3.49, 5.99],
    'oranges': [4.15, 5.15, 6.05],
    'apples': [0.91, 1.43, 3.35]
}
print('---------------')
# prices = np.array({
#     'bananas': [2.99, 3.49, 5.99],
#     'oranges': [4.15, 5.15, 6.05],
#     'apples': [0.91, 1.43, 3.35]
# })

print(pd.DataFrame(prices).describe())


# srednia = pd.DataFrame(prices)

# print(np.mean(srednia))
# print(srednia)

# print(tabelka.to_string())

# print(tabelka)

# print(tabelka.tail(1))