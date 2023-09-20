import random
import arcade

class Enemy(arcade.Sprite):
    def __init__(self,game):
        super().__init__(":resources:images/space_shooter/playerShip1_orange.png")
        self.center_x=random.randint(0,game.width)
        self.center_y=game.height+24
        self.angle=180
        self.width=48
        self.height=48
        self.speed=2
        self.speed_raising=0.01

    def move(self):
        self.center_y -=self.speed
        self.speed=self.speed*(self.speed_raising+1)
        # print(self.speed)