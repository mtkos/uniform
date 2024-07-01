#!/usr/bin/python3
from sympy import init_printing, sqrt, Matrix, to_number_field, pi, symbols, solve, pprint, Integer, simplify
from rotations import rot, rotations
from fileinput import input
from sys import argv

init_printing(use_unicode=True)

phi = (1 + sqrt(5))/2

def to_str(x):
    return to_number_field(x, phi, alias = symbols('phi'))

lines = list(input(files = argv[1]))

k = Matrix(eval(lines[0]))
theta = -2*pi/eval(lines[1])
R1 = rot(k, theta)

k = Matrix(eval(lines[2]))
theta = 2*pi/eval(lines[3])
R2 = rot(k, theta)

x, y = symbols('x,y')
z = eval(lines[4])

p = Matrix([x, y, z])
p1 = R1*p
p2 = R2*p

s = (solve(p1 - p2, x, y))

print()

vertex = Matrix([simplify(s[x]), simplify(s[y]), simplify(z)])
for r in rotations:
    v = r*vertex
    for i in range(3):
        v[i] = to_str(v[i])
    pprint(v)
    print()

edge = R1*vertex - vertex

for i in range(3):
    edge[i] = simplify(edge[i])

print('square edge length: ')
pprint(to_str(edge.dot(edge)))
