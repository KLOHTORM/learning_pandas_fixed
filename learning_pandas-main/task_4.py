"""
1. Изобразите отношение households к population с
помощью точечного графика
2. Визуализировать longitude по отношения к
median_house_value, используя линейный график
3. Представить гистограмму по housing_median_age
4. Изобразить гистограмму по median_house_value с
оттенком housing_median_age
"""

from pandas import read_csv
from seaborn import scatterplot, relplot
from matplotlib.pyplot import show

data = read_csv("california_housing_test.csv")

#scatterplot(data=data, x='households', y='population')
relplot(data=data, x='longitude', y='median_house_value', kind='line')

show()