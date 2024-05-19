#!/usr/bin/python3
from numpy import array, dot, pi
from numpy.linalg import det, matrix_power
from tempfile import NamedTemporaryFile
import open3d
from fileinput import input
from sys import argv, path

path.append('../utils')

from phi import phi
from rotations import rot
from group import stgr, btgr, sogr, bogr, sigr, bigr

def make_triangle(vertex, axis, rotation):
    return [vertex, rotation@vertex, axis*dot(axis, vertex)/dot(axis, axis)]

def write_triangle(triangle, color, f):
    for v in triangle:
        print(*v, *color, file = f)

groups = {'stgr':stgr, 'btgr':btgr, 'sogr':sogr, 'bogr':bogr, 'sigr':sigr, 'bigr':bigr}

lines = list(input(files = argv[1]))

n_axes = eval(lines[0])
axes = [array(eval(lines[i])) for i in range(1, n_axes + 1)]
mult = [eval(lines[i]) for i in range(1 + n_axes, 1 + 2*n_axes)]
theta = [2.*pi/eval(lines[i]) for i in range(1 + 2*n_axes, 1 + 3*n_axes)]
R = [rot(x, y) for x, y in zip(axes, theta)]
colors = [eval(lines[i]) for i in range(1 + 3*n_axes, 1 + 4*n_axes)]
vertex = array(eval(lines[1 + 4*n_axes]))
group = groups[lines[2 + 4*n_axes][:-1]] #remove trailing newline
ntriangles = 0
for x in mult:
    ntriangles += x*len(group)

f = NamedTemporaryFile(mode = 'w', encoding = 'ascii', suffix = '.ply', delete = False)
f.write('''ply
format ascii 1.0
element vertex {}
property float32 x
property float32 y
property float32 z
property uchar red
property uchar green
property uchar blue
element face {}
property list uint8 int32 vertex_index
end_header\n'''.format(3*ntriangles, ntriangles))

for x, y, z, u in zip(axes, R, colors, mult):
    for w in range(u):
        triangle = make_triangle(matrix_power(y, w)@vertex, x, y)
        for r in group:
            t = [r@v for v in triangle]
            if det(r) < 0:
                t.reverse()
            write_triangle(t, z, f)

index = 0
for i in range(ntriangles):
    print(3, *range(index, index + 3), file = f)
    index += 3

f.close()

mesh = open3d.io.read_triangle_mesh(f.name)
mesh.compute_vertex_normals()
open3d.visualization.draw_geometries([mesh], mesh_show_wireframe = False, window_name = argv[1])
