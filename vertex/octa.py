#!/usr/bin/python3
from sympy import init_printing, Matrix, pi, symbols, solve, pprint, simplify, sqrt, Integer
from rotations import rot
from fileinput import input
from sys import argv

init_printing(use_unicode=True)

lines = list(input(files = argv[1]))

k = Matrix(eval(lines[0]))
theta = -2*pi/eval(lines[1])
R1 = rot(k, theta)

k = Matrix(eval(lines[2]))
theta = 2*pi/eval(lines[3])
R2 = rot(k, theta)

x, y = symbols('x,y')
z = eval(lines[4])
print()

p = Matrix([x, y, z])
p1 = R1*p
p2 = R2*p

s = (solve(p1 - p2, x, y))

vertex = Matrix([simplify(s[x]), simplify(s[y]), z])
pprint(vertex)

edge = simplify(vertex - R1*vertex)
print('square edge length:', end = ' ')
pprint(simplify(edge.dot(edge)))
