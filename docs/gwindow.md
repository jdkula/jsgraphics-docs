The GWindow
===========

Factory Functions
-----------------

*function* @d.GWindow()
: 
 
*function* @d.GWindow(id)
: 
 
*function* @d.GWindow(width, height)
: 

*function* @d.GWindow(id, width, height)
:   Creates a new `GWindow` object with a given @p.width/@p.height,
    and displays it in the given HTML element @p.id.
:   If @p.width or @p.height is unspecified, it will default to 0, 0 (or whatever value is defined in CSS).
:   If @p.id is unspecified, it will default to an element with id `JSConsole` or the body of the document.
: **Returns:**  A new `GWindow` instance.


Methods
-------

*function* GWindow::@d.addEventListener(eventType, listener)
:   Stores an event listener in this GWindow. When the GWindow receives an event of the
    given @p.eventType, it invokes the @p.listener function.
:   @p.eventType should be a string. @p.listener should be a function that takes no arguments.
:   The following event types are valid:

    Event Type | Description
    -----------|------------
    click      | Invoked when a user finishes clicking, but not dragging, the GWindow.
    dblclick   | Invoked when a user double-clicks the GWindow.
    mousedown  | Invoked when a user's mouse clicks down on the GWindow.
    mouseup    | Invoked when a user's mouse button releases on the GWindow.
    drag       | Invoked when a user is holding down their mouse button, and moving their mouse.
    mousemove  | Invoked whenever the user moves their cursor.

*function* GWindow::@d.add(gObject[, x, y])
:   Adds the specified @p.gObject to the window at the location previously
stored in the object. @p.x and @p.y are optional; if they are supplied, then @p.gObject is moved
to the specified location.

*function* GWindow::@d.remove(gObject)
:   Removes the specified @p.gObject from the window. If the object wasn't added to
 the window, this method has no effect.

*function* GWindow::@d.clear()
:   Removes all GObjects from the window.
:   **Alias**: GWindow::@d.removeAll()

*function* GWindow::@d.setSize(width, height)
:   Sets the dimensions of the window as specified.

*function* GWindow::@d.getElementCount()
:   **Returns:** The number of elements contained in the window.

*function* GWindow::@d.getElement(index)
:   **Returns:** The GObject at the specified @p.index (where index 0 was the first GObject added
    to the window/the GObject farthest back, and the last index is the most recently added/most on top GObject).

*function* GWindow::@d.getElementAt(x, y)
:   Gets the topmost (i.e. most recently-added) GObject at the specified @p.x/@p.y coordinates.
:   **Returns:** The found GObject, or null if there's not an object at the specified coordinates.

*function* GWindow::@d.setAutoRepaintFlag(flag)
:   Changes the setting of the auto-repaint flag.  By default, any change
    to a graphical object contained in this window automatically triggers
    a repaint of the window as a whole.  While this behavior makes it
    easier to use JSGraphics, it has the disadvantage that repaint
    requests come much more frequently than necessary.  You can disable
    this feature by calling `gwindowObj.setAutoRepaintFlag(false)`, but you must then
    make explicit calls to `gwindowObj.repaint()` whenever you want to update the
    display.  The advantage of this model is that you can then make many
    different changes and have them all appear at once with a single
    repaint call.

*function* GWindow::@d.getAutoRepaintFlag()
:   **Returns:** `true` if the window is set to always auto-repaint, `false` otherwise.

*function* GWindow::@d.repaint()
:   Forces the window to repaint itself immediately.

*function* GWindow::@d.getSize()
:   **Returns:** The width and height of the window as a [GDimension](util/gdimension.md).

*function* GWindow::@d.getWidth()
:   **Returns:** The width of the window as a number.

*function* GWindow::@d.getHeight()
:   **Returns:** The height of the window as a number.

*function* GWindow::@d.setScaleFactor(multiplier)
:   Scales the entire window by the a @p.multiplier. The window's scale factor is 1 by default.

*function* GWindow::@d.getScaleFactor()
:   **Returns:** The scale factor of the window.