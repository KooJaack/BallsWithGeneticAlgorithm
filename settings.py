import pygame as pg

# define some colors (R, G, B)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARKGREY = (40, 40, 40)
LIGHTGREY = (100, 100, 100)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

# game settings
WIDTH = 2560   # 16 * 64 or 32 * 32 or 64 * 16
HEIGHT = 1080  # 16 * 48 or 32 * 24 or 64 * 12
FPS = 80
TITLE = "Sztuczna inteligencja"
BGCOLOR = LIGHTGREY

TILESIZE = 16
GRIDWIDTH = WIDTH / TILESIZE
GRIDHEIGHT = HEIGHT / TILESIZE

# Player settings
PLAYER_SPEED = 250
PLAYER_ROT_SPEED = 1500
PLAYER_IMG = 'kula.png'
PLAYER_HIT_RECT = pg.Rect(0, 0, 35, 35)
MAP_PATH = 'map.txt'

VIEW_ANGLE = 50
N_INPUT = 2
N_HIDDEN = 2
N_HIDDEN_LAYER = 1
N_OUTPUT = 1
POPULATION_SIZE = 1
CROSS_CHANCE = 0.6
MUTATION_CHANCE = 0.05
SENS = 0.5
#11111111111111111111
#111.....1..........1
#11......1..........1
#11......1..........1
#1...1...1...1......1
#1...1...1...1......1
#1...1...1...1......1
#1...1...1...1......1
#1...1...1...1......1
#1...1.......1......1
#1...1.......11.....1
#1...1.......111....1
#1...111111111111...1
#1.P................1
#1..................1
#11111111111111111111