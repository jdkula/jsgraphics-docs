GMath
======
GMath provides a bunch of convenience methods you can use when working with graphics.

Methods
--------

*@static function* GMath.@d.round(x)
:   Rounds @p.x to the nearest integer.
:   **Returns:** The rounded integer.

*@static function* GMath.@d.sinDegrees(angle)
:   **Returns:** The sine of the given @p.angle (where @p.angle is in degrees).

*@static function* GMath.@d.cosDegrees(angle)
:   **Returns:** The cosine of the given @p.angle (where @p.angle is in degrees).

*@static function* GMath.@d.tanDegrees(angle)
:   **Returns:** The tangent of the given @p.angle (where @p.angle is in degrees).

*@static function* GMath.@d.toDegrees(angle)
:   Converts an @p.angle expressed in radians to degrees.
:   **Returns:** The degree representation of @p.angle.

*@static function* GMath.@d.distance(x, y)
:   **Returns:** The distance from the origin to the point (@p.x, @p.y)

*@static function* GMath.@d.distance(x0, y0, x1, y1)
:   **Returns:** The length of the line from the point (@p.x0, @p.y0) to (@p.x1, @p.y1).

*@static function* GMath.@d.angle(x, y)
:   **Returns:** The angle (in degrees) from the origin to the point (@p.x, @p.y)

*@static function* GMath.@d.angle(x0, y0, x1, y1)
:   **Returns:** The angle (in degrees) from the point (@p.x0, @p.y0) to the point (@p.x1, @p.y1).