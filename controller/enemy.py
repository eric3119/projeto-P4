class Enemy:

    def __init__(self, xpos, ypos, speed):        
        self.xpos = xpos
        self.ypos = ypos
        self.speed = speed
        self.onScreen = True

    def destroy(self):
        self.onScreen = False
    
    def isOnScreen(self):
        return self.onScreen

    def update(self, boundary = 0):
        self.xpos -= self.speed
        if self.xpos < boundary:
            self.onScreen = False