from shared import *

def link_all_model_physics_body():
    physics_bodies = get_physics_world().physics_bodies

    for name in models.keys():
        body = models[name].body
        if models[name].body is not None and len(models[name].body) != 0:
            models[name].place(physics_bodies[body].x + physics_bodies[body].width / 2, physics_bodies[body].y + physics_bodies[body].height / 2)
