import pygame
import random
from .game import SCREEN_SIZE

class Number:
    
    def __init__(self, sprites):
        self.rects=[]
        self.sprites = sprites
        self.x=0
        self.y=0
        self.op='+'
        self.result = 0
        self.answered = True
        self.max_length = 5
        self.step = 2
    
    def trigger(self):
        print(self.sprites)
        self.x = random.random()
        self.x = int(self.x*10)
        self.y = random.random()
        self.y = int(self.y*10)
        self.result = self.x + self.y

        value = self.result

        randNum = random.random()*(SCREEN_SIZE[1]-self.sprites[0].get_width())            
        new_rect = self.sprites[value].get_rect()
        new_rect.x, new_rect.y = (randNum,0)
        self.rects.append({
            'rect':new_rect,
            'dead':False,
            'value':value,
        })

        
    def get_sprite_size(self):
        pass
    
    def get_sprite(self, value):
        return self.sprites[value]

    def destroy(self):
        pass

    def isOnScreen(self, item):
        return True if item['rect'].y < SCREEN_SIZE[1] and not item['dead'] else False

    def update(self):
        if self.answered:
            self.answered = False
            self.trigger()
        
        for i in range(len(self.rects)):
            # self.enemies[i] = (self.enemies[i][0], self.enemies[i][1]+self.step)
            self.rects[i]['rect'].x, self.rects[i]['rect'].y = (self.rects[i]['rect'].x, self.rects[i]['rect'].y+self.step)
        
        # self.enemies = list(filter(lambda x: self.isOnScreen(x) and self.alive(x), self.enemies))
            self.rects = list(filter(lambda x: self.isOnScreen(x), self.rects))
    
    def get_expression(self):
        return '{} {} {} = ?'.format(self.x, self.op, self.y)
    
    def is_answer(self, num):
        return num == self.result