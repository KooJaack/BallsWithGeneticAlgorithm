import pygame as pg
import sys
from os import path
from settings import *
from players import *
from tilemap import *
from neuralnetwork import *
import numpy as np
import copy


class Game:
    def __init__(self):
        pg.init()
        pg.font.init()  # you have to call this at the start,
        self.screen = pg.display.set_mode((WIDTH, HEIGHT), pg.FULLSCREEN)
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        self.player = []
        game_folder = path.dirname(__file__)
        self.player_img = pg.image.load(path.join(game_folder, PLAYER_IMG)).convert_alpha()
        self.new_player_img = pg.transform.scale(self.player_img, (TILESIZE, TILESIZE))
        self.player_img = self.new_player_img
        self.map = Map(path.join(game_folder, MAP_PATH))
        self.all_sprites = pg.sprite.Group()
        self.walls = pg.sprite.Group()
        self.camera = Camera(self.map.width, self.map.height)
        self.playing = None
        self.dt = None

    def new(self):
        self.all_sprites = pg.sprite.Group()
        self.walls = pg.sprite.Group()
        self.player.clear()
        for row, tiles in enumerate(self.map.data):
            for col, tile in enumerate(tiles):
                if tile == '1':
                    wall = Wall(self, col, row)
                    self.walls.add(wall)
                if tile == 'P':
                        self.player.append(Player(self, col, row))

        self.camera = Camera(self.map.width, self.map.height)

    def run(self):
        self.playing = True
        while self.playing:
            self.dt = self.clock.tick(FPS) / 1000.0
            self.events()
            self.update()
            self.draw()

    def quit(self):
        pg.quit()
        sys.exit()

    def update(self):
        self.all_sprites.update()
        for i in range(0, len(self.player)):
            self.camera.update(self.player[i])

    def draw_grid(self):
        for x in range(0, WIDTH, TILESIZE):
            pg.draw.line(self.screen, LIGHTGREY, (x, 0), (x, HEIGHT))
        for y in range(0, HEIGHT, TILESIZE):
            pg.draw.line(self.screen, LIGHTGREY, (0, y), (WIDTH, y))

    def draw(self):
        self.screen.fill(BGCOLOR)
        self.draw_grid()
        for sprite in self.all_sprites:
            self.screen.blit(sprite.image, self.camera.apply(sprite))
            for i in range(0, len(self.player)):
                pg.draw.rect(self.screen, WHITE, self.camera.apply(self.player[i]), 2)
        pg.display.flip()

    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.quit()

    def show_start_screen(self):
        pass

    def show_go_screen(self):
        pass


g = Game()
g.show_start_screen()
while True:
    g.new()
    g.run()
    g.show_go_screen()
