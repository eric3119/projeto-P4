import pygame
import os.path
from .loader import Loader
from .shot import Shot
from .enemy import Enemy
from .player import Player

loader=Loader()

SPRITES_PATH = 'model\\sprites'
SPRITES = dict(SPACESHIP='spaceship_pack\\Blue\\alienship_new_2_try_resize.png',
            ENEMY='enemy_2.png',
            SHOT='spaceship_pack\\Blue\\bullet_resize.png',
            BACKGROUND='background.png',
        )
SPRITES = {k: os.path.join(SPRITES_PATH, v) for k, v in SPRITES.items()}
SPRITES = {k: loader.load_img(v) for k, v in SPRITES.items()}

SCREEN_SIZE = (600, 600)

class Game():
    
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(SCREEN_SIZE)
        # logo = pygame.image.load("logo32x32.png")
        # pygame.display.set_icon(logo)        
        self.background = SPRITES['BACKGROUND'].convert()
        pygame.display.set_caption("projeto P4")        

        self.player = Player(SPRITES['SPACESHIP'], SCREEN_SIZE)
        self.shots = Shot(SPRITES['SHOT'])
        self.enemies = []
        
        self.clock = pygame.time.Clock()
    
    def run(self):

        still_down = False
        arrow_pressed = None
        
        while True:
        
            evento = pygame.event.poll()

            if evento.type == pygame.QUIT:
                return
                
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

                    else:
                        still_down = True                
                        arrow_pressed = evento.key
                elif evento.key == pygame.K_DOWN:

                    if still_down and arrow_pressed == pygame.K_UP:
                        pygame.event.post(evento)
                    else:
                        still_down = True                
                        arrow_pressed = evento.key
                
                elif evento.key == pygame.K_LEFT:
                    if still_down and arrow_pressed == pygame.K_RIGHT:
                        pygame.event.post(evento)

                    else:
                        still_down = True                
                        arrow_pressed = evento.key
                
                elif evento.key == pygame.K_RIGHT:
                    if still_down and arrow_pressed == pygame.K_LEFT:
                        pygame.event.post(evento)

                    else:
                        still_down = True                
                        arrow_pressed = evento.key
                     

            if still_down:
                self.player.update(arrow_pressed)
                    
            self.screen.blit(self.background, (0,0))
            self.screen.blit(self.player.sprite, (self.player.get_position()))
            
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
    