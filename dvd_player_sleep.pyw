# ================================ #
# DVD Player Screensaver in Python #
#         By Raphaël Denni         #
# ================================ #

from glob import glob
from random import choice, randint
from time import sleep

import pygame


def image_variation(actual_img: pygame.Surface = None) -> pygame.Surface:
    """Return a random image from the DVD logo collection

    Returns:
        pygame.Surface: A random image from the DVD logo collection
    """
    images = glob("images/dvd*.png")

    image = actual_img

    while image == actual_img:
        ran = randint(0, len(images) - 1)
        image = pygame.image.load(images[ran])

    return image


def rainbow_variation(actual_img: pygame.Surface = None) -> pygame.Surface:
    for i in range(randint(0, 255)):
        image_variation(actual_img)

        pygame.display.update()


def main() -> None:
    pygame.init()

    # Set up the screen
    surface = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    surface.fill((0, 0, 0))

    screenWidth, screenHeight = pygame.display.get_surface().get_size()

    # Set up the DVD logo
    actual_img = image_variation()

    imgWidth, imgHeight = actual_img.get_size()

    # Set up the initial position and direction of the DVD logo
    X, Y = choice([0, screenWidth - imgWidth]), choice([0, screenHeight - imgHeight])
    backShiftX, backShiftY = False if X == 0 else True, False if Y == 0 else True

    pxShift = 2.5
    fps = 1 / 60

    while not pygame.key.get_pressed()[pygame.K_ESCAPE]:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        surface.blit(actual_img, (X, Y))
        pygame.display.update()

        if X <= screenWidth - imgWidth:
            X += pxShift if not backShiftX else -pxShift

        if X == 0 or X == screenWidth - imgWidth:
            backShiftX = True if not backShiftX else False
            actual_img = image_variation(actual_img)

        if Y <= screenHeight - imgHeight:
            Y += pxShift if not backShiftY else -pxShift

        if Y == 0 or Y == screenHeight - imgHeight:
            backShiftY = True if not backShiftY else False
            actual_img = image_variation(actual_img)

        sleep(fps)


if __name__ == "__main__":
    main()
