# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from circleshape import *
from player import *
def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    ship = Player((SCREEN_WIDTH/2),(SCREEN_HEIGHT/2))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill((0,0,0))
        ship.draw(screen)
        pygame.display.flip()

        #limits the framerate to 60 FPS
        delta = clock.tick(60)
        dt = (delta/1000)

    
if __name__ == "__main__":
    main()


