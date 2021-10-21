import pygame as pg
from settings import *
from tilemap import collide_hit_rect
import math
import datetime
from neuralnetwork import *

vector = pg.math.Vector2


class Player(pg.sprite.Sprite):

    block = None

    def __init__(self, game, x, y, a=None, b=None):
        self.groups = game.walls
        self.all = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.all)
        self.bot = LearningBot(a, b)
        self.game = game
        self.image = game.player_img
        self.rect = self.image.get_rect()
        self.hit_rect = PLAYER_HIT_RECT
        self.hit_rect.center = self.rect.center
        self.vel = vector(0, 0)
        self.pos = vector(x, y) * TILESIZE
        self.pos.x += TILESIZE/2
        self.pos.y += TILESIZE/2
        self.last_pos = vector(x, y) * TILESIZE
        self.last_pos.x += TILESIZE/2
        self.last_pos.y += TILESIZE/2
        self.rot = 0
        self.block = False
        self.speed_a = 0
        self.speed_b = PLAYER_SPEED
        self.raz = False

    def get_keys(self):
        #self.vel = vector(0, PLAYER_SPEED)
        if not self.block:
            a, d = self.in_view_player()
            self.bot.feed_network(a, d)
            print("Wejscie: ", a, d)
            data = self.bot.calculate_layers()
            print("Siec mowi: ", data)
            if data[0] > SENS or data[0] < -SENS or data[1] > SENS or data[1] < -SENS:
                if data[1] > SENS:
                    self.speed_a = PLAYER_SPEED
                elif data[1] < -SENS:
                    self.speed_a = -PLAYER_SPEED
                else:
                    self.speed_a = 0

                if data[0] > SENS:
                    self.speed_b = PLAYER_SPEED
                elif data[0] < -SENS:
                    self.speed_b = -PLAYER_SPEED
                else:
                    self.speed_b = 0
            if d != -1:
                self.raz = False
                if not self.block:
                    self.vel = vector(self.speed_b, self.speed_a)
            else:
                if self.raz is False:
                    self.raz = True
                    r = np.random.randint(0, 8)
                    if r == 0:
                        self.vel = vector(PLAYER_SPEED, 0)
                    elif r == 1:
                        self.vel = vector(-PLAYER_SPEED, 0)
                    elif r == 2:
                        self.vel = vector(0, PLAYER_SPEED)
                    elif r == 3:
                        self.vel = vector(0, -PLAYER_SPEED)
                    elif r == 4:
                        self.vel = vector(PLAYER_SPEED, -PLAYER_SPEED)
                    elif r == 5:
                        self.vel = vector(-PLAYER_SPEED, -PLAYER_SPEED)
                    elif r == 6:
                        self.vel = vector(PLAYER_SPEED, PLAYER_SPEED)
                    elif r == 7:
                        self.vel = vector(-PLAYER_SPEED, PLAYER_SPEED)
        else:
            self.vel = vector(0, 0)

    def in_view_player(self):
        answer = -1
        distance = -1
        mydistance = -1
        for sprite in self.all:
            if sprite is not self:
                dx = sprite.pos.x - self.pos.x
                dy = sprite.pos.y - self.pos.y
                rads = math.atan2(-dy, dx)
                rads %= 2 * math.pi
                degs = math.degrees(rads)
                distance = -1
                if math.sqrt(dx**2+dy**2) <= 100:
                    distance = (math.sqrt(dx ** 2 + dy ** 2) * (-1 /25)) + 3
                    if math.sqrt(dx**2+dy**2) < 50:
                        distance = 1
                    if distance > mydistance:
                        mydistance = distance
                        answer = (degs/180)-1
        print(answer, mydistance)
        return answer, mydistance

    def collide(self):
        if pg.sprite.spritecollide(self, self.groups, False):
            self.block = True

    def update(self):
        self.get_keys()
        self.rect.center = self.pos
        self.pos += self.vel * self.game.dt
        self.collide()


class Wall(pg.sprite.Sprite):

    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.walls
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.x = x+TILESIZE/2
        self.y = y+TILESIZE/2
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE
        self.pos = vector(x, y) * TILESIZE
        self.pos.x += TILESIZE/2
        self.pos.y += TILESIZE/2
