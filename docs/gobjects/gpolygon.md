GPolygon @extends [GObject](../gobject.md)
=======

Factory Functions
------------------
*function* @d.GPolygon([x=0, y=0])
:   Creates an empty GPolygon. The object's @p.x and @p.y coordinates can also be
    specified --- if left unspecified, defaults to 0, 0.

Methods
--------
*function* GPolygon::@d.addVertex(x, y)
:   Adds a vertex at (@p.x, @p.y) relative to the polygon's origin.

*function* GPolygon::@d.addEdge(dx, dy)
:   Adds a vertex at wherever the last point was placed (or 0, 0 if 
    this is the first), shifted by @p.dx and @p.dy.

*function* GPolygon::@d.addPolarEdge(r, theta)
:   Adds a vertex at wherever the last point was placed (or, 0, 0 if
    this is the first), shifted by @p.r units in the direction @p.theta.
    @p.theta is measured in *degrees counterclockwise from the +x axis*.
:   **See Also:** [GObject::movePolar](../gobject.md#movePolar)

*function* GPolygon::@d.getCurrentPoint()
:   **Returns:** A [GPoint](../util/gpoint.md),
    representing the last point that was added to this GPolygon.
:   **See Also:** [GPoint](../util/gpoint.md)