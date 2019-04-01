import pygame
from .loader import Loader
from .game import SCREEN_SIZE

class Player():
    def __init__(self, sprites):
        self.sprites = sprites        
        self.sprite_index = 0 # indice do loop da animação
        self.anim_control = 0
        self.anim_delta = 10

        self.health = 5
        self.shield_time = 0
        self.delta = 2000
        
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
    
    def is_shield(self):
        return (pygame.time.get_ticks() - self.shield_time) < self.delta
    
    def get_position(self):
        return (self.xpos, self.ypos)
    
    def collide(self):
        if (pygame.time.get_ticks() - self.shield_time) >= self.delta:
            self.health-=1
            self.shield_time = pygame.time.get_ticks()            
    
    def update(self, direction):
        
        if (pygame.time.get_ticks() - self.anim_control) >= self.anim_delta:
            self.anim_control = pygame.time.get_ticks()
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

    def is_alive(self):
        return True if self.health > 0 else False