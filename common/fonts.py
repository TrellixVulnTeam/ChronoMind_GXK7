"""This file contains all the fonts used in the game"""

import pygame as pg


# Initialize the fonts
pg.font.init()

# The font used to display the hud
HUD = pg.font.Font('../assets/Fonts/MonsterFriendFore.otf', 30)

# The font used to display the maths letters
MATH = pg.font.SysFont('../assets/Fonts/MonsterFriendFore.otf', 60)
