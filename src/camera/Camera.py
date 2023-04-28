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

# class Camera:
#
#     def __init__(self, window: pyglet.window.Window, move_speed = 1, min_zoom = 1, max_zoom = 4):
#         assert min_zoom <= max_zoom, "Minimum zoom must not be greater than maximum zoom"
#         self.move_speed = move_speed
#         self.max_zoom = max_zoom
#         self.min_zoom = min_zoom
#         self.offset_x = 0
#         self.offset_y = 0
#         self.zoom = max(min(1, self.max_zoom), self.min_zoom)
#
#         self.window = window
#
#     def zoom(self):
#         return(self.zoom)
#
#     def set_zoom(self, value):
#         self.zoom = max(min(value, self.max_zoom), self.min_zoom)
#
#     def position(self):
#         return self.offset_x, self.offset_y
#
#     def set_position(self, value):
#         self.offset_x, self.offset_y = value
#
#     def move(self, axis_x, axis_y):
#         self.offset_x += self.move_speed * axis_x
#         self.offset_y += self.move_speed * axis_y
#
#
#     def begin(self):
#         self.window.view = self.window.view @ Mat4.from_translation((-self.offset_x * self.zoom, -self.offset_y * self.zoom, 0)) @ Mat4.from_scale((self.zoom, self.zoom, 1))
#
#     def end(self):
#         self.window.view = self.window.view @ Mat4.from_scale((1 / self.zoom, 1 / self.zoom, 1)) @ Mat4.from_translation((self.offset_x * self.zoom, self.offset_y * self.zoom, 0))
#
#
#     def __enter__(self):
#         self.begin()
#
#     def __exit__(self, exception_type, exception_value, traceback):
#         self.end()
#
#
# class CenteredCamera(Camera):
#     """A simple 2D camera class. 0, 0 will be the centre of the screen, as opposed to the bottom left.\n
#     CenteredCamera(window: pyglet.window.Window, move_speed = 1, min_zoom = 1, max_zoom = 4)"""
#
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#
#     def begin(self):
#         x = -self.window.width//2/self.zoom + self.offset_x
#         y = -self.window.height//2/self.zoom + self.offset_y
#
#         self.window.view = self.window.view @ Mat4.from_translation((-x * self.zoom, -y * self.zoom, 0)) @ Mat4.from_scale((self.zoom, self.zoom, 1))
#
#     def end(self):
#         x = -self.window.width//2/self.zoom + self.offset_x
#         y = -self.window.height//2/self.zoom + self.offset_y
#
#         self.window.view = self.window.view @ Mat4.from_scale((1 / self.zoom, 1 / self.zoom, 1)) @ Mat4.from_translation((x * self.zoom, y * self.zoom, 0))
#
#
# class FollowCamera(CenteredCamera):
#
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.delay = 0.1
#
#     def follow(self, target_x, target_y):
#         self.offset_x += (target_x - self.offset_x) * self.delay
#         self.offset_y += (target_y - self.offset_y) * self.delay
