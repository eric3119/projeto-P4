import pygame

class Shot:
    ''' projeteis disparados pela nave '''
    def __init__(self, sprite):
                
        self.sprite = sprite

        #############
        ## controle do delay dos disparos
        ######
        self.delta = 100 # tempo de duração do delay
        self.start_time = 0 # tempo do ultimo disparo
        
        # self.max_speed = 5
        
        self.step = sprite.get_height()
        
        ##############
        ## retangulos para detecção de colisões
        #######
        self.rects = []
    
    def trigger(self, position):
        ''' gera novos disparos baseado no delay '''
        if (pygame.time.get_ticks() - self.start_time) >= self.delta:
            self.start_time = pygame.time.get_ticks()

            new_rect = self.sprite.get_rect()
            new_rect.x, new_rect.y = position
            
            self.rects.append({
                'rect':new_rect,
                'dead':False,
            })

    def get_sprite_size(self):
        return (self.sprite.get_width(), self.sprite.get_height())

    def destroy(self, rect):
        ''' marca um disparo para ser destruido se saiu da tela ou se colidiu '''
        i = self.rects.index(rect)
        self.rects[i]['dead'] = True
    
    def alive(self, rect):        
        return not rect['dead']

    def isOnScreen(self, item):
        ''' verifica se não foi destruido ou se saiu da tela '''
        return True if item['rect'].y >= 0 and not item['dead'] else False

    def update(self):
        ''' atualiza as posições '''
        for i in range(len(self.rects)):
            self.rects[i]['rect'].x, self.rects[i]['rect'].y = (self.rects[i]['rect'].x, self.rects[i]['rect'].y-self.step)
        
        # remove os que colidiram ou sairam da tela
        self.rects = list(filter(lambda x: self.isOnScreen(x), self.rects))