import pyglet

physics_world = None
window = None
models = dict()
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
