## coordinates for uniform star polyhedra

This map contains two small Python programs to compute exact (not numerical approximations) coordinates for the vertices of a number of uniform star polyhedra. To be precise: the non-snub ones.
See the Wikipedia page <https://en.wikipedia.org/wiki/Uniform_star_polyhedron>. The motivation is that it is much simpler to 'see' the symmetry axes of these polyhedra than the (coordinates of) the
vertices. From the symmetry axes of adjacent faces, together with the corresponding rotation angles, a vertex can be computed by solving a linear equation. This vertex is determined up to a scalar
multiple of course. This multiple is determined by specifying the z-coordinate for the vertex (so we always take care that it is non-zero). This is done in such a way that the resulting coordinates
can be easily compared to those given on Wikipedia. In case of octahedral (or tetrahedral) symmetry the coordinates of the remaining vertices can be found by permuting and negating the coordinates
of a single vertex. In case of icosahedral symmetry we compute four additional vertices, obtained from the first one by succesive rotations over $2\pi/5$ around the axis $(0, \phi, 1)$. The 
remaining vertices can be found again by permuting and negating coordinates.

The cases of octahedral (including tetrahedral) and icosahedral symmetry are treated by two different programs. The reason for this being that in the icohedral case we pretty print the coordinates in
terms of the golden ratio. In the octahedral case we need $\sqrt2$. Having them in one program makes things unnecessarily complicated.

The input to both programs consists of five lines: a symmetry axis, a (possibly fractional) number n denoting n-fold symmetry, a second symmetry axis and symmetry number, and, finally, a
z-coordinate. Input files have been prepared for the platonic solids, the archimedean solids, the Kepler-Poinsot polyhedra and the remaining non-snub star polyhedra. The naming scheme is,
hopefully, self-explanatory. The programs octa.py and icosa.py expect a file name as argument
