import arcade
from bullet import Bullet

class Spaceship(arcade.Sprite):
    def __init__(self,game):
        super().__init__(":resources:images/space_shooter/playerShip1_blue.png")
        self.center_x= game.width//2
        self.center_y= game.height//10
        self.change_x=0
        self.change_y=0
        self.width=48 # dimension of object
        self.height=48
        self.speed=6
        self.game_width=game.width
        self.bullet_list=[]
        self.score=0

    def move(self):
        if self.change_x==-1:
            if self.center_x > 0:
                self.center_x -=self.speed
        elif self.change_x==1:
            if self.center_x < self.game_width:
                self.center_x +=self.speed
                
    def fire(self):
        new_bullet=Bullet(self)
        self.bullet_list.append(new_bullet)