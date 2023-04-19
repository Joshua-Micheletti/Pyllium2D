import pyglet
from window.Window import Window
from renderer.Renderer import Renderer
from shared import cameras
from camera.Camera import CenteredCamera
from controller.Controller import Controller
from scene import load_scene
from physics.PhysicsWorld import PhysicsWorld

if __name__ == "__main__":
    pyglet.options['degub_graphics_batch'] = False
    renderer = Renderer()
    physics_world = PhysicsWorld()
    controller = Controller()
    window = Window(1280, 720, renderer = renderer, controller = controller, physics_world = physics_world)
    load_scene()

    cameras["world"] = CenteredCamera(window, move_speed = 4)

    physics_world.collision_ray_rect(10, 40, 100, -10, 20, 10, 40, 20)


    pyglet.app.run()
