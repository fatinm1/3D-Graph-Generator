import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Function to prompt for integer input with a given prompt message
def input_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a valid integer.")

# Asking for user inputs
z_max = input_int("Enter the max value for z in the helix (e.g., 15): ")
num_points = input_int("Enter the number of scatter points (e.g., 100): ")

# Set up the figure and 3D axis
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Data for a three-dimensional line
zline = np.linspace(0, z_max, 1000)
xline = np.sin(zline)
yline = np.cos(zline)
ax.plot3D(xline, yline, zline, 'gray')

# Data for three-dimensional scattered points
zscatter = z_max * np.random.random(num_points)
xscatter = np.sin(zscatter) + 0.1 * np.random.randn(num_points)
yscatter = np.cos(zscatter) + 0.1 * np.random.randn(num_points)
ax.scatter3D(xscatter, yscatter, zscatter, c=zscatter, cmap='Greens')

plt.show()
