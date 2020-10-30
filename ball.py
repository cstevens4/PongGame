import pygame
class Ball:
    pass
    #class variable
    RADIUS = 10

    def __init__(self, x, y, vx, vy, screen, fgcolor, bgcolor, CONSTS):
       #instance variables
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.screen = screen
        self.fgcolor = fgcolor
        self.bgcolor = bgcolor
        self.CONSTS = CONSTS

    def show(self, color):
        pygame.draw.circle(self.screen, color, (self.x, self.y), self.RADIUS)

    def update(self):
        #newpos = oldpos + deltapos
        #delete old ball
        self.show(self.bgcolor)
        self.x = self.x + self.vx
        self.y = self.y + self.vy
        self.show(self.fgcolor)
        #If I'm colliding:
        #flip velocity
        if self.x < self.CONSTS.BORDER + self.RADIUS:
            self.vx = -self.vx

        if self.y < self.CONSTS.BORDER + self.RADIUS:
            self.vy = -self.vy

        if self.y > self.CONSTS.HEIGHT - self.CONSTS.BORDER - self.RADIUS:
            self.vy = -self.vy