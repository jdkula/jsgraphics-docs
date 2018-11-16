GPoint
=======

A utility class to store an x and y coordinate.

Factory Functions
------------------

*function* @d.GPoint(point)
:   Creates a copy of the given @p.point.

*function* @d.GPoint([x=0, y=0])
:   Creates a new GPoint with the given @p.x and @p.y coordinates. If they are both omitted,
    defaults to 0, 0


Methods
--------

*function* GPoint::@d.getX()
:   **Returns:** The x component of this GPoint.

*function* GPoint::@d.getY()
:   **Returns:** The y component of this GPoint.

*function* GPoint::@d.setLocation(point)
:   Sets this GPoint to be equal to the given @p.point.

*function* GPoint::@d.setLocation(x, y)
:   Sets this GPoint's location to (@p.x, @p.y).

*function* GPoint::@d.getLocation()
:   **Returns:** A copy of this GPoint.

*function* GPoint::@d.translate(dx, dy)
:   Adds @p.dx and @p.dy to the x and y components of this GPoint, respectively.

Fields
-------
GPoint::@d.x
:   The x component of this GPoint

GPoint::@d.y
:   The y component of this GPoint