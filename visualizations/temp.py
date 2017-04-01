'''
Created on Feb 6, 2017

@author: Angel
'''

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # @UnusedImport

nsize = 300
X = [1, 0]
Y = [2, 0]
Z = [0, 0]
#create scatter plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(X, Y, Z, color='gray', marker='s')

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.show()