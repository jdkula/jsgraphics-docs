GRect @extends [GObject](../gobject.md)
========================================

A graphical representation of a rectangle.

!!! Note
    Don't confuse GRect with [GRectangle](../util/grectangle.md). The former is
    a [GObject](../gobject.md) that you can add to a [GWindow](../gwindow.md);
    the latter is a utility type that stores a GObject's bounding box, and
    cannot be added to a GWindow.

Factory Functions
------------------
*function* @d.GRect(width, height)
: 

*function* @d.GRect(x, y, width, height)
:   Creates a new GRect of a given @p.width and @p.height.
    The object's @p.x and @p.y coordinates can also be specified --- if left unspecified,
    defaults to 0, 0.

Methods
--------

!!! warning
    These functions will all throw an error if this object has been transformed
    by [GObject::rotate](../gobject.md#rotate), [GObject::scale](../gobject.md#scale),
    [GObject::shear](../gobject.md#shear), or [GObject::translate](../gobject.md#translate).

*function* GRect::@d.setSize(object)
:   Sets this GRect's width/height to match that of the passed-in @p.object
    of type [GRectangle](../util/grectangle.md) or [GObject](../gobject.md).

*function* GRect::@d.setSize(width, height)
:   Sets this GRect's @p.width and @p.height as specified.

*function* GRect::@d.setBounds(object)
:   Sets this GRect's x/y/width/height to match that of the passed-in @p.object
    of type [GRectangle](../util/grectangle.md) or [GObject](../gobject.md).

*function* GRect::@d.setBounds(positionObject, sizeObject)
:   Sets this GOval's x/y to match that of the passed-in @p.positionObject, and
    its width/height to match that of the passed-in @p.sizeObject.
:   These objects should be of type [GRectangle](../util/grectangle.md) or [GObject](../gobject.md).
    Additionally, @p.positionObject can be a [GPoint](../util/gpoint.md), and @p.positionObject
    can be a [GDimension](../util/gdimension.md).

*function* GRect::@d.setBounds(x, y, width, height)
:   Sets this GOval's @p.x, @p.y, @p.width, and @p.height as specified.