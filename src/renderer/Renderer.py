# from pyglet.gl import *
# import pyglet
# from shared import models
# from shared import cameras
# from shared import batch
# from shared import groups
# from shared import *
# # from mesh.Mesh import Model
# # from mesh.dynamic.DynamicSprite import DynamicSprite
# from pyglet.graphics.shader import Shader, ShaderProgram

from OpenGL.GL import *
from shared import *
from pyrr import Matrix44

class Renderer():
    def __init__(self):
        glClearColor(0.1, 0.1, 0.1, 1.0)
        # groups["background"] = pyglet.graphics.Group(order = 0)
        # groups["foreground"] = pyglet.graphics.Group(order = 1)
        # groups["debug"] = pyglet.graphics.Group(order = 2)
        # groups["debug"].visible = False

    def render(self):
        glClear(GL_COLOR_BUFFER_BIT)

        for model in models.values():
            textures[model.texture].use()
            glUseProgram(shaders[model.shader].program)
            glUniform1i(glGetUniformLocation(shaders[model.shader].program, "texture_image"), 0)
            glUniformMatrix4fv(glGetUniformLocation(shaders[model.shader].program, "view"), 1, GL_FALSE, cameras["world"].view_matrix)
            glUniformMatrix4fv(glGetUniformLocation(shaders[model.shader].program, "model"), 1, GL_FALSE, model.model_matrix)
            glUniformMatrix4fv(glGetUniformLocation(shaders[model.shader].program, "projection"), 1, GL_FALSE, get_window().projection_matrix)
            glBindVertexArray(meshes[model.mesh].vao)
            glDrawArrays(GL_TRIANGLES, 0, meshes[model.mesh].vertex_count)


        # global batch
        # global cameras

        # bodies = get_physics_world().physics_bodies

        # for name in bodies.keys():
        #     if name in models.keys():
        #         models[name].place(bodies[name].x, bodies[name].y)

        # for name in models.keys():
        #     if isinstance(models[name], DynamicSprite):
        #         models[name].update_state(bodies[name])

            # screen_width = 1280
            # screen_height = 720
            # print(name)
            # if models[name].x >= -cameras["world"].offset_x + screen_width / 2 or models[name].x + models[name].width <= -cameras["world"].offset_x - screen_width / 2 or models[name].y + models[name].height >= -cameras["world"].offset_y + screen_height / 2 or models[name].y <= -cameras["world"].offset_y - screen_height / 2:
            #     models[name].sprite.group = groups["debug"]
            # else:
            #     models[name].sprite.group = groups["background"]

            # int positionX = i * this.tileSize - (this.tileSize * (world.length / 2));
			# int positionY = j * this.tileSize - (this.tileSize * (world[0].length / 2));
            #
			# // check if the current tile is visible by the camera
			# if (positionX - this.tileSize / 2 >= -this.camera.getX() + this.w / 2 ||
			# 	positionX + this.tileSize / 2 <= -this.camera.getX() - this.w / 2 ||
			# 	positionY - this.tileSize / 2 >= -this.camera.getY() + this.h / 2 ||
			# 	positionY + this.tileSize / 2 <= -this.camera.getY() - this.h / 2) {
			# }



        # with cameras["world"]:
        #     batch.draw()
