from .game import SCREEN_SIZE
import random

class Enemy:

    def __init__(self, sprites):
        
        self.sprites = sprites
        
        #############
        ## controle do loop da animação
        ######
        self.sprite_index = 0
        self.anim_time = 200
        self.anim_control = 0

        #############
        ## controle do delay de geração de inimigos
        ######
        self.delta = 1000 # tempo de duração do delay
        self.start_time = 0 # tempo do ultimo gerado
        
        #self.max_speed = 5

        self.max_qtd = 5 # quantidade de inimigos na tela
        self.step = 3 # quantidade de avanço de pixels

        self.dead_num = 0 # quantidade de inimigos destruidos

        ##############
        ## retangulos para detecção de colisões
        #######
        self.rects = []

    def destroy(self, rect):
        ''' marca um inimigo eliminado para ser destruido '''
        i = self.rects.index(rect)
        self.rects[i]['dead'] = True
        self.dead_num += 1
    
    def alive(self, rect):
        return not rect['dead']

    def trigger(self, clock_ticks):
        ''' gera novos inimigos '''
        
        ## verifica o limite de inimigos na tela
        if self.max_qtd <= len(self.rects): 
            return
        
        ## delay para controlar a velocidade com que
        # os inimigos aparecem
        if (clock_ticks - self.start_time) >= self.delta:
            self.start_time = clock_ticks
            randNum = random.random()*(SCREEN_SIZE[1]-self.sprites[0].get_width())            
            new_rect = self.sprites[0].get_rect()
            new_rect.x, new_rect.y = (randNum,0)
            self.rects.append({
                'rect':new_rect,
                'dead':False,
            })            
    
    # def isOnScreen(self, position):
    #     return True if position[1] < SCREEN_SIZE[1] else False
    
    def isOnScreen(self, item):
        ''' verifica se não foi destruido ou se saiu da tela '''
        return True if item['rect'].y < SCREEN_SIZE[1] and not item['dead'] else False
    
    def get_sprite(self):
        return self.sprites[self.sprite_index]

    def get_sprite_size(self):
        return (self.sprites.get_width()[0], self.sprites.get_height()[0])

    def update(self, clock_ticks):
        ''' atualiza as posições e o estado das animações '''
        self.trigger(clock_ticks) # tenta gerar um novo inimigo

        ##############
        ## atualização da animação
        #######
        # delay de atualização da animação
        if (clock_ticks - self.anim_control) >= self.anim_time:
            self.anim_control = clock_ticks
            self.sprite_index += 1
            self.sprite_index %= len(self.sprites)

        ##############
        ## atualização da posição atual
        #######
        for i in range(len(self.rects)):
            self.rects[i]['rect'].x, self.rects[i]['rect'].y = (self.rects[i]['rect'].x, self.rects[i]['rect'].y+self.step)
        
        # remove inimigos marcados ou que sairam da tela
        self.rects = list(filter(lambda x: self.isOnScreen(x), self.rects))