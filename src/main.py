from renderer.Renderer import *
from controller.Controller import Controller
from scene import load_scene
from PysicsWorld.PysicsWorld import PhysicsWorld
from shared import *

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

        if time.time() > last_update + tick:
            last_update += tick
            get_controller().update(tick)
            get_physics_world().update(1)
            link_all_model_physics_body()

            for model in models.values():
                if isinstance(model, Animation):
                    model.update()

        get_renderer().render()

        finish_time = time.time()
        elapsed_time = finish_time - starting_time        

        # Swap front and back buffers
        glfw.swap_buffers(get_window().window)
        # Poll for and process events
        glfw.poll_events()

        if elapsed_time != 0:
            print(1 / elapsed_time)
        else:
            print("inf")

            # print(1 / (finish_time - starting_time))

    glfw.terminate()

if __name__ == "__main__":
    main()



    # # pyglet.options['degub_graphics_batch'] = False
    # pyglet.options['debug_gl'] = False
    # pyglet.options['vsync'] = True

    # renderer = Renderer()
    # physics_world = PhysicsWorld()

    # set_physics_world(physics_world)

    # controller = Controller()
    # window = Window(1280, 720, renderer = renderer, controller = controller)
    # load_scene()

    # cameras["world"] = FollowCamera(window, move_speed = 4)

    # pyglet.app.run(interval = 1 / 60)
