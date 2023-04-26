import pyglet
from pyglet.window import key
from pyglet.window import mouse
from pyglet.window import FPSDisplay
from pyglet import gl
from pyglet.math import Mat4
from renderer.Renderer import Renderer
from controller.Controller import Controller
from shared import cameras
from shared import *

import time

class Window(pyglet.window.Window):
    def __init__(self, width = 1280, height = 720, resizable = True, min_w = 400, min_h = 300, max_w = 1920, max_h = 1080, renderer = Renderer(), controller = Controller()):
        # self.customContext = gl.Config()
        # self.customContext.stencil_size = 8
        # self.customContext.aux_buffers = 4

        super().__init__(width, height, resizable = resizable)

        print(self.config)

        self.set_minimum_size(min_w, min_h)
        self.set_maximum_size(max_w, max_h)

        self.renderer = renderer
        self.controller = controller

        self.fps_display = FPSDisplay(self)

        self.tick = 1 / 60


    def on_draw(self):
        # print("started rendering")
        self.clear()
        self.controller.update()
        get_physics_world().update(1)
        self.renderer.render()
        cameras["world"].follow(models["player"].x, models["player"].y)
        self.fps_display.draw()



    def on_key_press(self, symbol, modifiers):
        self.controller.handle_key_press(symbol, modifiers)

    def on_key_release(self, symbol, modifiers):
        self.controller.handle_key_release(symbol, modifiers)

    def on_mouse_press(self, x, y, button, modifiers):
        centered_x = x - self.width / 2
        centered_y = y - self.height / 2
        self.controller.handle_mouse_press(x, y, centered_x, centered_y, button, modifiers)

    def on_mouse_drag(self, x, y, dx, dy, button, modifiers):
        if button == mouse.LEFT:
            print(f'Dragged the mouse the mouse by ({dx}, {dy})')
        self.controller.handle_mouse_drag(x, y, button, modifiers)

    def on_mouse_scroll(self, x, y, scroll_x, scroll_y):
        print(f"Mouse scrolled ({scroll_x}, {scroll_y})")
        self.controller.handle_mouse_scroll(x, y, scroll_x, scroll_y)

    def on_resize(self, width, height):
        gl.glViewport(0, 0, *self.get_framebuffer_size())
        self.projection = Mat4.orthogonal_projection(0, width, 0, height, -255, 255)
        print(f'The window was resized to {width}, {height}')

    def on_move(self, x, y):
        print(f'Window moved to: ({x}, {y})')

    def on_close(self):
        print('goodbye')
        pyglet.app.exit()

    def on_file_drop(self, x, y, paths):
        print(f'dropped at ({x}, {y}): {paths}')
