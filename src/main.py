from renderer.Renderer import *
from renderer.ResourceManager import ResourceManager
from controller.Controller import Controller
from scene import load_scene
from PysicsWorld.PysicsWorld import PhysicsWorld
from shared import *
from camera.Camera import FollowCamera

import glfw
from OpenGL.GL import *
from window.Window import Window
from utils import *
from model.animation.Animation import Animation

import time

import math

def main():
    tick = 1 / 60
    print_tick = 1 / 1
    last_update = time.time()
    last_print = time.time()

    window = Window(1280, 720, "Pyllium")
    set_window(window)
    glfw.make_context_current(get_window().window)

    controller = Controller()
    renderer = Renderer()
    physics_world = PhysicsWorld()
    physics_world.gravity = 10
    physics_world.friction = 2

    resource_manager = ResourceManager()

    set_controller(controller)
    set_renderer(renderer)
    set_physics_world(physics_world)
    set_resource_manager(resource_manager)

    load_scene()

    glfw.swap_interval(0)

    # Loop until the user closes the window
    while not glfw.window_should_close(get_window().window):
        starting_time = time.time()

        if starting_time > last_update + tick:
            last_update += tick
            get_controller().update()
            get_physics_world().update()
            update_entities()


        get_renderer().render()

        # Swap front and back buffers
        glfw.swap_buffers(get_window().window)
        # Poll for and process events
        glfw.poll_events()


        if starting_time > last_print + print_tick:
            last_print += print_tick

            finish_time = time.time()
            elapsed_time = finish_time - starting_time

            if elapsed_time != 0:
                print(f"FPS: {math.trunc(1 / elapsed_time)}  FT: {math.trunc(elapsed_time * 100000) / 100}")
            else:
                print("inf")

    glfw.terminate()


def update_entities():
    physics_bodies = get_physics_world().physics_bodies
    rm = get_resource_manager()

    for model in rm.models.values():
        if isinstance(model, Animation):
            model.update()

    for entity in entities.values():
        if entity.body != "" and entity.model != "" and physics_bodies[entity.body].movable:
            rm.models[entity.model].place(physics_bodies[entity.body].x + physics_bodies[entity.body].width / 2, physics_bodies[entity.body].y + physics_bodies[entity.body].height / 2)
            entity.update(rm.models[entity.model], physics_bodies[entity.body])

    if isinstance(cameras["world"], FollowCamera):
        target_x = rm.models[entities[cameras["world"].target].model].x
        target_y = rm.models[entities[cameras["world"].target].model].y

        cameras["world"].follow(target_x, target_y)



if __name__ == "__main__":
    main()
