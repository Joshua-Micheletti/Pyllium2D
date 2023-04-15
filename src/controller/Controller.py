from shared import cameras
from shared import models
from pyglet.window import key
from pyglet.window import mouse
from model.Model import Model
from model.Sprite import Sprite
from pyglet.math import *

class Controller:

    def __init__(self):
        self.states = dict()

        self.states["camera_left"] = False
        self.states["camera_right"] = False
        self.states["camera_up"] = False
        self.states["camera_down"] = False

    def handle_key_press(self, symbol, modifiers):
        if symbol == key.A:
            self.states["camera_left"] = True

        if symbol == key.S:
            self.states["camera_down"] = True

        if symbol == key.D:
            self.states["camera_right"] = True

        if symbol == key.W:
            self.states["camera_up"] = True


    def handle_key_release(self, symbol, modifiers):
        if symbol == key.A:
            self.states["camera_left"] = False

        if symbol == key.S:
            self.states["camera_down"] = False

        if symbol == key.D:
            self.states["camera_right"] = False

        if symbol == key.W:
            self.states["camera_up"] = False


    def handle_mouse_scroll(self, x, y, scroll_x, scroll_y):
        if scroll_y > 0:
            cameras["world"].set_zoom(cameras["world"].zoom + 0.1)
        if scroll_y < 0:
            cameras["world"].set_zoom(cameras["world"].zoom - 0.1)


    def handle_mouse_drag(self, x, y, button, modifiers):
        pass


    def handle_mouse_press(self, x, y, centered_x, centered_y, button, modifiers):
        print(f"pressed a mouse button at ({x}, {y})")

        for item in models.items():
            name = item[0]
            model = item[1]

            if not isinstance(model, Sprite):
                continue

            screen_coords = Vec4(x, y, 0, 0)

            print(screen_coords)

            # view_matrix = Mat4.from_translation((-cameras["world"].offset_x * cameras["world"].zoom, -cameras["world"].offset_y * cameras["world"].zoom, 0)) @ Mat4.from_scale((cameras["world"].zoom, cameras["world"].zoom, 1))

            # print(view_matrix)
            #
            # for i in range(16):
            #     print(view_matrix[i])
            #
            # matrix_col_0 = Vec4(view_matrix[12], view_matrix[8], view_matrix[4], view_matrix[0])
            # matrix_col_1 = Vec4(view_matrix[13], view_matrix[9], view_matrix[5], view_matrix[1])

            # world_coords = Vec4(screen_coords.dot(matrix_col_0), screen_coords.dot(matrix_col_1), 0, 0)

            world_x = centered_x + (-cameras["world"].offset_x * cameras["world"].zoom)
            world_y = centered_y + (-cameras["world"].offset_y * cameras["world"].zoom)

            print(world_x, world_y)

            # print(Mat4.from_translation((-cameras["world"].offset_x * cameras["world"].zoom, -cameras["world"].offset_y * cameras["world"].zoom, 0)) @ Mat4.from_scale((cameras["world"].zoom, cameras["world"].zoom, 1)))

            # print(world_coords)

            if world_x > model.center[0] + (model.width / 2) + (-cameras["world"].offset_x * cameras["world"].zoom):
                continue

            if world_x < model.center[0] - (model.width / 2) + (-cameras["world"].offset_x * cameras["world"].zoom):
                continue

            if world_y > model.center[1] + (model.height / 2) + (-cameras["world"].offset_y * cameras["world"].zoom):
                continue

            if world_y < model.center[1] - (model.height / 2) + (-cameras["world"].offset_y * cameras["world"].zoom):
                continue

            print(name, model.x, model.y, model.width, model.height, model.center[0] + (-cameras["world"].offset_x * cameras["world"].zoom), model.center[1] + (-cameras["world"].offset_y * cameras["world"].zoom))



    def update(self):
        if self.states["camera_left"] == True:
            cameras["world"].move(-1, 0)
        if self.states["camera_right"] == True:
            cameras["world"].move(1, 0)
        if self.states["camera_up"] == True:
            cameras["world"].move(0, 1)
        if self.states["camera_down"] == True:
            cameras["world"].move(0, -1)
