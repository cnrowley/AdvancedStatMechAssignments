import numpy as np
import matplotlib.pyplot as plt

from scipy.stats import gaussian_kde
import sys

def density_estimation(m1, m2):
    X, Y = np.mgrid[-180:180:5, -180:180:5]
    positions = np.vstack([X.ravel(), Y.ravel()])
    values = np.vstack([m1, m2])
    kernel = gaussian_kde(values)
    Z = np.reshape(kernel(positions).T, X.shape)
    return X, Y, Z

series=np.genfromtxt(sys.argv[1])
X, Y, Z = density_estimation(series[:,1], series[:,2])
print(np.amax(Z))
fig, ax = plt.subplots()
ax.scatter(series[:,1], series[:,2], marker='.', s=1, color='red')
plt.contour(X, Y, Z, levels=[0.0001, 0.0002, 0.0003, 0.0004, 0.0005])
plt.show()

ax.set(xlim=(-180,180), ylim=(-180,180), xlabel=r'$\phi (^\circ)$', ylabel=r'$\psi (^\circ)$')

plt.show()
plt.savefig(sys.argv[2])
plt.savefig(sys.argv[2][-4:] + '.png')

