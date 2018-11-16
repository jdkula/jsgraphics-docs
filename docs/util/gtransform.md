GTransform
===========
This class represents an affine transformation. Essentially, it's a 2 by 2 matrix,
plus two fields for an \(x\) and \(y\) transformation.

Applying such a transformation multiplies the vector field
that makes up a given [GObject](../gobject.md) by
$$
\begin{bmatrix}
a & b \\
c & d
\end{bmatrix}
$$
...then transforms the space by \((tx, ty)\).

This class is not intended to be used directly. Every [GObject](../gobject.md) contains one,
and its properties may be updated using methods like [GObject::shear](../gobject.md#shear),
etc.

Factory Methods
----------------
*function* @d.GTransform()
:   Creates a new GTransform with the identity matrix, i.e.
    $$
        \begin{bmatrix}
        1 & 0 \\
        0 & 1
        \end{bmatrix}
    $$
    and no transform.

*function* @d.GTransform(transform)
:   Creates a new GTransform that's a copy of the passed-in @p.transform.

*function* @d.GTransform(a, b, c, d[, tx=0, ty=0])
:   Creates a new GTransform with the following matrix:
    $$
        \begin{bmatrix}
        a & b \\
        c & d
        \end{bmatrix}
    $$
    @p.tx and @p.ty can also be specified in the constructor, but default to 0,0.

Fields
-------
GTransform::@d.a
: 

GTransform::@d.b
: 

GTransform::@d.c
: 

GTransform::@d.d
:   The matrix values \(a\), \(b\), \(c\), and \(d\), respectively.

GTransform::@d.tx
: 

GTransform::@d.ty
:   The \(x\) and \(y\) transform values, respectively.