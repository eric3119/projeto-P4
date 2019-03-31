import pygame
from .loader import Loader

class Player():
    def __init__(self, sprite, screen_size):
        self.sprite = sprite
        self.xpos, self.ypos = (
            (screen_size[0]-sprite.get_width())//2,
            screen_size[1]-sprite.get_height()
            )
    
    def get_sprite_size(self):
        return (self.sprite.get_width(), self.sprite.get_height())
    
    def get_position(self):
        return (self.xpos, self.ypos)
    
    def update(self, direction):
        if direction == pygame.K_UP and self.ypos > 0:
            self.ypos -= 5
        elif direction == pygame.K_DOWN and self.ypos < 600:
            self.ypos += 5 
        elif direction == pygame.K_LEFT and self.xpos > 0:
            self.xpos -= 5 
        elif direction == pygame.K_RIGHT and self.xpos < 600:
            self.xpos += 5