import pygame

def main():
    pygame.init()

    screen = pygame.display.set_mode(800, 400)

    screen.fill((255,0,0))
    pygame.display.update()

    running = True

    # main loop
    while running:
        # Event handling, gets all event from the event queue
        for event in pygame.event.get():
            # Only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # Change value to False, to exit the main loop
                running = False

if __name__ == "__main__":
    #calls main method
    main()