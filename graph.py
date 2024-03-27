import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Set up the figure and 3D axis
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Data for a three-dimensional line
zline = np.linspace(0, 15, 1000)
xline = np.sin(zline)
yline = np.cos(zline)
ax.plot3D(xline, yline, zline, 'gray')

# Data for three-dimensional scattered points
zscatter = 15 * np.random.random(100)
xscatter = np.sin(zscatter) + 0.1 * np.random.randn(100)
yscatter = np.cos(zscatter) + 0.1 * np.random.randn(100)
ax.scatter3D(xscatter, yscatter, zscatter, c=zscatter, cmap='Greens')

plt.show()
