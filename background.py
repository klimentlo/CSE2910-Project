"""
title: Background class
Author: Samuel Tran
date: 2023-12-4
"""
import pygame
from image_sprite import ImageSprite
from my_sprite import MySprite

class Background:
    def __init__(self):
        self._SEA = ImageSprite("media/soft-underwater-landscape-with-waves-seabed-vector-22615902.jpg")


if __name__ == "__main__":
    from window import Window
    pygame.init()
    WINDOW = Window("background", 1000, 500, 30)
    BACKGROUND = ImageSprite("media/drawing-underwater-world-poster-background_2752998.jpg")
    BACKGROUND.setScale(1)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()


        WINDOW.clearScreen()
        WINDOW.getSurface().blit(BACKGROUND.getSurface(), BACKGROUND.getPOS())
        WINDOW.updateFrame()