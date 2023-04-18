

class PhysicsBody:

    def __init__(self, x = 0, y = 0, width = 1, height = 1, mass = 1, moving = True):
        print("new physics body")

        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.mass = mass
        self.movable = moving
        self.force = (0, 0)
        self.speed = (0, 0)

        self.center = (self.x + (self.width / 2), self.y + (self.height / 2))


    def move(self, x, y):
        self.x = self.x + x
        self.y = self.y + y

        self.center = (self.x + (self.width / 2), self.y + (self.height / 2))

    def push(self, x, y):
        self.force = (self.force[0] + x, self.force[1] + y)
