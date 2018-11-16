GCompound @extends [GObject](../gobject.md)
============================================

The GCompound defines a graphical object that consists of a collection
of other graphical objects.  Once assembled, the internal objects
can be manipulated as a unit.

Factory Functions
------------------
*function* @d.GCompound()
: 

*function* @d.GCompound(x, y)
:   Creates a new GCompound, optionally moving the compound's origin
    to (@p.x, @p.y).

Methods
--------
*function* GCompound::@d.add(gObject[x=@p.gObject.getX(), y=@p.gObject.getY()])
:   Adds the given @p.gObject to the compound. If @p.x and @p.y are specified,
    the @p.gObject's x and y values are overwritten; otherwise, they're used instead.

*function* GCompound::@d.remove(gObject)
:   Removes the given @P.gObject from the compound.

*function* GCompound::@d.removeAll()
:   Removes all GObjects from this GCompound.

*function* GCompound::@d.getElementCount()
:   **Returns:** The number of GObjects stored in this GCompound.

*function* GCompound::@d.getElement(index)
:   **Returns:** The GObject at the specified @p.index (where index 0 was the first GObject added
                 to the GCompound/the GObject farthest back, and the last index is the most recently
                 added/most on top GObject).

*function* GCompound::@d.getElementAt(x, y)
:   Gets the topmost (i.e. most recently-added) GObject at the specified @p.x/@p.y coordinates.
:   **Returns:** The found GObject, or null if there's not an object at the specified coordinates.

!!! Note
    If you need to access elements in a GCompound, it's recommended to append
    them as additional fields, rather than use `GCompound::getElementAt` or
    `GCompound::getElement`.