# DVD Player Sleep Screen in Python
# By Raphaël Denni

# Import

from random import randint
from time import sleep

import pygame

pygame.init()

# Variables

surface = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
black = pygame.Color(0, 0, 0)
screenWidth, screenHeight = pygame.display.get_surface().get_size()

image0 = pygame.image.load("./images/dvd0.png").convert_alpha()
image1 = pygame.image.load("./images/dvd1.png").convert_alpha()
image2 = pygame.image.load("./images/dvd2.png").convert_alpha()
image3 = pygame.image.load("./images/dvd3.png").convert_alpha()
image4 = pygame.image.load("./images/dvd4.png").convert_alpha()
image5 = pygame.image.load("./images/dvd5.png").convert_alpha()
image6 = pygame.image.load("./images/dvd6.png").convert_alpha()

img = image0
imgWidth, imgHeight = img.get_width(), img.get_height()
X = 0 or screenWidth / randint(2, 4)
Y = 0 or screenHeight / randint(2, 4)

backShiftX = False
backShiftY = False

pxShift = 2.5
fps = 1 / 60

ran0 = 0

# Functions


def colorChange():
    global ran0

    global img

    ran = randint(0, 6)
    if ran == ran0:
        if ran == 6:
            ran = 0
        else:
            ran = ran + 1

    if ran == 0:
        img = image0
    if ran == 1:
        img = image1
    if ran == 2:
        img = image2
    if ran == 3:
        img = image3
    if ran == 4:
        img = image4
    if ran == 5:
        img = image5
    if ran == 6:
        img = image6

    ran0 = ran


def rainbow(t, n):
    global img

    if (
        X == 0
        and Y == 0
        or X == screenWidth - imgWidth
        and Y == 0
        or X == 0
        and Y == screenHeight - imgHeight
        or X == screenWidth - imgWidth
        and Y == screenHeight - imgHeight
    ):
        while n != 0:
            n = n - 1

            colorChange()

            surface.fill(black)
            surface.blit(img, (X, Y))
            pygame.display.update()
            sleep(t)


# Display

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)

    surface.fill(black)
    surface.blit(img, (X, Y))
    rainbow(0.05, 21)

    pygame.display.update()

    if backShiftX is False:
        if X < screenWidth - imgWidth:
            X = X + pxShift
        if X == screenWidth - imgWidth:
            backShiftX = True
            colorChange()

    else:
        if X <= screenWidth - imgWidth:
            X = X - pxShift
        if X == 0:
            backShiftX = False
            colorChange()

    if backShiftY is False:
        if Y < screenHeight - imgHeight:
            Y = Y + pxShift
        if Y == screenHeight - imgHeight:
            backShiftY = True
            colorChange()

    else:
        if Y <= screenHeight - imgHeight:
            Y = Y - pxShift
        if Y == 0:
            backShiftY = False
            colorChange()

    sleep(fps)
