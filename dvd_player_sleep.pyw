# DVD Player Sleep Screen in Python
# By Raphaël Denni

# Import

from glob import glob
from random import randint
from time import sleep

import pygame

pygame.init()


def image_variation() -> tuple:
    images = glob("images/dvd*.png")

    ran = randint(0, len(images) - 1)
    image = pygame.image.load(images[ran])

    return image


def main() -> None:
    # Set up the screen
    surface = pygame.display.set_mode((0, 0))
    surface.fill((0, 0, 0))

    screenWidth, screenHeight = pygame.display.get_surface().get_size()

    # Set up the DVD logo
    actual_img = image_variation()

    imgWidth, imgHeight = actual_img.get_size()

    # Set up the initial position and direction of the DVD logo
    X, Y = 0, 0
    backShiftX, backShiftY = False, False
    pxShift = 2.5
    fps = 1 / 60

    while not pygame.key.get_pressed()[pygame.K_ESCAPE]:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        surface.blit(actual_img, (X, Y))
        pygame.display.update()

        if not backShiftX:
            if X < screenWidth - imgWidth:
                X += pxShift
            if X == screenWidth - imgWidth:
                backShiftX = True
                actual_img = image_variation()

        else:
            if X <= screenWidth - imgWidth:
                X -= pxShift
            if X == 0:
                backShiftX = False
                actual_img = image_variation()

        if not backShiftY:
            if Y < screenHeight - imgHeight:
                Y += pxShift
            if Y == screenHeight - imgHeight:
                backShiftY = True
                actual_img = image_variation()

        else:
            if Y <= screenHeight - imgHeight:
                Y -= pxShift
            if Y == 0:
                backShiftY = False
                actual_img = image_variation()

        sleep(fps)


if __name__ == "__main__":
    main()
