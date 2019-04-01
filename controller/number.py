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
        self.max_length = 4
        self.step = 2
        self.missed = False
    
    def trigger(self):

        self.x = random.random()
        self.x = int(self.x*5)
        self.y = random.random()
        self.y = int(self.y*4)
        self.result = self.x + self.y

        value = self.result
        for x in range(self.max_length):
            randx = random.random()*(SCREEN_SIZE[0]-self.sprites[0].get_width())
            randy = random.random()*100 - 100
            new_rect = self.sprites[value].get_rect()
            new_rect.x, new_rect.y = (randx,randy)
            self.rects.append({
                'rect':new_rect,
                'dead':False,
                'value':value,
            })
            value = int(random.random()*5)

        
    def get_sprite_size(self):
        pass
    
    def get_sprite(self, value):
        return self.sprites[value]

    def destroy(self, rect):
        i = self.rects.index(rect)
        self.rects[i]['dead'] = True        

    def isOnScreen(self, item):
        return True if item['rect'].y < SCREEN_SIZE[1] and not item['dead'] else False

    def update(self):        
        if self.answered:
            self.answered = False
            self.trigger()
        elif len(self.rects) == 0:            
            self.trigger()
            self.missed = True
            
        
        for item in self.rects:            
            item['rect'].x, item['rect'].y = (item['rect'].x, item['rect'].y+self.step)
        
        self.rects = list(filter(lambda x: self.isOnScreen(x), self.rects))
    
    def get_expression(self):
        return '{} {} {} = ?'.format(self.x, self.op, self.y)
    
    def is_answer(self, num):
        if num == self.result:
            self.answered = True
        return self.answered
    
    def missed_answer(self):
        if self.missed:
            self.missed = False
            return True
        
        return False