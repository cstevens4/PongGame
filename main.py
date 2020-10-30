import pygame

def main():

    pygame.init()
    pygame.display.set_caption("my pong")

    screen = pygame.display.set_mode((800,400))
    screen.fill((0,0,0))
    WIDTH = 800
    HEIGHT = 400
    BORDER = 15

    #Walls
    #Rectangle(surface, color, rect) -> Rect
    #Rect((left,top), (width,height)) -> Rect
    wcolor = pygame.Color("white")

    #top wall
    pygame.draw.rect(screen, wcolor, pygame.Rect((0,0),(WIDTH,BORDER)))

    #left wall
    pygame.draw.rect(screen, wcolor, pygame.Rect((0,0),(BORDER,HEIGHT)))

    #bottom wall
    pygame.draw.rect(screen, wcolor, pygame.Rect((0,HEIGHT-BORDER), (WIDTH,BORDER)))

    pygame.display.update()

    running = True

    #main loop
    while running:
        #Event handling, gets all event from the event queue
        for event in pygame.event.get():
            #Only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                #Change value to False, to exit the main loop
                running = False

if __name__ == "__main__":
    #calls main method
    main()