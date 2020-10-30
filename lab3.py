from ball import Ball
from paddle import Paddle
import pygame
from collections import namedtuple
import random as rand

def main():
    pygame.init()
    pygame.display.set_caption("my pong")

    screen = pygame.display.set_mode((800,400))
    screen.fill((0,0,0))
    WIDTH = 800
    HEIGHT = 400
    BORDER = 15
    VELOCITY = 2
    FPS = 120

    myconstants = namedtuple("myconstants", ["WIDTH", "HEIGHT", "BORDER", "VELOCITY", "FPS"])
    CONSTS = myconstants(WIDTH,HEIGHT,BORDER,VELOCITY,FPS)

#Walls
#Rectangle(surface, color, rect) -> Rect
#Rect((left,top), (width,height)) -> Rect
    bgcolor = pygame.Color("black")
    wcolor = pygame.Color("white")

#top wall
    pygame.draw.rect(screen, wcolor, pygame.Rect((0,0),(WIDTH,BORDER)))

#left wall
    pygame.draw.rect(screen, wcolor, pygame.Rect((0,0),(BORDER,HEIGHT)))

#bottom wall
    pygame.draw.rect(screen, wcolor, pygame.Rect((0,HEIGHT-BORDER), (WIDTH,BORDER)))

#Ball init
    x0 = WIDTH - Ball.RADIUS
    y0 = HEIGHT // 2
    vx0 = -VELOCITY
    vy0 = rand.randint(-VELOCITY,VELOCITY)

    b0 = Ball(x0,y0, vx0, vy0, screen, wcolor, bgcolor, CONSTS)
    b0.show(wcolor)

#Paddle init

    running = True
    clock = pygame.time.Clock()

#main loop
    while running:
    #Event handling, gets all event from the event queue
        for event in pygame.event.get():
        #Only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
            #Change value to False, to exit the main loop
                running = False
        pygame.display.update()
        clock.tick(FPS)

        #Ball
        b0.update()

if __name__ == "__main__":
    #calls main method
    main()