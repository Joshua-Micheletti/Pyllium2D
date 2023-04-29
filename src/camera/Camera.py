import pyglet
from pyglet.gl import *
from pyglet.math import *
from pyrr import Matrix44
import numpy as np

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