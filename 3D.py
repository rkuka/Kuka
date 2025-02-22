import numpy as up
import matplotlib.pyplot as pt

date = up.random.randint(0,100,size=[40,40])
x, y, z = date[0], date[1], date[2]

ax = pt.subplot(projection='3d')

ax.scatter(x[:10], y[:10], z[:10], c='b')
ax.scatter(x[10:20], y[10:20], z[10:20], c='r')
ax.scatter(x[30:40], y[30:40], z[30:40], c='g')


pt.show()