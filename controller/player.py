import pygame
from .loader import Loader

class Player():
    def __init__(self, sprites, screen_size):
        self.sprites = sprites        
        self.sprite_index = 0
        
        self.xpos, self.ypos = (
            (screen_size[0]-sprites[0].get_width())//2,
            screen_size[1]-sprites[0].get_height()
            )
    
    def get_sprite_size(self):
        return (self.sprites[0].get_width(), self.sprites[0].get_height())
    
    def get_sprite(self):
        return self.sprites[self.sprite_index]
    
    def get_position(self):
        return (self.xpos, self.ypos)
    
    def update(self, direction):

        self.sprite_index += 1
        self.sprite_index %= len(self.sprites)

        if direction == pygame.K_UP and self.ypos > 0:
            self.ypos -= 5
        elif direction == pygame.K_DOWN and self.ypos < 600:
            self.ypos += 5 
        elif direction == pygame.K_LEFT and self.xpos > 0:
            self.xpos -= 5 
        elif direction == pygame.K_RIGHT and self.xpos < 600:
            self.xpos += 5