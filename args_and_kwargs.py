def test_func(*args, **kwargs):
    print(args)
    print(kwargs)


def another_test(a, b):
    print('a is ', a)
    print('b is ', b)


# another_test(b=5, a=3)
# another_test(5, 3)

# test_func(4, 5, 6, 'Ram', a=5, b=6, c=7)

import numpy as np

rand_array = np.random.randn(100).reshape((10, 10))
# np.savetxt('rand_array.txt', rand_array)
another_array = np.loadtxt('rand_array.txt')

a = np.array([
    [3, 2],
    [4, 1]
])

b = np.array([
    [3, 2],
    [4, 1.001]
])

print(np.allclose(a, b, atol=0.0001))
