import numpy as np

print(np.ones((3, 3), dtype='int'))
#
# print(np.identity(3))
#
# print(np.empty((3, 3)))

a = np.array([
    [3, 1],
    [1, 1]
], dtype=int)

a_inverse = np.linalg.inv(a)

c = np.array([
    5, 3
])

print(a_inverse.dot(c))

print(np.linalg.solve(a, c))

d = np.array([
    [0, -2],
    [4, 5]
], dtype=int)

print(d.T)

print(np.linalg.det(d))

print(np.sum(d))
print(np.min(d))
print(np.max(d))
print(np.mean(d))
print(np.median(d))
print(np.std(d))

print(np.mean(d, axis=1))

print(np.nan == np.nan)

print(np.isnan(np.nan))

div_by_zero = d / 0

print(div_by_zero)

from matplotlib import pyplot as plt

x = np.arange(5, 20, 0.0025)

y = (7 - ((x - 10) ** 2)) ** 0.5 + 10
_y = -(7 - ((x - 10) ** 2)) ** 0.5 + 10

plt.title('Sample Graph')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.plot([x, x], [y, _y])
plt.show()
