GArc @extends [GObject](../gobject.md)
=======================================

The GArc is a graphical object whose appearance consists of an arc.
If unfilled, the arc is simply a portion of the circumference of an
ellipse; if filled, the arc is a pie-shaped wedge connected to the
center of the figure.

Factory Functions
------------------
*function* @d.GArc(width, height, start, sweep)
: 

*function* @d.GArc(x, y, width, height, start, sweep)
:   Creates a GArc object consisting of an elliptical arc that fits inside
    the bounding box specified by @p.x, @p.y, @p.width, and @p.height.
    If @p.x and @p.y are missing, they default to 0. The @p.start parameter 
    indicates the angle at which the arc begins and is measured 
    in *degrees counterclockwise from the +x axis.*
    Thus, a @p.start angle of 0 indicates an arc that begins
    along the line running eastward from the center, a @p.start angle of 135
    begins along the line running northwest, and a @p.start angle of -90
    begins along the line running south.  The @p.sweep parameter indicates
    the extent of the arc and is also measured in *degrees counterclockwise*.
    A @p.sweep angle of 90 defines a quarter circle extending counterclockwise
    from the @p.start angle, and a @p.sweep angle of -180 defines a semicircle
    extending clockwise.

Method
-------
*function* GArc::@d.setStartAngle(angle)
:   Sets the starting @p.angle for this GArc object.

*function* GArc::@d.getStartAngle()
:   **Returns:** The starting angle for this GArc.

*function* GArc::@d.setSweepAngle(angle)
:   Sets the sweep @p.angle for this GArc.

*function* GArc::@d.getSweepAngle()
:   **Returns:** The current sweep angle for this GArc.

*function* GArc::@d.getStartPoint()
:   **Returns:** The x and y coordinates of where the arc starts as a [GPoint](../util/gpoint.md).

*function* GArc::@d.getEndPoint()
:   **Returns:** The x and y coordinates of where the arc ends as a [GPoint](../util/gpoint.md).

*function* GArc::@d.setFrameRectangle(object)
:   Sets this GArc's bounding box to match the given @p.object's. @p.object must be
    a [GRectangle](../util/grectangle.md) or a [GObject](../gobject.md).

*function* GArc::@d.setFrameRectangle(x, y, width, height)
:   Sets this GArc's bounding box to match the coordinates and dimensions given.

*function* GArc::@d.getFrameRectangle()
:   **Returns:** The current bounding box of this GArc, as a [GRectangle](../util/grectangle.md).