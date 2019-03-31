import pygame
###player.xpos + player_width, 
###player.ypos + (player_height//2 - shot_img.get_height()//2
class Shot:
    
    def __init__(self, sprite):
        self.shots = []
        self.sprite = sprite
    
    def trigger(self, position):
        self.shots.append(position)

    def destroy(self):
        self.onScreen = False

    def isOnScreen(self, position):
        return True if position[1] >= 0 else False

    def update(self):
        for i in range(len(self.shots)):
            self.shots[i] = (self.shots[i][0], self.shots[i][1]-10)
        
        self.shots = list(filter(lambda x: self.isOnScreen(x), self.shots))        