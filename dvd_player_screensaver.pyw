# ================================ #
# DVD Player Screensaver in Python #
#         By Raphaël Denni         #
# ================================ #

from glob import glob
from random import choice, randint
from time import sleep

import pygame


def image_variation(current_image: pygame.Surface = None) -> pygame.Surface:
    """Return a random image from the DVD logo collection

    Returns:
        pygame.Surface: A random image from the DVD logo collection
    """
    images = glob("images/dvd*.png")

    next_image = current_image

    while next_image == current_image:
        i = randint(0, len(images) - 1)
        next_image = pygame.image.load(images[i])

    return next_image


def rainbow_variation(actual_img: pygame.Surface = None) -> pygame.Surface:
    for i in range(randint(0, 255)):
        image_variation(actual_img)

        pygame.display.update()


def main() -> None:
    pygame.init()

    # Set up the screen
    screen_surface = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    screen_surface.fill((0, 0, 0))
    screen_width, screen_height = pygame.display.get_surface().get_size()

    # Set up the DVD logo
    current_image = image_variation()
    img_width, img_height = current_image.get_size()

    # Set up area for the DVD logo
    length_zone = screen_width - img_width
    height_zone = screen_height - img_height

    # Set up the initial position and direction of the DVD logo
    x_coor, y_coor = (
        choice([0, length_zone]),
        choice([0, height_zone]),
    )

    backShiftX, backShiftY = bool(x_coor), bool(y_coor)

    pixel_move = 2.5
    frame_rate = 1 / 60

    while not pygame.key.get_pressed()[pygame.K_ESCAPE]:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        screen_surface.blit(current_image, (x_coor, y_coor))
        pygame.display.update()

        if x_coor <= length_zone:
            x_coor += pixel_move if not backShiftX else -pixel_move

        if y_coor <= height_zone:
            y_coor += pixel_move if not backShiftY else -pixel_move

        if x_coor == 0 or x_coor == length_zone:
            backShiftX = not backShiftX
            current_image = image_variation(current_image)

        if y_coor == 0 or y_coor == height_zone:
            backShiftY = not backShiftY
            current_image = image_variation(current_image)

        sleep(frame_rate)


if __name__ == "__main__":
    main()
