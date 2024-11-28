import numpy as np


a = np.array([[1, 2, 0],
              [3, 1, -1],
              [0, 0, 0]])
b = np.array([[1, 0, 0],
              [2, 0, 0],
              [3, 0, 0]])
c = np.array([1, 3, 5, 7, 9])

"""Математические операции с матрицами"""
"""Умножение матриц"""
result = np.dot(a,b)
print (result)

"""Сложение матриц"""
result1 = a + b
print (result1)

"""Сортировка значений массива в сторону убывания и извлечение значения согласно требуемого индекса """

sorted = np.sort(c)[::-1]
print(sorted[3])




"""Построение графика линейной функции и кривой второго порядка"""

import matplotlib.pyplot as plt
import numpy as np


x = np.linspace(0, 20)
x_values = range(0,12, 2)
y1_values = []
y2_values = []
for i in x_values:
    y = i**2
    y1_values.append(y)
for i in x_values:
    y = -3*i + 3
    y2_values.append(y)

plt.plot(x_values,y1_values, label = 'First line' )
plt.plot(x_values,y2_values, label = 'Second line' )
plt.ylabel('Значения оси Y')
plt.xlabel('Значения оси X')
plt.title('Простые графики')
plt.legend(title = 'List lines')
plt.show()

