import pygame
import os.path
from .loader import Loader
from .shot import Shot
from .enemy import Enemy
from .player import Player

SCREEN_SIZE = (800, 600)

x = 10
y = 100
from os import environ
environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (x,y)

loader=Loader()

SPRITES_PATH = 'model\\sprites'
ANIMATIONS_PATH = 'model\\sprites\\spaceship_pack\\Blue\\Animation'
BUTTONS_PATH = 'model\\sprites\\spaceship_pack\\Buttons'

SPRITES = dict(
            ENEMY='enemy_2.png',
            SHOT='spaceship_pack\\Blue\\bullet_resize.png',
            BACKGROUND='background.png',
        )

ANIMATIONS = dict(
    SPACESHIP='{}.png',
)

BUTTONS = dict(
    PLAY='play.png',
    EXIT='exit.png',
)

SPRITES = {k: os.path.join(SPRITES_PATH, v) for k, v in SPRITES.items()}
SPRITES = {k: loader.load_img(v) for k, v in SPRITES.items()}

ANIMATIONS = {k: os.path.join(ANIMATIONS_PATH, v) for k, v in ANIMATIONS.items()}
ANIMATIONS = {k: loader.load_pack(v) for k, v in ANIMATIONS.items()}

BUTTONS = {k: os.path.join(BUTTONS_PATH, v) for k, v in BUTTONS.items()}
BUTTONS = {k: loader.load_img(v) for k, v in BUTTONS.items()}


class Game():
    
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(SCREEN_SIZE)
        # logo = pygame.image.load("logo32x32.png")
        # pygame.display.set_icon(logo)        
        self.background = SPRITES['BACKGROUND'].convert()
        pygame.display.set_caption("projeto P4")        
        
        self.player = Player(ANIMATIONS['SPACESHIP'], SCREEN_SIZE)
        self.shots = Shot(SPRITES['SHOT'])
        self.enemies = []
        
        self.clock = pygame.time.Clock()
    
    def run(self):

        still_down = False
        arrow_pressed = None
        
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
                    x, y = self.player.get_position()
                    x += self.player.get_sprite_size()[0]//2 - self.shots.get_sprite_size()[0]//2
                    y -= self.shots.get_sprite_size()[1]
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

            
            self.player.update(arrow_pressed)
                    
            self.screen.blit(self.background, (0,0))
            self.screen.blit(self.player.get_sprite(), (self.player.get_position()))
            
            for position in self.shots.shots:
                self.screen.blit(self.shots.sprite, position)
            self.shots.update()
            
            # if (pygame.time.get_ticks() - enemy_control) >= enemy_time:            
            #     enemy_control = pygame.time.get_ticks()
            #     enemies.append(enemy.Enemy(xpos = screen_width, ypos= random.random()*(screen_height-enemy_img.get_height()), speed=(random.random()+1)*enemy_max_speed))
            
            # for target in enemies:
            #     self.screen.blit(enemy_img, (target.xpos, target.ypos))
            #     target.update()
            #     #colision enemy ship
            #     if target.xpos < xpos + ship_img.get_width() and target.xpos + ship_img.get_height() > xpos and target.ypos < ypos + ship_img.get_height() and ship_img.get_width() + target.ypos > ypos:
            #         return
            #     #colision enemy shot
            #     for projec in shots:
            #         if projec.xpos < target.xpos + enemy_img.get_width() and projec.xpos + shot_img.get_width() > target.xpos and projec.ypos < target.ypos + enemy_img.get_height() and shot_img.get_width() + projec.ypos > target.ypos:
            #             target.destroy()
            #             projec.destroy()
            #             score+=1

            # f = display_score.render("Destruidos: "+str(score), True, [0, 0, 0], [116,166,129])

            # self.screen.blit(f, ((screen_width//2)-(display_score.size("Destruidos: "+str(score))[0]//2),0))
            pygame.display.flip()

            self.clock.tick(30)
        #end loop
    ## end run()
    def event_handler(self):
        pass
    
    def main_menu(self):
        
        mouseX, mouseY = (None,None)
        padding = 10
        btn_play_pos = (SCREEN_SIZE[0]//2 - BUTTONS['PLAY'].get_width()//2, SCREEN_SIZE[1]//2)
        btn_exit_pos = (SCREEN_SIZE[0]//2 - BUTTONS['EXIT'].get_width()//2, SCREEN_SIZE[1]//2 + BUTTONS['PLAY'].get_height()+padding)
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
                
                if event.type == pygame.MOUSEBUTTONDOWN:
                    LEFT, MIDDLE, RIGHT = pygame.mouse.get_pressed()
                    if LEFT == 1:
                        mouseX, mouseY = pygame.mouse.get_pos()
                        if btn_play_pos[0] <= mouseX <= btn_play_pos[0]+BUTTONS['PLAY'].get_width():
                            if btn_play_pos[1] <= mouseY <= btn_play_pos[1]+BUTTONS['PLAY'].get_height():
                                start_game = True
                        
                        if btn_exit_pos[0] <= mouseX <= btn_exit_pos[0]+BUTTONS['EXIT'].get_width():
                            if btn_exit_pos[1] <= mouseY <= btn_exit_pos[1]+BUTTONS['EXIT'].get_height():
                                pygame.quit()
                                quit()
                    

            self.screen.blit(self.background, (0,0))
            self.screen.blit(BUTTONS['PLAY'], btn_play_pos)
            self.screen.blit(BUTTONS['EXIT'], btn_exit_pos)
            
            pygame.display.flip()
        
            if start_game:
                start_game = False
                self.run()
        
    