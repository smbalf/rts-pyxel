import pyxel
from highlight import Highlight as H

# SPRITES
unselected_sprite = 0, 0, 0, 3, 3
selected_sprite = 0, 4, 0, 3, 3

npc_list = []


class Npc:

    def __init__(self, x, y, selected, d_x, d_y):
        self.npc_x = x
        self.npc_y = y
        self.npc_selected = selected
        self.dest_x = d_x
        self.dest_y = d_y

        npc_list.append(self)


block1 = Npc(20, 20, False, 20, 20)
block2 = Npc(20, 25, False, 20, 25)
block3 = Npc(20, 30, False, 20, 30)
block4 = Npc(20, 35, False, 20, 35)
block5 = Npc(20, 40, False, 20, 40)


def draw_npcs():
    for npc in npc_list:
        if not npc.npc_selected:
            pyxel.blt(npc.npc_x, npc.npc_y, *unselected_sprite)
        else:
            pyxel.blt(npc.npc_x, npc.npc_y, *selected_sprite)


def select_npc():
    # IF NPC INSIDE BOX - BECOMES SELECTED
    if pyxel.btnr(pyxel.MOUSE_LEFT_BUTTON):
        for npc in npc_list:
            if pyxel.btnr(pyxel.MOUSE_LEFT_BUTTON) and npc.npc_selected:
                npc.npc_selected = False

            if npc.npc_x in range(H.line_x1, H.line_x2) and npc.npc_y in range(H.line_y1, H.line_y2):
                npc.npc_selected = True

            elif npc.npc_x in range(H.line_x2, H.line_x1) and npc.npc_y in range(H.line_y1, H.line_y2):
                npc.npc_selected = True

            elif npc.npc_x in range(H.line_x1, H.line_x2) and npc.npc_y in range(H.line_y2, H.line_y1):
                npc.npc_selected = True

            elif npc.npc_x in range(H.line_x2, H.line_x1) and npc.npc_y in range(H.line_y2, H.line_y1):
                npc.npc_selected = True


def move_npc():
    for npc in npc_list:
        # SETS THE DESTINATION CO-ORDINATES WHEN SELECTED AND RMB RELEASED
        if pyxel.btnr(pyxel.MOUSE_RIGHT_BUTTON) and npc.npc_selected:
            npc.dest_x = pyxel.mouse_x
            npc.dest_y = pyxel.mouse_y
            npc.npc_selected = False

        # MOVES THE NPC EVERY 2 FRAMES BY 1 PIXEL UNTIL DESTINATION CO-ORDINATES REACHED
        if pyxel.frame_count % 2 == 0:
            if npc.npc_x < npc.dest_x:
                npc.npc_x += 1
            elif npc.npc_x > npc.dest_x:
                npc.npc_x -= 1
            if npc.npc_y < npc.dest_y:
                npc.npc_y += 1
            elif npc.npc_y > npc.dest_y:
                npc.npc_y -= 1
