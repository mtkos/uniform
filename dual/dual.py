#!/usr/bin/python3
from numpy import array, dot
from numpy.linalg import det
from tempfile import NamedTemporaryFile
import open3d
from fileinput import input
from sys import argv, path

path.append('../utils')

from phi import phi
from group import stgr, btgr, sogr, bogr, sigr, bigr

def make_triangle(vertex, n1, n2):
    return [vertex, n1*dot(vertex, vertex)/dot(n1, vertex), n2*dot(vertex, vertex)/dot(n2, vertex)]

def write_triangle(triangle, color, f):
    for v in triangle:
        print(*v, *color, file = f)

groups = {'stgr':stgr, 'btgr':btgr, 'sogr':sogr, 'bogr':bogr, 'sigr':sigr, 'bigr':bigr, }

lines = list(input(files = argv[1]))

n_normals = eval(lines[0])
normals = [array(eval(lines[i])) for i in range(1, 1 + n_normals)]
color = eval(lines[1 + n_normals])
vertex = array(eval(lines[2 + n_normals]))
group = groups[lines[3 + n_normals][:-1]] #remove trailing newline
ntriangles = n_normals*len(group)

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

for i in range(n_normals):
    triangle = make_triangle(vertex, normals[i - 1], normals[i])
    for g in group:
        t = [g@v for v in triangle]
        if det(g) < 0:
            t.reverse()
        write_triangle(t, color, f)

index = 0
for i in range(ntriangles):
    print(3, *range(index, index + 3), file = f)
    index += 3

f.close()

mesh = open3d.io.read_triangle_mesh(f.name)
mesh.compute_vertex_normals()
open3d.visualization.draw_geometries([mesh], mesh_show_wireframe = False, window_name = argv[1])
