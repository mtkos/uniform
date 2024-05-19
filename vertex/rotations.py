from sympy import sqrt, Matrix, eye, pi, sin, cos, simplify

def rot(k, theta):
    klength = sqrt(k[0]**2 + k[1]**2 + k[2]**2)
    k = k/klength
    K = Matrix([[0, -k[2], k[1]], [k[2], 0, -k[0]], [-k[1], k[0], 0]])
    I = eye(3)
    return I + sin(theta)*K + (1 - cos(theta))*K**2

phi = (1 + sqrt(5))/2

rot5 = rot(Matrix([0, phi, 1]), 2*pi/5)
rotations = [simplify(rot5**i) for i in range(5)]
