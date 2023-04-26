import pyglet
from window.Window import Window
from renderer.Renderer import Renderer
from shared import cameras
from camera.Camera import FollowCamera
from controller.Controller import Controller
from scene import load_scene
from PysicsWorld.PysicsWorld import PhysicsWorld
from shared import *

if __name__ == "__main__":

    # pyglet.options['degub_graphics_batch'] = False
    pyglet.options['debug_gl'] = False
    pyglet.options['vsync'] = True

    renderer = Renderer()
    physics_world = PhysicsWorld()

    set_physics_world(physics_world)

    controller = Controller()
    window = Window(1280, 720, renderer = renderer, controller = controller)
    load_scene()

    cameras["world"] = FollowCamera(window, move_speed = 4)

    pyglet.app.run(interval = 1 / 60)
