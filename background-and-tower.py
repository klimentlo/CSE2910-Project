"""
title: Background class
Author: Samuel Tran
date: 2023-12-4
"""
import pygame
from image_sprite import ImageSprite


if __name__ == "__main__":
    from window import Window
    pygame.init()
    WINDOW = Window("background", 960, 400, 30)
    BACKGROUND = ImageSprite("media/b228ea58-42fe-43eb-9f60-07622a4072f9.png")
    BACKGROUND.setScale(1)
    BACKGROUND.setY(-500)
    E_TOWER = ImageSprite("media/image-removebg-preview.png")
    E_TOWER.setScale(2/5)
    E_TOWER.setY(200)
    A_TOWER = ImageSprite("media/humanBase.png")
    A_TOWER.setScale(2 / 5)
    A_TOWER.setY(185)
    A_TOWER.setX(870)
    SAND1 = ImageSprite("media/sand-background-preview.png")
    SAND1.setY(250)
    SAND2 = ImageSprite("media/sand-background-preview.png")
    SAND2.setY(250)
    SAND2.setX(500)



    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()


        WINDOW.clearScreen()
        WINDOW.getSurface().blit(BACKGROUND.getSurface(), BACKGROUND.getPOS())
        WINDOW.getSurface().blit(E_TOWER.getSurface(), E_TOWER.getPOS())
        WINDOW.getSurface().blit(A_TOWER.getSurface(), A_TOWER.getPOS())
        WINDOW.getSurface().blit(SAND1.getSurface(), SAND1.getPOS())
        WINDOW.getSurface().blit(SAND2.getSurface(), SAND2.getPOS())
        WINDOW.updateFrame()