import pyglet

physics_world = None
window = None
controller = None
renderer = None

models = dict()
meshes = dict()
shaders = dict()
textures = dict()
cameras = dict()
physics_bodies = dict()
groups = dict()
batch = pyglet.graphics.Batch()

def set_physics_world(obj):
    global physics_world
    physics_world = obj

def get_physics_world():
    global physics_world
    return physics_world

def get_window():
    global window
    return window

def set_window(obj):
    global window
    window = obj

def get_controller():
    global controller
    return controller

def set_controller(obj):
    global controller
    controller = obj

def get_renderer():
    global renderer
    return renderer

def set_renderer(obj):
    global renderer
    renderer = obj