from OpenGL.GL import *
from shared import *
from pyrr import Matrix44

class Renderer():
    def __init__(self):
        glClearColor(0.1, 0.1, 0.1, 1.0)
        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

    def render(self):
        glClear(GL_COLOR_BUFFER_BIT)
        rm = get_resource_manager()


        for order in rm.rendering_buffer.keys():
            for shader in rm.rendering_buffer[order].keys():
                if shader == "basic":
                    basic_shader = rm.shaders["basic"]

                    glUseProgram(basic_shader.program)
                    glUniform1i(glGetUniformLocation(basic_shader.program, "texture_image"), 0)
                    glUniformMatrix4fv(glGetUniformLocation(basic_shader.program, "view"), 1, GL_FALSE, cameras["world"].view_matrix)
                    glUniformMatrix4fv(glGetUniformLocation(basic_shader.program, "projection"), 1, GL_FALSE, get_window().projection_matrix)

                for model in rm.rendering_buffer[order][shader]:
                    if collision_rect_rect(model.x - model.scale_x / 2, model.y - model.scale_y / 2, model.scale_x, model.scale_y, cameras["world"].x - get_window().width / 2, cameras["world"].y - get_window().height / 2, get_window().width, get_window().height):
                        rm.textures[model.texture].use()
                        glUniformMatrix4fv(glGetUniformLocation(rm.shaders[model.shader].program, "model"), 1, GL_FALSE, model.model_matrix)
                        glBindVertexArray(rm.meshes[model.mesh].vao)
                        glDrawArrays(GL_TRIANGLES, 0, rm.meshes[model.mesh].vertex_count)

        # for model in rm.models.values():
            # if collision_rect_rect(model.x - model.scale_x / 2, model.y - model.scale_y / 2, model.scale_x, model.scale_y, cameras["world"].x - 1280 / 2, cameras["world"].y - 720 / 2, 1280, 720):
            #     rm.textures[model.texture].use()
            #     # glUseProgram(shaders[model.shader].program)
            #     # glUniform1i(glGetUniformLocation(shaders[model.shader].program, "texture_image"), 0)
            #     # glUniformMatrix4fv(glGetUniformLocation(shaders[model.shader].program, "view"), 1, GL_FALSE, cameras["world"].view_matrix)
            #     glUniformMatrix4fv(glGetUniformLocation(rm.shaders[model.shader].program, "model"), 1, GL_FALSE, model.model_matrix)
            #     # glUniformMatrix4fv(glGetUniformLocation(shaders[model.shader].program, "projection"), 1, GL_FALSE, get_window().projection_matrix)
            #     glBindVertexArray(rm.meshes[model.mesh].vao)
            #     glDrawArrays(GL_TRIANGLES, 0, rm.meshes[model.mesh].vertex_count)


def collision_rect_rect(r1x, r1y, r1w, r1h, r2x, r2y, r2w, r2h):
        # are the sides of one rectangle touching the other?
        return (r1x + r1w >= r2x and # r1 right edge past r2 left
                r1x <= r2x + r2w and # r1 left edge past r2 right
                r1y + r1h >= r2y and # r1 top edge past r2 bottom
                r1y <= r2y + r2h)     # r1 bottom edge past r2 top
