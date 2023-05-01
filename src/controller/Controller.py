from shared import *

import glfw
import time

class Controller:
    """Class for handling inputs from the user\n
    Controller()"""

    def __init__(self):
        self.states = dict()

        self.states["camera_left"] = False
        self.states["camera_right"] = False
        self.states["camera_up"] = False
        self.states["camera_down"] = False

        self.states["player_up"] = False
        self.states["player_down"] = False
        self.states["player_left"] = False
        self.states["player_right"] = False
        self.states["player_jumping"] = False

        self.states["display_bounding_box"] = False

        self.player_movement_speed = 50
        self.player_jumping_strength = 30
        self.camera_movement_speed = 40

        self.can_jump = True

        self.last_update = time.time()


    def handle_key_press(self, symbol, modifiers):
        if symbol == glfw.KEY_A:
            self.states["camera_left"] = True

        if symbol == glfw.KEY_S:
            self.states["camera_down"] = True

        if symbol == glfw.KEY_D:
            self.states["camera_right"] = True

        if symbol == glfw.KEY_W:
            self.states["camera_up"] = True


        if symbol == glfw.KEY_UP:
            self.states["player_up"] = True

        if symbol == glfw.KEY_DOWN:
            self.states["player_down"] = True

        if symbol == glfw.KEY_LEFT:
            self.states["player_left"] = True

        if symbol == glfw.KEY_RIGHT:
            self.states["player_right"] = True


        if symbol == glfw.KEY_SPACE:
            self.states["player_jumping"] = True


        if symbol == glfw.KEY_B and self.states["display_bounding_box"] == False:
            self.states["display_bounding_box"] = True

        elif symbol == glfw.KEY_B and self.states["display_bounding_box"] == True:
            self.states["display_bounding_box"] = False


    def handle_key_release(self, symbol, modifiers):
        if symbol == glfw.KEY_A:
            self.states["camera_left"] = False

        if symbol == glfw.KEY_S:
            self.states["camera_down"] = False

        if symbol == glfw.KEY_D:
            self.states["camera_right"] = False

        if symbol == glfw.KEY_W:
            self.states["camera_up"] = False


        if symbol == glfw.KEY_UP:
            self.states["player_up"] = False

        if symbol == glfw.KEY_DOWN:
            self.states["player_down"] = False

        if symbol == glfw.KEY_LEFT:
            self.states["player_left"] = False

        if symbol == glfw.KEY_RIGHT:
            self.states["player_right"] = False

        if symbol == glfw.KEY_SPACE:
            self.states["player_jumping"] = False


    # def handle_mouse_scroll(self, x, y, scroll_x, scroll_y):
    #     if scroll_y > 0:
    #         cameras["world"].set_zoom(cameras["world"].zoom + 0.1)
    #     if scroll_y < 0:
    #         cameras["world"].set_zoom(cameras["world"].zoom - 0.1)


    # def handle_mouse_drag(self, x, y, button, modifiers):
    #     pass


    # def handle_mouse_press(self, x, y, centered_x, centered_y, button, modifiers):
    #     print(f"pressed a mouse button at ({x}, {y})")

    #     for item in models.items():
    #         name = item[0]
    #         model = item[1]

    #         if not isinstance(model, Sprite):
    #             continue

    #         screen_coords = Vec4(x, y, 0, 0)

    #         world_x = centered_x + cameras["world"].offset_x
    #         world_y = centered_y + cameras["world"].offset_y

    #         if world_x > model.center[0] + (model.width / 2):
    #             continue

    #         if world_x < model.center[0] - (model.width / 2):
    #             continue

    #         if world_y > model.center[1] + (model.height / 2):
    #             continue

    #         if world_y < model.center[1] - (model.height / 2):
    #             continue

    #         print(name, model.x, model.y, model.width, model.height, model.center)



    def update(self):
        dt = time.time() - self.last_update
        self.last_update = time.time()

        if self.states["camera_left"] == True:
            cameras["world"].move(-self.camera_movement_speed * dt, 0)

        if self.states["camera_right"] == True:
            cameras["world"].move(self.camera_movement_speed  * dt, 0)

        if self.states["camera_up"] == True:
            cameras["world"].move(0, self.camera_movement_speed * dt)

        if self.states["camera_down"] == True:
            cameras["world"].move(0, -self.camera_movement_speed * dt)


        physics_world = get_physics_world()

        if self.states["player_up"] == True:
            physics_world.physics_bodies[entities["player"].body].push(0, self.player_movement_speed * 3 * dt)

        if self.states["player_down"] == True:
            physics_world.physics_bodies[entities["player"].body].push(0, -self.player_movement_speed * dt)
            entities["player"].states["crouching"] = True
        else:
            entities["player"].states["crouching"] = False

        if self.states["player_left"] == True:
            physics_world.physics_bodies[entities["player"].body].push(-self.player_movement_speed * dt, 0)

        if self.states["player_right"] == True:
            physics_world.physics_bodies[entities["player"].body].push(self.player_movement_speed * dt, 0)

        if self.states["player_jumping"] == True and physics_world.physics_bodies["player"].touching["down"] and self.can_jump:
            physics_world.physics_bodies["player"].push(0, self.player_jumping_strength)
            self.can_jump = False

        if physics_world.physics_bodies["player"].touching["down"] == False:
            self.can_jump = True

        set_physics_world(physics_world)
