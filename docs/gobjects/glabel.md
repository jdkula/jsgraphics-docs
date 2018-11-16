GLabel @extends [GObject](../gobject.md)
=======

Factory Functions
------------------
*function* @d.GLabel(str, [x=0, y=0])
:   Creates a new GLabel, displaying the given string @p.str. The object's
    @p.x and @p.y coordinates can also be specified --- if left unspecified, defaults
    to 0, 0.

Methods
--------

*function* GLabel::@d.setFont(fontStr)     {: #setFont}
:   Sets this GLabel's font to the font specified by @p.fontStr.
:   @p.fontStr should be using the CSS form of font specification; for example: `24px 'Helvetica Neue'`

*function* GLabel::@d.getFont()
:   **Returns:** The font this GLabel is currently using. The font is
    returned in the same format specified in [GLabel::setFont](#setFont).

*function* GLabel::@d.setLabel(str)
:   Sets this GLabel to display the string specified by @p.str.

*function* GLabel::@d.getLabel()
:   **Returns:** The text currently displayed by this GLabel.

*function* GLabel::@d.getAscent()
:   **Returns:** The ascent of this font, which is the maximum distance characters 
    extend above the baseline.  In JavaScript, this value is estimated from
    the point size.

*function* GLabel::@d.getDescent()
:   **Returns:** the descent of this font, which is the maximum distance characters
    extend below the baseline.  In JavaScript, this value is estimated from the point size.

Fields
-------

@static @const GLabel.@d.DEFAULT_FAMILY = "SansSerif"
:   Defines the default font family used on a newly-created GLabel.

@static @const GLabel.@d.DEFAULT_SIZE = 12
:   Defines the default font size used on a newly-created GLabel.