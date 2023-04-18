from shared import physics_bodies
from pyglet.math import Vec2

class PhysicsWorld:

    def __init__(self):
        print("new physics world")
        self.collision_solve_speed = 0.01
        self.gravity = 1
        self.friction = 0.5

    def update(self, sub_steps = 1):
        for body in physics_bodies.values():
            if body.movable:
                # calculate the forces applied on the X and Y components, according to air friction, velocity, mass and gravity
                totalForceX = body.force[0] + (self.friction * (-body.speed[0]))
                totalForceY = body.force[1] + (self.friction * (-body.speed[1])) - (body.mass * self.gravity)
                # calculate the acceleration by the formula: "a = F / m"
                acceleration_x = totalForceX / body.mass
                acceleration_y = totalForceY / body.mass
                # update the velocity according to the acceleration
                body.speed = (body.speed[0] + acceleration_x, body.speed[1] + acceleration_y)
                # update the position according to the velocity
                body.x += body.speed[0]
                body.y += body.speed[1]
                # reset the current force on the body
                body.force = (0, 0)


        for i in range(sub_steps):
            for body_1 in physics_bodies.values():
                for body_2 in physics_bodies.values():
                    if body_1 != body_2:
                        self.solve_collision(body_1, body_2)

    def solve_collision(self, body_1, body_2):

        if self.collision_rect_rect(body_1.x, body_1.y, body_1.width, body_1.height,
                                    body_2.x, body_2.y, body_2.width, body_2.height):
            if body_1.movable:
                distance = Vec2(body_1.center[0], body_1.center[1]) - Vec2(body_2.center[0], body_2.center[1])
                body_1.move(distance.x * self.collision_solve_speed, distance.y * self.collision_solve_speed)


    def collision_rect_rect(self, r1x, r1y, r1w, r1h, r2x, r2y, r2w, r2h):
        # are the sides of one rectangle touching the other?
        return (r1x + r1w >= r2x and # r1 right edge past r2 left
                r1x <= r2x + r2w and # r1 left edge past r2 right
                r1y + r1h >= r2y and # r1 top edge past r2 bottom
                r1y <= r2y + r2h)     # r1 bottom edge past r2 top
