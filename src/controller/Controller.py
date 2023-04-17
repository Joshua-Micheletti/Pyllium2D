from shared import cameras
from shared import models
from pyglet.window import key
from pyglet.window import mouse
from model.Model import Model
from model.Sprite import Sprite
from pyglet.math import *

class Controller:
    """Class for handling inputs from the user\n
    Controller()"""

    def __init__(self):
        self.states = dict()


    def handle_key_press(self, symbol, modifiers):
        if symbol == key.A:
            self.states["camera_left"] = True

        if symbol == key.S:
            self.states["camera_down"] = True

        if symbol == key.D:
            self.states["camera_right"] = True

        if symbol == key.W:
            self.states["camera_up"] = True


        if symbol == key.UP:
            self.states["player_up"] = True

        if symbol == key.DOWN:
            self.states["player_down"] = True

        if symbol == key.LEFT:
            self.states["player_left"] = True

        if symbol == key.RIGHT:
            self.states["player_right"] = True


    def handle_key_release(self, symbol, modifiers):
        if symbol == key.A:
            self.states["camera_left"] = False

        if symbol == key.S:
            self.states["camera_down"] = False

        if symbol == key.D:
            self.states["camera_right"] = False

        if symbol == key.W:
            self.states["camera_up"] = False


        if symbol == key.UP:
            self.states["player_up"] = False

        if symbol == key.DOWN:
            self.states["player_down"] = False

        if symbol == key.LEFT:
            self.states["player_left"] = False

        if symbol == key.RIGHT:
            self.states["player_right"] = False


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

            world_x = centered_x + cameras["world"].offset_x
            world_y = centered_y + cameras["world"].offset_y

            if world_x > model.center[0] + (model.width / 2):
                continue

            if world_x < model.center[0] - (model.width / 2):
                continue

            if world_y > model.center[1] + (model.height / 2):
                continue

            if world_y < model.center[1] - (model.height / 2):
                continue

            print(name, model.x, model.y, model.width, model.height, model.center)


    def update(self):
        if "camera_left" in self.states:
            if self.states["camera_left"] == True:
                cameras["world"].move(-1, 0)

        if "camera_right" in self.states:
            if self.states["camera_right"] == True:
                cameras["world"].move(1, 0)

        if "camera_up" in self.states:
            if self.states["camera_up"] == True:
                cameras["world"].move(0, 1)

        if "camera_down" in self.states:
            if self.states["camera_down"] == True:
                cameras["world"].move(0, -1)


        if "player_up" in self.states:
            if self.states["player_up"] == True:
                models["player"].move(0, 5)

        if "player_down" in self.states:
            if self.states["player_down"] == True:
                models["player"].move(0, -5)

        if "player_left" in self.states:
            if self.states["player_left"] == True:
                models["player"].move(-5, 0)

        if "player_right" in self.states:
            if self.states["player_right"] == True:
                models["player"].move(5, 0)
