from numpy import array, identity
from numpy.linalg import inv, det
from itertools import permutations
from rotations import rotations

#tetrahedron vertices
v = [[-1., 1., 1.], [1., -1., 1.], [1., 1., -1.], [-1., -1., -1.]]

#compute big (including reflections) and small tetrahedral groups
m = inv(array(v[:-1]).T)
btgr = [array(p[:-1]).T@m for p in permutations(v)]
stgr = [m for m in btgr if det(m) > 0]

#big and small octahedral groups
o = -identity(3)
bogr = btgr + [o@m for m in btgr]
sogr = [m for m in bogr if det(m) > 0]

#big and small icosahedral groups
sigr = [r@s for r in rotations for s in stgr]
bigr = sigr + [o@m for m in sigr]
