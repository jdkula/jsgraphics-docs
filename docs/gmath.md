GMath
======
GMath provides a bunch of convenience methods you can use when working with graphics.

Methods
--------

*@static function* GMath.round(x)
:   Rounds @p.x to the nearest integer.
:   **Returns:** The rounded integer.

*@static function* GMath.sinDegrees(angle)
:   **Returns:** The sine of the given @p.angle (where @p.angle is in degrees).

*@static function* GMath.cosDegrees(angle)
:   **Returns:** The cosine of the given @p.angle (where @p.angle is in degrees).

*@static function* GMath.tanDegrees(angle)
:   **Returns:** The tangent of the given @p.angle (where @p.angle is in degrees).

*@static function* GMath.toDegrees(angle)
:   Converts an @p.angle expressed in radians to degrees.
:   **Returns:** The degree representation of @p.angle.

*@static function* GMath.distance(x, y)
:   **Returns:** The distance from the origin to the point (@p.x, @p.y)

*@static function* GMath.distance(x0, y0, x1, y1)
:   **Returns:** The length of the line from the point (@p.x0, @p.y0) to (@p.x1, @p.y1).

*@static function* GMath.angle(x, y)
:   **Returns:** The angle (in degrees) from the origin to the point (@p.x, @p.y)

*@static function* GMath.angle(x0, y0, x1, y1)
:   **Returns:** The angle (in degrees) from the point (@p.x0, @p.y0) to the point (@p.x1, @p.y1).