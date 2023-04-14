import pyglet
from window.Window import Window
from renderer.Renderer import Renderer
from shared import cameras
from camera.Camera import CenteredCamera
from controller.Controller import Controller
from scene import load_scene

if __name__ == "__main__":
    pyglet.options['degub_graphics_batch'] = False
    renderer = Renderer()
    controller = Controller()
    window = Window(1280, 720, renderer = renderer, controller = controller)
    load_scene()

    cameras["world"] = CenteredCamera(window, move_speed = 4)
    pyglet.app.run()
