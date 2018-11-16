GLine @extends [GObject](../gobject.md)
========================================

Factory Functions
------------------
*function* @d.GLine(x0, y0, x1, y1)
:   Creates a new GLine connecting points (@p.x0, @p.y0) and (@p.x1, @p.y1).

Methods
--------

*function* GLine::@d.distanceSquared()
:   **Returns:** The length of this line, squared (\( (x_1-x_0)^2 - (y_1-y_0)^2 \)).

*function* GLine::@d.setStartPoint(x, y)
:   Sets the initial point *and origin* of this line to (@p.x, @p.y),
    without changing the position of the end point.

*function* GLine::@d.getStartPoint()
:   **Returns:** The x and y coordinates of the start point as a [GPoint](../util/gpoint.md).

*function* GLine::@d.setEndPoint(x, y)
:   Sets the end point of this line to (@p.x, @p.y),
    without changing the position of the start point or the origin.

*function* GLine::@d.getEndPoint()
:   **Returns:** The x and y coordinates of the end point as a [GPoint](../util/gpoint.md).