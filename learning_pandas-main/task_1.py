"""
1. Прочесть с помощью pandas файл
california_housing_test.csv, который находится в папке
sample_data
2. Посмотреть сколько в нем строк и столбцов
3. Определить какой тип данных имеют столбцы
"""

from pandas import read_csv
data = read_csv("california_housing_test.csv")

print(type(data))
print()

print(data.shape)
print()

print(data.dtypes)
print()

print(data.info())
print()

print(data.describe())