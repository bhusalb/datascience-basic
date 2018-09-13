import numpy as np
from matplotlib import pyplot as plt

# image = plt.imread('sd.png')
#
# print(image.ndim)
#
# image_inverse = np.linalg.inv(image[0:500, 0:500])
#
# # plt.imshow(image[70:550:2, 130:880:2])
#
# plt.imshow(image_inverse)
# plt.show()

# print(image)

# marks = np.array([90, 91, 92, 91, 92,95, 92, 99, 91, 99])
#
# plt.hist(marks)
#
# plt.show()
#


import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 10, 0.005)
y = np.exp(-x / 2.) * np.sin(2 * np.pi * x)

# np.savetxt('samplgffe.txt', x)


a = np.loadtxt('samplgffe.txt')

# fig, ax = plt.subplots()
# ax.plot(x, y)
# ax.set_xlim(0, 10)
# ax.set_ylim(-1, 1)
#
# xdata, ydata = 5, 0
# xdisplay, ydisplay = ax.transData.transform_point((xdata, ydata))
#
# bbox = dict(boxstyle="round", fc="0.8")
# arrowprops = dict(
#     arrowstyle="->",
#     connectionstyle="angle,angleA=0,angleB=90,rad=10")
#
# offset = 72
# ax.annotate('data = (%.1f, %.1f)' % (xdata, ydata),
#             (xdata, ydata), xytext=(-2 * offset, offset), textcoords='offset points',
#             bbox=bbox, arrowprops=arrowprops)
#
# disp = ax.annotate('display = (%.1f, %.1f)' % (xdisplay, ydisplay),
#                    (xdisplay, ydisplay), xytext=(0.5 * offset, -offset),
#                    xycoords='figure pixels',
#                    textcoords='offset points',
#                    bbox=bbox, arrowprops=arrowprops)
#
# plt.show()
