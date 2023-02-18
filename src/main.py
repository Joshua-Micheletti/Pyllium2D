import pyglet
from window.Window import Window
from renderer.Renderer import Renderer
from shared import cameras
from camera.Camera import Camera

pyglet.options['degub_graphics_batch'] = False

renderer = Renderer()
window = Window(1280, 720, renderer = renderer)

renderer.loadModelsIntoBatch()

cameras["world"] = Camera()


if __name__ == "__main__":
    pyglet.app.run()
    