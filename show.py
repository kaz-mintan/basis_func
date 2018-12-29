import math
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import pyplot as plt
import numpy as np

array = np.zeros((3,3,3))
print(array)

array[0] = np.linspace(0,1,3)
array[1] = np.linspace(2,3,3)
array[2] = np.linspace(3,4,3)

fig = plt.figure()
ax = Axes3D(fig)
ax.scatter(array[0],array[1],array[2])

plt.show()
