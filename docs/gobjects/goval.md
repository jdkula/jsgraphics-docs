GOval @extends [GObject](../gobject.md)
========================================

Factory Functions
------------------
*function* @d.GOval(width, height)
: 

*function* @d.GOval(x, y, width, height)
:   Creates a new GOval that fits into the rectangle of a given @p.width and @p.height.
    The object's @p.x and @p.y coordinates can also be specified --- if left unspecified,
    defaults to 0, 0.

Methods
--------

!!! Warning
    These functions will all throw an error if this object has been transformed
    by [GObject::rotate](../gobject.md#rotate), [GObject::scale](../gobject.md#scale),
    [GObject::shear](../gobject.md#shear), or [GObject::translate](../gobject.md#translate).

*function* GOval::@d.setSize(object)
:   Sets this GOval's width/height to match that of the passed-in @p.object
    of type [GDimension](../util/gdimension.md), [GRectangle](../util/grectangle.md),
    or [GObject](../gobject.md).

*function* GOval::@d.setSize(width, height)
:   Sets this GOval's @p.width and @p.height as specified.

*function* GOval::@d.setBounds(object)
:   Sets this GOval's x/y/width/height to match that of the passed-in @p.object
    of type [GRectangle](../util/grectangle.md) or [GObject](../gobject.md).

*function* GOval::@d.setBounds(positionObject, sizeObject)
:   Sets this GOval's x/y to match that of the passed-in @p.positionObject, and
    its width/height to match that of the passed-in @p.sizeObject.
:   These objects should be of type [GRectangle](../util/grectangle.md) or [GObject](../gobject.md).
    Additionally, @p.positionObject can be a [GPoint](../util/gpoint.md), and @p.positionObject
    can be a [GDimension](../util/gdimension.md).

*function* GOval::@d.setBounds(x, y, width, height)
:   Sets this GOval's @p.x, @p.y, @p.width, and @p.height as specified.