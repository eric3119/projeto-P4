import pygame
import random
from .game import SCREEN_SIZE

class Number:
    
    def __init__(self, sprites):
        ##############
        ## retangulos para detecção de colisões
        #######
        self.rects=[]

        self.sprites = sprites

        ##############
        ## variaveis das operações
        #######
        self.x=0
        self.y=0
        self.op='+'
        self.result = 0 
        #########
        
        self.answered = True        
        self.missed = False 
        self.max_length = 4 # maximo de numeros na tela
        self.step = 2 # quantidade de avanço de pixels
    
    def trigger(self):
        ''' limpa as variaveis e gera uma nova expressão matematica '''
        self.rects = []
        self.x = random.random()
        self.x = int(self.x*5)
        self.y = random.random()
        self.y = int(self.y*4)
        self.result = self.x + self.y

        value = self.result
        for x in range(self.max_length):
            randx = random.random()*(SCREEN_SIZE[0]-self.sprites[0].get_width())
            randy = random.random()*100 - 1000
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
        ''' marca um numero para ser destruido se saiu da tela ou se colidiu '''
        i = self.rects.index(rect)
        self.rects[i]['dead'] = True        

    def isOnScreen(self, item):
        ''' verifica se não foi destruido ou se saiu da tela '''
        return True if item['rect'].y < SCREEN_SIZE[1] and not item['dead'] else False

    def update(self):
        ''' checa se obteve o resultado e atualiza as posições '''
        if self.answered:
            self.answered = False
            self.trigger()
        elif len(self.rects) == 0:            
            self.trigger()
            self.missed = True
            
        ##############
        ## atualização da posição atual
        #######
        for item in self.rects:            
            item['rect'].x, item['rect'].y = (item['rect'].x, item['rect'].y+self.step)
        
        # remove os que colidiram ou sairam da tela
        self.rects = list(filter(lambda x: self.isOnScreen(x), self.rects))
    
    def get_expression(self):
        ''' retorna a string da expressão '''
        return '{} {} {} = ?'.format(self.x, self.op, self.y)
    
    def is_answer(self, num):
        ''' verifica se num é um resultado '''
        if num == self.result:
            self.answered = True
        return self.answered
    
    def missed_answer(self):
        ''' verifica se a resposta não foi obtida '''
        if self.missed:
            self.missed = False
            return True
        
        return False