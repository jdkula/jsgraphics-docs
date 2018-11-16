GImage @extends [GObject](../gobject.md)
=========================================

A graphical representation of an image.

Factory Functions
------------------

*function* @d.GImage(source[, x=0, y=0])
:   Constructs a GImage object from the given @p.source. @p.x and @p.y may
    be specified to set where the GImage should appear in the window; otherwise,
    it defaults to (0, 0).
:   @p.source may be a Data URL, a local file, or a 2D array of pixels.
:   
    !!! Note
        The GImage is loaded *asynchronously*, meaning that your code will continue
        to run while the GImage is loading. However, before it's loaded, it does not
        know its own width or height. If you need to work with these values, it's recommended
        to add a "load" event listener.

Methods
--------

*function* GImage::@d.addEventListener(eventType, listener)
:   Adds the given @p.listener to this image. The only valid @p.eventType is "load" ---
    any other event type will fail silently.
:   The load event triggers when the image has been fully loaded.

*function* GImage::@d.getPixelArray()
:   **Returns:** A 2D array of RGBA pixels. You can get the individual color values from
                 these pixels using the methods below.

@static *function* GImage.@d.getAlpha(pixel)
:   **Returns:** The alpha value of the given @p.pixel.

@static *function* GImage.@d.getRed(pixel)
:   **Returns:** The red intensity of the given @p.pixel.

@static *function* GImage.@d.getGreen(pixel)
:   **Returns:** The green intensity of the given @p.pixel.

@static *function* GImage.@d.getBlue(pixel)
:   **Returns:** The blue intensity of the given @p.pixel.

@static *function* GImage.@d.createRGBPixel(red, green, blue[, alpha=255])
:   **Returns:** A pixel created from the given @p.red, @p.green, @p.blue, and @p.alpha
                 values. If @p.alpha is omitted, defaults to 255 (completely opaque).

!!! Warning
    The functions below will all throw an error if this object has been transformed
    by [GObject::rotate](../gobject.md#rotate), [GObject::scale](../gobject.md#scale),
    [GObject::shear](../gobject.md#shear), or [GObject::translate](../gobject.md#translate).

*function* GImage::@d.setSize(object)
:   Sets this GImage's width/height to match that of the passed-in @p.object
    of type [GDimension](../util/gdimension.md), [GRectangle](../util/grectangle.md),
    or [GObject](../gobject.md).

*function* GImage::@d.setSize(width, height)
:   Sets this GOval's @p.width and @p.height as specified.

*function* GImage::@d.setBounds(object)
:   Sets this GImage's x/y/width/height to match that of the passed-in @p.object
    of type [GRectangle](../util/grectangle.md) or [GObject](../gobject.md).

*function* GImage::@d.setBounds(positionObject, sizeObject)
:   Sets this GImage's x/y to match that of the passed-in @p.positionObject, and
    its width/height to match that of the passed-in @p.sizeObject. These objects
    should be of type [GRectangle](../util/grectangle.md) or [GObject](../gobject.md).
    Additionally, @p.positionObject can be a [GPoint](../util/gpoint.md), and @p.positionObject
    can be a [GDimension](../util/gdimension.md).

*function* GImage::@d.setBounds(x, y, width, height)
:   Sets this GImage's @p.x, @p.y, @p.width, and @p.height as specified.