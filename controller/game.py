import pygame
import os.path

SCREEN_SIZE = (800, 600)

from .loader import Loader
from .shot import Shot
from .enemy import Enemy
from .player import Player

from os import environ

x = 10
y = 100
environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (x,y)

loader=Loader(sprites_path='model\\sprites\\spaceship_pack\\')

class Game():
    
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(SCREEN_SIZE)
        # logo = pygame.image.load("logo32x32.png")
        # pygame.display.set_icon(logo)        
        self.background = loader.get('SPRITES').get('BACKGROUND').convert()
        pygame.display.set_caption("projeto P4")        
        
        self.player = Player(loader.get('ANIMATIONS').get('SPACESHIP'))
        self.shots = Shot(loader.get('SPRITES').get('SHOT'))
        self.enemies = Enemy(loader.get('ANIMATIONS').get('ENEMY'))
        
        self.clock = pygame.time.Clock()
    
    def run(self):

        still_down = False
        arrow_pressed = None
        text = pygame.font.Font(pygame.font.get_default_font(), 30)
        while True:
        
            evento = pygame.event.poll()

            if evento.type == pygame.QUIT:
                pygame.quit()
                quit()
                
            if evento.type == pygame.KEYUP:
                if evento.key != pygame.K_SPACE:
                    still_down = False

            if evento.type == pygame.KEYDOWN:
                
                if evento.key == pygame.K_ESCAPE:
                    return

                if evento.key == pygame.K_SPACE:
                    cannon_size = 0# 62
                    x, y = self.player.get_position()
                    x += self.player.get_sprite_size()[0]//2 - self.shots.get_sprite_size()[0]//2
                    y -= self.shots.get_sprite_size()[1]-cannon_size
                    self.shots.trigger((x,y))
                    
                elif evento.key == pygame.K_UP:
                    
                    if still_down and arrow_pressed == pygame.K_DOWN:
                        pygame.event.post(evento)
                        arrow_pressed = None
                    else:
                        still_down = True                
                        arrow_pressed = evento.key
                elif evento.key == pygame.K_DOWN:

                    if still_down and arrow_pressed == pygame.K_UP:
                        pygame.event.post(evento)
                        arrow_pressed = None
                    else:
                        still_down = True                
                        arrow_pressed = evento.key
                
                elif evento.key == pygame.K_LEFT:
                    if still_down and arrow_pressed == pygame.K_RIGHT:
                        pygame.event.post(evento)
                        arrow_pressed = None
                    else:
                        still_down = True                
                        arrow_pressed = evento.key
                
                elif evento.key == pygame.K_RIGHT:
                    if still_down and arrow_pressed == pygame.K_LEFT:
                        pygame.event.post(evento)
                        arrow_pressed = None
                    else:
                        still_down = True                
                        arrow_pressed = evento.key                                     
            elif evento.type == pygame.KEYUP and evento.key in (
                pygame.K_UP,
                pygame.K_DOWN,
                pygame.K_LEFT,
                pygame.K_RIGHT,
            ):                
                arrow_pressed = None
            
            self.player.update(arrow_pressed)
                    
            self.screen.blit(self.background, (0,0))
            self.screen.blit(self.player.get_sprite(), (self.player.get_position()))
            
            for item in self.shots.rects:
                self.screen.blit(self.shots.sprite, item['rect'])
            self.shots.update()
            
            for item in self.enemies.rects:
                self.screen.blit(self.enemies.get_sprite(), (item['rect'].x, item['rect'].y))
            self.enemies.update(pygame.time.get_ticks())

            ## check collision
            
            for enemy in self.enemies.rects:
                
                if enemy['rect'].colliderect(self.player.rect):
                    if not self.player.is_shield():
                        self.enemies.destroy(enemy)
                    
                    self.player.collide()
                
                for shot in self.shots.rects:
                    
                    if shot['rect'].colliderect(enemy['rect']):                        
                        self.enemies.destroy(enemy)
                        self.shots.destroy(shot)            
            
            f = text.render("Vidas: "+str(self.player.health), True, [255, 255, 255])
            self.screen.blit(f, (
                    (SCREEN_SIZE[0])-(text.size("Vidas: "+str(self.player.health))[0]),
                    0
                )
            )
            
            f = text.render("Destruidos: "+str(self.enemies.dead_num), True, [255, 255, 255])
            self.screen.blit(f, (0,0))

            pygame.display.flip()

            self.clock.tick(30)
        #end loop
    ## end run()
    def event_handler(self):
        pass
    
    def main_menu(self):
        
        mouseX, mouseY = (None,None)
        padding = 10
        btn_play_pos = (SCREEN_SIZE[0]//2 - loader.get('BUTTONS').get('PLAY').get_width()//2, SCREEN_SIZE[1]//2)
        btn_exit_pos = (SCREEN_SIZE[0]//2 - loader.get('BUTTONS').get('EXIT').get_width()//2, SCREEN_SIZE[1]//2 + loader.get('BUTTONS').get('PLAY').get_height()+padding)
        start_game = False

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        quit()
                    if event.key == pygame.K_SPACE:
                        start_game = True
                
                if event.type == pygame.MOUSEBUTTONDOWN:
                    LEFT, MIDDLE, RIGHT = pygame.mouse.get_pressed()
                    if LEFT == 1:
                        mouseX, mouseY = pygame.mouse.get_pos()
                        if btn_play_pos[0] <= mouseX <= btn_play_pos[0]+loader.get('BUTTONS').get('PLAY').get_width():
                            if btn_play_pos[1] <= mouseY <= btn_play_pos[1]+loader.get('BUTTONS').get('PLAY').get_height():
                                start_game = True
                        
                        if btn_exit_pos[0] <= mouseX <= btn_exit_pos[0]+loader.get('BUTTONS').get('EXIT').get_width():
                            if btn_exit_pos[1] <= mouseY <= btn_exit_pos[1]+loader.get('BUTTONS').get('EXIT').get_height():
                                pygame.quit()
                                quit()
                    

            self.screen.blit(self.background, (0,0))
            self.screen.blit(loader.get('BUTTONS').get('PLAY'), btn_play_pos)
            self.screen.blit(loader.get('BUTTONS').get('EXIT'), btn_exit_pos)
            
            pygame.display.flip()
        
            if start_game:
                start_game = False
                self.run()
        
    