import numpy as np
import matplotlib.pyplot as plt

col_1 = 87;
col_2 = 130;

data = np.genfromtxt('data.txt', usecols=(col_1-1, col_2-1),
  invalid_raise=False)

y_1 = data[:, 0]
y_2 = data[:, 1]
row_num = np.arange(len(data))

plt.scatter(row_num, y_1, label='Col 87', alpha=0.3, edgecolors='none')
plt.scatter(row_num, y_2, label='Col 130', alpha=0.3, edgecolors='none')

plt.legend(loc=1)
plt.xlabel('Row Num')
plt.ylabel('Value')

plt.show()
