from model.Sprite import Sprite

class StaticSprite(Sprite):

    def __init__(self, path, group):
        print("new static sprite")

        Sprite.__init__(self, path, group)
        
