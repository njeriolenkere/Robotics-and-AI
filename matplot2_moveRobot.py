#Move the robot to goal in a 1x1 grid size. Avoid osbtacles
#Ploting with matplotlib and numpy
import matplotlib.pyplot as plt
import numpy as np
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
#plot 1:
xpoints = np.array([0, 0, 0, 0, 0, 1, 2, 3])
ypoints = np.array([0, 1, 2, 3, 3, 3, 3, 3])
plt.plot(xpoints, ypoints)

#plot 2:
xpoints = np.array([0, 1, 2, 2, 3, 3, 3])
ypoints = np.array([0, 0, 0, 1, 1,  2, 3])
plt.plot(xpoints, ypoints)

#plot 3:
xpoints = np.array([0, 1, 2, 3, 3, 3, 3])
ypoints = np.array([0, 0, 0, 0, 1,  2, 3])
plt.plot(xpoints, ypoints)

#obstacls:
xpoints = np.array([1, 1, 2])
ypoints = np.array([1, 2, 2])
plt.scatter(xpoints, ypoints)

plt.show()

