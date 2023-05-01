from renderer.Renderer import *
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

def main():
    tick = 1 / 60
    last_update = time.time()

    window = Window(1280, 720, "Pyllium")
    set_window(window)
    glfw.make_context_current(get_window().window)

    controller = Controller()
    renderer = Renderer()
    physics_world = PhysicsWorld()

    set_controller(controller)
    set_renderer(renderer)
    set_physics_world(physics_world)

    load_scene()

    glfw.swap_interval(0)

    # Loop until the user closes the window
    while not glfw.window_should_close(get_window().window):
        starting_time = time.time()

        if starting_time > last_update + tick:
            last_update += tick
            get_physics_world().update(1)
            update_entities()

        get_controller().update()
        get_renderer().render()

        finish_time = time.time()
        elapsed_time = finish_time - starting_time

        # Swap front and back buffers
        glfw.swap_buffers(get_window().window)
        # Poll for and process events
        glfw.poll_events()

        # if elapsed_time != 0:
        #     print(1 / elapsed_time)
        # else:
        #     print("inf")

    glfw.terminate()


def update_entities():
    physics_bodies = get_physics_world().physics_bodies

    for model in models.values():
        if isinstance(model, Animation):
            model.update()

    for entity in entities.values():
        if entity.body != "" and entity.model != "":
            models[entity.model].place(physics_bodies[entity.body].x + physics_bodies[entity.body].width / 2, physics_bodies[entity.body].y + physics_bodies[entity.body].height / 2)

            entity.update(models[entity.model], physics_bodies[entity.body])

    if isinstance(cameras["world"], FollowCamera):
        target_x = models[entities[cameras["world"].target].model].x
        target_y = models[entities[cameras["world"].target].model].y

        cameras["world"].follow(target_x, target_y)



if __name__ == "__main__":
    main()
