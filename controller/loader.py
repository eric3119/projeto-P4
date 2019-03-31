import pygame
import os.path

class Loader():
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