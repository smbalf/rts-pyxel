import pyxel


class Highlight:
    # LINE CO-ORDINATES FOR CREATING THE BOX
    line_x1 = 0
    line_y1 = 0
    line_x2 = 0
    line_y2 = 0

    # LIST TO STORE THE CO-ORDINATES OF THE BOX
    highlight_box = []

    @classmethod
    def hbox(cls):
        # TAKE X1 Y1 WHEN LMB HELD
        if pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON, 0):
            Highlight.line_x1 = pyxel.mouse_x
            Highlight.line_y1 = pyxel.mouse_y

        # TAKE X2 Y2 WHEN LMB PRESSED - DRAWS THE HIGHLIGHT BOX BY CONNECTING CO-ORDINATES
        if pyxel.btn(pyxel.MOUSE_LEFT_BUTTON):
            Highlight.line_x2 = pyxel.mouse_x
            Highlight.line_y2 = pyxel.mouse_y
            pyxel.line(Highlight.line_x1, Highlight.line_y1, Highlight.line_x2, Highlight.line_y1, 3)
            pyxel.line(Highlight.line_x1, Highlight.line_y1, Highlight.line_x1, Highlight.line_y2, 3)
            pyxel.line(Highlight.line_x1, Highlight.line_y2, Highlight.line_x2, Highlight.line_y2, 3)
            pyxel.line(Highlight.line_x2, Highlight.line_y1, Highlight.line_x2, Highlight.line_y2, 3)

        # CLEARS THE HIGHLIGHT_BOX LIST, ADDS THE X1 Y1 X2 Y2 VALUES TO THE LIST
        if pyxel.btnr(pyxel.MOUSE_LEFT_BUTTON):
            Highlight.highlight_box.clear()
            Highlight.highlight_box.extend([Highlight.line_x1, Highlight.line_x2, Highlight.line_y1, Highlight.line_y2])
