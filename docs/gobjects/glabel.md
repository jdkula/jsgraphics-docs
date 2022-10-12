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

*function* GLabel::@d.getDescent()
:   **Returns:** the descent of this font, which is the maximum distance characters
    extend below the baseline.  In JavaScript, this value is estimated from the point size.

*function* GLabel::@d.getTextAlign()     {: #getTextAlign}
:   **Returns**: the current horizontal text alignment of this font. Can take on
    any of the values noted [here](https://developer.mozilla.org/en-US/docs/Web/API/CanvasRenderingContext2D/textAlign#value),
    notably: `"left"`, `"right"`, and `"center"`. The default value is `"start"`,
    which is `"left"` in LTR languages and `"right"` for RTL languages.

*function* GLabel::@d.setTextAlign(alignment)
:   Sets this GLabel's horizontal text alignment (see [GLabel::getTextAlign](#getTextAlign) for options).

*function* GLabel::@d.getBaseline()     {: #getBaseline}
:   **Returns**: the current baseline alignment (roughly, vertical alignment) of this font. Can take on
    any of the values noted [here](https://developer.mozilla.org/en-US/docs/Web/API/CanvasRenderingContext2D/textBaseline#value),
    notably: `"top"`, `"bottom"`, and `"middle"`. The default value is `"alphabetic"`.

*function* GLabel::@d.setBaseline(baselineAlignment)
:   Sets this GLabel's baseline alignment (see [GLabel::getBaseline](#getBaseline) for options).

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