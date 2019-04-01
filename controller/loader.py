import pygame
import os.path

class Loader():

    def __init__(self, sprites_path):

        self.sprites_path = sprites_path

        self.animations_path = self.sprites_path+'Animation\\'
        self.buttons_path = self.sprites_path+'Buttons\\'
        self.static_path = self.sprites_path+'Static\\'
        self.numbers_path = self.static_path+'Numbers\\'

        SPRITES = dict(            
                    SHOT='bullet2.png',
                    BACKGROUND='background.png',
                )

        ANIMATIONS = dict(
            SPACESHIP='Player\\{}.png',
            ENEMY='Spacemines\\{}.png',
        )

        BUTTONS = dict(
            PLAY='play.png',
            EXIT='exit.png',
            BAR='press_start_bar.png',
        )

        NUMBERS = {k:'{}.png'.format(k) for k in range(10)}

        SPRITES = {k: os.path.join(self.static_path, v) for k, v in SPRITES.items()}
        SPRITES = {k: self.load_img(v) for k, v in SPRITES.items()}        

        ANIMATIONS = {k: os.path.join(self.animations_path, v) for k, v in ANIMATIONS.items()}
        ANIMATIONS = {k: self.load_pack(v) for k, v in ANIMATIONS.items()}

        BUTTONS = {k: os.path.join(self.buttons_path, v) for k, v in BUTTONS.items()}
        BUTTONS = {k: self.load_img(v) for k, v in BUTTONS.items()}        
        
        NUMBERS = {k: os.path.join(self.numbers_path, v) for k, v in NUMBERS.items()}
        NUMBERS = {k: self.load_img(v) for k, v in NUMBERS.items()}        

        self.sprites_dict = {
            'SPRITES': SPRITES,
            'ANIMATIONS': ANIMATIONS,
            'BUTTONS': BUTTONS,
            'NUMBERS': NUMBERS,
        }

    def get(self, item):
        return self.sprites_dict.get(item)


    def load_img(self, path):
        return pygame.image.load(path)
    
    def load_pack(self, path):
        
        sprites = []
        
        i = 1

        while True:
            try:
                img = pygame.image.load(path.format(i))
                sprites.append(img)
                i+=1

            except:
                break

        return sprites