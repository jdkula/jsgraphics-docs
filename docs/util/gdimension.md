GDimension
===========

A utility class to store a width/height pair.

Factory Functions
------------------

*function* @d.GDimension(dimension)
:   Creates a copy of the given @p.dimension.

*function* @d.GDimension([width=0, height=0])
:   Creates a new GDimension with the given @p.width and @p.height. If they are both omitted,
    defaults to 0 and 0.


Methods
--------

*function* GDimension::@d.getWidth()
:   **Returns:** The width of this GDimension.

*function* GDimension::@d.getHeight()
:   **Returns:** The height of this GDimension.

*function* GDimension::@d.setSize(dimension)
:   Sets this GDimension to be equal to the given @p.dimension.

*function* GDimension::@d.setSize(width, height)
:   Sets this GDimension's size to the given @p.width and @p.height).

*function* GDimension::@d.getSize()
:   **Returns:** A copy of this GDimension.

Fields
-------
GPoint::@d.width
:   The width component of this GDimension

GPoint::@d.height
:   The height component of this GDimension