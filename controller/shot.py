import pygame
###player.xpos + player_width, 
###player.ypos + (player_height//2 - shot_img.get_height()//2
class Shot:
    
    def __init__(self, sprite):
        self.shots = []
        self.rects = []
        
        self.sprite = sprite

        self.delta = 100
        self.start_time = 0
        self.max_speed = 5
        self.step = sprite.get_height()

        self.rect = self.sprite.get_rect()        
    
    def trigger(self, position):
        
        if (pygame.time.get_ticks() - self.start_time) >= self.delta:
            self.start_time = pygame.time.get_ticks()
            # self.shots.append(position)
            new_rect = self.sprite.get_rect()
            new_rect.x, new_rect.y = position
            
            self.rects.append({
                'rect':new_rect,
                'dead':False,
            })

    def get_sprite_size(self):
        return (self.sprite.get_width(), self.sprite.get_height())

    def destroy(self, rect):
        i = self.rects.index(rect)
        self.rects[i]['dead'] = True
    
    def alive(self, rect):        
        return not rect['dead']

    def isOnScreen(self, position):
        return True if position[1] >= 0 else False

    def isOnScreen2(self, item):        
        return True if item['rect'].y >= 0 and not item['dead'] else False

    def update(self):
        for i in range(len(self.rects)):
            # self.shots[i] = (self.shots[i][0], self.shots[i][1]-self.step)
            self.rects[i]['rect'].x, self.rects[i]['rect'].y = (self.rects[i]['rect'].x, self.rects[i]['rect'].y-self.step)
        
        # self.shots = list(filter(lambda x: self.isOnScreen(x), self.shots))
        self.rects = list(filter(lambda x: self.isOnScreen2(x), self.rects))