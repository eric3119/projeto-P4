import pygame
from .loader import Loader
from .game import SCREEN_SIZE

class Player():
    def __init__(self, sprites):
        self.sprites = sprites        
        self.sprite_index = 0
        
        self.step = 10

        self.xpos, self.ypos = (
            (SCREEN_SIZE[0]-sprites[0].get_width())//2,
            SCREEN_SIZE[1]-sprites[0].get_height()
            )
        
        self.rect = self.sprites[0].get_rect()
    
    def get_sprite_size(self):
        return (self.sprites[0].get_width(), self.sprites[0].get_height())
    
    def get_sprite(self):
        return self.sprites[self.sprite_index]
    
    def get_position(self):
        return (self.xpos, self.ypos)
    
    def collide(self):
        pass
    
    def update(self, direction):

        self.sprite_index += 1
        self.sprite_index %= len(self.sprites)

        if direction == pygame.K_UP and self.ypos > 0:
            self.ypos -= self.step
        elif direction == pygame.K_DOWN and self.ypos < SCREEN_SIZE[1]-self.sprites[0].get_height():
            self.ypos += self.step 
        elif direction == pygame.K_LEFT and self.xpos > 0:
            self.xpos -= self.step 
        elif direction == pygame.K_RIGHT and self.xpos < SCREEN_SIZE[0]-self.sprites[0].get_width():
            self.xpos += self.step
        
        (self.rect.x, self.rect.y) = (self.xpos, self.ypos)