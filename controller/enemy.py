from .game import SCREEN_SIZE
import random

class Enemy:

    def __init__(self, sprites):
        self.enemies = []
        
        self.sprites = sprites
        self.sprite_index = 0

        self.anim_time = 200
        self.anim_control = 0

        self.delta = 1000
        self.start_time = 0
        self.max_speed = 5
        self.max_qtd = 5
        self.step = 3

        self.rect = self.sprites[0].get_rect()

    def destroy(self):
        self.onScreen = False

    def trigger(self, clock_ticks):
        if self.max_qtd <= len(self.enemies):
            return
        # speed=(random.random()+1)*max_speed
        if (clock_ticks - self.start_time) >= self.delta:
            self.start_time = clock_ticks
            self.enemies.append(
                    (
                        random.random()*(SCREEN_SIZE[1]-self.sprites[0].get_width()),
                        0, 
                    )
                )
    
    def isOnScreen(self, position):
        return True if position[1] < SCREEN_SIZE[1] else False
    
    def get_sprite(self):
        return self.sprites[self.sprite_index]

    def get_sprite_size(self):
        return (self.sprites.get_width()[0], self.sprites.get_height()[0])

    def update(self, clock_ticks):
        
        self.trigger(clock_ticks)
        if (clock_ticks - self.anim_control) >= self.anim_time:
            self.anim_control = clock_ticks
            self.sprite_index += 1
            self.sprite_index %= len(self.sprites)

        for i in range(len(self.enemies)):
            self.enemies[i] = (self.enemies[i][0], self.enemies[i][1]+self.step)
        
        self.enemies = list(filter(lambda x: self.isOnScreen(x), self.enemies))