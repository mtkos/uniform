from numpy import sqrt, dot, array, identity, sin, cos, pi
from numpy.linalg import matrix_power
from phi import phi

# rotation around axis k through angle theta, using Rodrigues' formula

def rot(k, theta):
    klength = sqrt(dot(k, k))
    k = k/klength
    K = array([[0, -k[2], k[1]], [k[2], 0, -k[0]], [-k[1], k[0], 0]])
    I = identity(3)
    return I + sin(theta)*K + (1 - cos(theta))*K@K

k = array([1., 0., phi])
theta = 2.*pi/5.

m1 = rot(k, theta)
rotations = [matrix_power(m1, i) for i in range(5)]
