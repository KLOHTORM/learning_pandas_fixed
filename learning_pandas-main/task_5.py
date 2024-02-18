"""
Написать EDA для датасета про пингвинов
Необходимо:
1. Использовать 2-3 точечных графика
2. Применить доп измерение в точечных графиках, используя
аргументы hue, size, stile
3. Использовать PairGrid с типом графика на ваш выбор
4. Изобразить Heatmap
5. Использовать 2-3 гистограммы

Чтобы подключить датасет с
пингвинами, воспользуйтесь данным
скриптом:
penguins = sns.load_dataset("penguins")
penguins.head()
"""

from seaborn import  load_dataset, scatterplot
from matplotlib.pyplot import show
data = load_dataset('penguins')

#1. scatterplot(data=data, x='flipper_length_mm', y='body_mass_g')
scatterplot(data=data, x='flipper_length_mm', y='body_mass_g', hue='sex', size='island', style='island')

show()