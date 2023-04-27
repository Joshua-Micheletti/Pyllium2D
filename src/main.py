# import pyglet
# from window.Window import Window
from renderer.Renderer import *
# from shared import cameras
# from camera.Camera import FollowCamera
from controller.Controller import Controller
from scene import load_scene
# from PysicsWorld.PysicsWorld import PhysicsWorld
from shared import *

import glfw
from OpenGL.GL import *
from window.Window import Window

def main():
    window = Window(1280, 720, "Pyllium")
    set_window(window)
    glfw.make_context_current(get_window().window)

    controller = Controller()
    renderer = Renderer()

    set_controller(controller)
    set_renderer(renderer)

    load_scene()


    # Loop until the user closes the window
    while not glfw.window_should_close(get_window().window):
        # Render here, e.g. using pyOpenGL
        get_controller().update()
        get_renderer().render()


        # Swap front and back buffers
        glfw.swap_buffers(get_window().window)
        # Poll for and process events
        glfw.poll_events()

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
