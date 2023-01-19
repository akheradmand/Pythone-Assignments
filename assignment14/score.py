import arcade

class Score(arcade.Sprite):
    def __init__(self,game):
        super().__init__()
        self.center_x=9*game.width//10
        self.center_y=20
        self.game_score=game.score
        
    def draw(self):
        arcade.draw_text(self.game_score,self.center_x,self.center_y,arcade.color.RED,20)