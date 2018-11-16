The GObject
============
The GObject is the base object (i.e. the common superclass) for all other
graphics objects. Any abstract method seen here can be called on any other (more specific) graphics object,
but not on a generic GObject.

GObject is an abstract class -- if you try to make one directly, you'll have to fill in the abstract methods.

Factory Functions
------------------
*function* @d.GObject()
:   Creates an empty `GObject`. You probably shouldn't be using this.

Methods
--------
*@abstract function* GObject::@d.getBounds()
:   Returns a [GRectangle](util/grectangle.md) representing the smallest box that covers everything
    this GObject covers.

*function* GObject::@d.setLocation([x[, y]])
:   Sets this GObject's location in the window to (@p.x, @p.y). If `undefined` is passed in instead of a number for
    either @p.x and/or @p.y, it defaults to the object's current location.

*function* GObject::@d.getLocation()
:   **Returns:** A [GPoint](util/gpoint.md) representing the origin of this object.

*function* GObject::@d.getX()
:   **Returns:** The x coordinate of this object's origin.

*function* GObject::@d.getY()
:   **Returns:** The y coordinate of this object's origin.

*function* GObject::@d.move(dx, dy)
:   Moves this object by the displacements @p.dx and @p.dy

*function* GObject::@d.movePolar(r, theta)  {:  #movePolar}
:   Moves this object @p.r units in the direction @p.theta. @p.theta is measured in *degrees clockwise
    from the +x axis*.

*@abstract function* GObject::@d.getSize()
:   **Returns:** The size of this object as a [GDimension](util/gdimension.md).

*@abstract function* GObject::@d.getWidth()
:   **Returns:** The width of this object as a number.

*@abstract function* GObject::@d.getHeight()
:   **Returns:** The height of this object as a number.

*@abstract function* GObject::@d.contains(x, y)
:   **Returns:** `true` if this object contains the given @p.x and @p.y coordinates, and `false` otherwise.

*function* GObject::@d.sendToFront()
:   Puts this object on top of all other objects in its attached container. Fails if this object isn't in a container.
:   **See Also:** [GWindow](gwindow.md), [GCompound](gobjects/gcompound.md)

*function* GObject::@d.sendToBack()
:   Puts this object behind all other objects in its attached container. Fails if this object isn't in a container.
:   **See Also:** [GWindow](gwindow.md), [GCompound](gobjects/gcompound.md)


*function* GObject::@d.sendForward()
:   Moves this object one "step" towards the front of its container. Fails if this object isn't in a container.
:   **See Also:** [GWindow](gwindow.md), [GCompound](gobjects/gcompound.md)

*function* GObject::@d.sendBackward()
:   Moves this object one "step" towards the back of its container. Fails if this object isn't in a container.
:   **See Also:** [GWindow](gwindow.md), [GCompound](gobjects/gcompound.md)

*function* GObject::@d.setColor(color)      {: #setColor }
:   Sets the border @p.color of this object. If the object is filled and hasn't been specifically
    assigned a fill color, also sets the fill color.
:   @p.color may be a predefined Javascript color (e.g. `"Red"`), or it may be a string in the form `"#RRGGBB`,
    where RR, GG, and BB are the hexadecimal values of the red, green, and blue intensities.

*function* GObject::@d.getColor()
:   **Returns:** The color of the object as previously set.

*function* GObject::@d.setFillColor(color)
:   Sets the fill @p.color of this object specifically. @p.color's format matches that of [GObject::setColor](#setColor).
:   **See Also:** [GObject::setColor](#setColor)

*function* GObject::@d.setFilled(flag)
:   Sets this object to be filled if `flag` is true, or not filled if `flag` is false.

*function* GObject::@d.isFilled()
:   **Returns:** `true` if this object is filled, `false` otherwise.

*function* GObject::@d.setLineWidth(width)
:   Sets this object's lines to be @p.width units wide.

*function* GObject::@d.getLineWidth()
:   **Returns:** The width of this object's lines as a number.

*function* GObject::@d.rotate(theta)            {: #rotate }
:   Rotates this object by @p.theta degrees around its origin.
:   Marks the object as transformed.

*function* GObject::@d.scale(multiplier)            {: #scale }
: 

*function* GObject::@d.scale(xMultiplier, yMultiplier)
:   Scales this object. If an individual @p.xMultiplier and @p.yMultiplier are specified, scales the x and y
    axes differently as specified. If a single @p.multiplier is specified, scales both x and y by that multiplier.
:   Marks the object as transformed.

*function* GObject::@d.shear(xShear, yShear)            {: #shear }
:   Applies an affine shear transformation to this object, using scale factors @p.xShear and @p.yShear.
:   Marks the object as transformed.

*function* GObject::@d.translate(xTransform, yTransform)            {: #translate }
:   Translates the display of the object by @p.xTransform and @p.yTransform before it is displayed, **without** changing
    the object's origin.
:   Marks the object as transformed.

*function* GObject::@d.setVisible(flag)
:   Makes the object visible if @p.flag is `true`, and invisible if @p.flag is `false`.

*function* GObject::@d.isVisible()
:   **Returns:** `true` if the object is visible, `false` otherwise.