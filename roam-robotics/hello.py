import numpy as np
import matplotlib.pyplot as plt

col_1 = 87;
col_2 = 130;

data = np.genfromtxt('data.txt', usecols=(col_1-1, col_2-1),
  invalid_raise=False)

y_1_pre = data[:, 0]
y_2_pre = data[:, 1]

y_1_long = [];
y_2_long = [];

for num in y_1_pre:
  if num > 10:
    continue
  if num < -10:
    continue
  y_1_long.append(num)

for num in y_2_pre:
  if num > 10:
    continue
  if num < -10:
    continue
  y_2_long.append(num)

row_num_1 = np.arange(len(y_1_long))
row_num_2 = np.arange(len(y_2_long))

y_1_s = np.array(y_1_long)
y_2_s = np.array(y_2_long)

y_1 = y_1_s[:143000]
y_2 = y_2_s[:143000]


# plt.scatter(row_num_1, y_1, c='blue', label='Col 87', alpha=0.3, edgecolors='none')
# plt.scatter(row_num_2, y_2, c='orange', label='Col 130', alpha=0.3, edgecolors='none')

# plt.plot(y_1, c='blue', label='Col 87')
# plt.plot(y_2, c='orange', label='Col 130')

# plt.legend(loc=1)
# plt.xlabel('Row Num')
# plt.ylabel('Value')


plt.plot(y_1, y_2)

plt.xlabel('Col 87')
plt.ylabel('Col 130')


plt.show()
