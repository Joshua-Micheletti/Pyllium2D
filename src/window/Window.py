import pyglet
from pyglet.window import key
from pyglet.window import mouse
from pyglet.window import FPSDisplay
from pyglet import gl
from pyglet.math import Mat4
from renderer.Renderer import Renderer
from controller.Controller import Controller
from shared import cameras




class Window(pyglet.window.Window):
    def __init__(self, width = 1280, height = 720, resizable = True, min_w = 400, min_h = 300, max_w = 1920, max_h = 1080, renderer = Renderer(), controller = Controller()):
        # self.customContext = gl.Config()
        # self.customContext.stencil_size = 8
        # self.customContext.aux_buffers = 4
        
        super().__init__(width, height, resizable = resizable)
        self.set_minimum_size(min_w, min_h)
        self.set_maximum_size(max_w, max_h)
        
        self.renderer = renderer
        self.controller = controller
        
        self.fps_display = FPSDisplay(self)
        
    def on_draw(self):
        self.controller.update()
        self.clear()
        self.renderer.render()
        self.fps_display.draw()

    def on_key_press(self, symbol, modifiers):
        if symbol == key.A:
            self.controller.handle_input("A_down")
        if symbol == key.S:
            self.controller.handle_input("S_down")
        if symbol == key.D:
            self.controller.handle_input("D_down")
        if symbol == key.W:
            self.controller.handle_input("W_down")
        
        if symbol == key.LEFT:
            print('The left arrow key was pressed.')
        if symbol == key.ENTER:
            print('The enter key was pressed.')
            
    def on_key_release(self, symbol, modifiers):
        if symbol == key.A:
            self.controller.handle_input("A_up")
        if symbol == key.S:
            self.controller.handle_input("S_up")
        if symbol == key.D:
            self.controller.handle_input("D_up")
        if symbol == key.W:
            self.controller.handle_input("W_up")
            
    def on_mouse_press(self, x, y, button, modifiers):
        if button == mouse.LEFT:
            print('The left mouse button was pressed.')
            
    def on_mouse_drag(self, x, y, dx, dy, button, modifiers):
        if button == mouse.LEFT:
            print(f'Dragged the mouse the mouse by ({dx}, {dy})')

    def on_mouse_scroll(self, x, y, scroll_x, scroll_y):
        print(f"Mouse scrolled ({scroll_x}, {scroll_y})")
        if scroll_y > 0:
            self.controller.handle_input("scroll_up")
        else:
            self.controller.handle_input("scroll_down")
            
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
        