import pyglet
from pyglet.gl import *
from pyglet.math import *
from pyrr import Matrix44
import numpy as np
import time

class Camera:
    def __init__(self):
        self.view_matrix = Matrix44.identity()
        self.x = 0
        self.y = 0

    def set_view_matrix(self, width, height):
        self.view_matrix = Matrix44.from_translation(np.array([-self.x, -self.y, 0]))

    def move(self, x, y):
        self.x += x
        self.y += y
        self.set_view_matrix(self.x, self.y)

    def place(self, x, y):
        self.x = x
        self.y = y
        self.set_view_matrix(self.x, self.y)


class FollowCamera(Camera):

    def __init__(self, target = ""):
        super().__init__()
        self.delay = 3
        self.target = target
        self.last_update = time.time()


    def follow(self, target_x, target_y):
        dt = time.time() - self.last_update
        self.last_update = time.time()

        self.x += (target_x - self.x) * self.delay * dt
        self.y += (target_y - self.y) * self.delay * dt
        self.set_view_matrix(self.x, self.y)
