GRectangle
==========

The GRectangle is a utility class representing a bounding box.

!!! Note
    Don't confuse [GRect](../gobjects/grect.md) with GRectangle. The former is
    a [GObject](../gobject.md) that you can add to a [GWindow](../gwindow.md);
    the latter is a utility type that stores a GObject's bounding box, and
    cannot be added to a GWindow.

Factory Functions
------------------

*function* @d.GRectangle(rect)
:   Creates a copy of the given @p.rect.

*function* @d.GRectangle(x, y, width, height)
:   Creates a GRectangle at (@p.x, @p.y) with the given @p.width and @p.height.

Methods
--------

*function* GRectangle::@d.getX()
:   **Returns:** The x component of this GRectangle's origin.

*function* GRectangle::@d.getY()
:   **Returns:** The y component of this GRectangle's origin.

*function* GRectangle::@d.getWidth()
:   **Returns:** The width of this GRectangle.

*function* GRectangle::@d.getHeight()
:   **Returns:** The height of this GRectangle.

*function* GRectangle::@d.setLocation(point)
:   Sets this GRectangle to be located at the given @p.point.
:   @p.point can also be another GRectangle, or a [GObject](../gobject.md)!

*function* GRectangle::@d.setLocation(x, y)
:   Sets this GRectangle to be located at (@p.x, @p.y)

*function* GRectangle::@d.getLocation()
:   Returns the origin of this rectangle as a [GPoint](gpoint.md)

*function* GRectangle::@d.setSize(dimension)
:   Sets this GRectangle to be the size of the given @p.dimension.
:   @p.dimension can also be another GRectangle, or a [GObject](../gobject.md)!

*function* GRectangle::@d.setSize(width, height)
:   Sets this GRectangle's size to be a given @p.width and @p.height.

*function* GRectangle::@d.setBounds(object)
:   Sets this GRectangle's x/y/width/height to match that of the passed-in @p.object
    of type [GRectangle](../util/grectangle.md) or [GObject](../gobject.md).

*function* GRectangle::@d.setBounds(positionObject, sizeObject)
:   Sets this GRectangle's x/y to match that of the passed-in @p.positionObject, and
    its width/height to match that of the passed-in @p.sizeObject.
:   These objects should be of type [GRectangle](../util/grectangle.md) or [GObject](../gobject.md).
    Additionally, @p.positionObject can be a [GPoint](../util/gpoint.md), and @p.positionObject
    can be a [GDimension](../util/gdimension.md).

*function* GRectangle::@d.setBounds(x, y, width, height)
:   Sets this GRectangle's @p.x, @p.y, @p.width, and @p.height as specified.

*function* GRectangle::@d.contains(x, y)
:   **Returns:** `true` if this GRectangle contains the point (@p.x, @p.y). `false` otherwise.

*function* GRectangle::@d.add(point)
:   Expands this GRectangle to contain the given @p.point.

*function* GRectangle::@d.add(x, y)
:   Expands this GRectangle to contain the point (@p.x, @p.y).

*function* GRectangle::@d.translate(dx, dy)
:   Adjusts the origin of this GRectangle by the displacements @p.dx, @p.dy.