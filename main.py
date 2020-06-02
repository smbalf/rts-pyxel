import pyxel
import npc
from highlight import Highlight


class App:
    def __init__(self):
        pyxel.init(250, 250)

        pyxel.load("rects.pyxres", image=True)

        pyxel.run(self.update, self.draw)

    def update(self):
        pass

    def draw(self):
        pyxel.cls(0)
        pyxel.circ(pyxel.mouse_x, pyxel.mouse_y, 1, 9)  # THE MOUSE

        Highlight.hbox()
        npc.draw_npcs()
        npc.select_npc()
        npc.move_npc()

        pyxel.text(170, 1, f"{Highlight.highlight_box}", 3)


App()
