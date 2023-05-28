# coding: utf-8
import pygame
from pygame.locals import *
import sys
SCREEN = Rect(0, 0, 400, 400)

class Paddle(pygame.sprite.Sprite):
    def __init__(self, filename):
        # initialize as pygame Sprite
        pygame.sprite.Sprite.__init__(self, self.containers)

        # loading image for this Sprite
        self.image = pygame.image.load(filename).convert()
        self.rect = self.image.get_rect()
        self.rect.bottom = SCREEN.bottom - 20
    def update(self):
        self.rect.centerx = pygame.mouse.get_pos()[0]
        self.rect.clamp_ip(SCREEN) # display within screen

def main():
    # initialize for imported pygame modules
    pygame.init()

    # create Screen instance
    screen = pygame.display.set_mode(SCREEN.size)

    # create sprite group for updating
    renderUpdates = pygame.sprite.RenderUpdates()

    # create Paddle instance
    Paddle.containers = renderUpdates
    Paddle("paddle.png")

    while (1):
        screen.fill((0,10,0))   # background color
        renderUpdates.update()  # updating all sprite group
        renderUpdates.draw(screen)  # drawing all sprite group
        pygame.display.update() # updating for actual pygame display
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

if __name__ == "__main__":
    main()
