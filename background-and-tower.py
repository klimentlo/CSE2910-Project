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
    WINDOW = Window("background", 1233, 384, 30)
    BACKGROUND = ImageSprite("media/underwater-fantasy-background.png")
    BACKGROUND.setScale(3)
    E_TOWER = ImageSprite("media/enemybase1.png")
    E_TOWER.setScale(4/10)
    E_TOWER.setY(190)
    E_TOWER.setX(-10)
    A_TOWER = ImageSprite("media/allybase11.png")
    A_TOWER.setScale(9.2/10)
    A_TOWER.setY(50)
    A_TOWER.setX(1015)
    OUTLINE1 = ImageSprite("media/outline.png")
    OUTLINE1.setScale(1/6)
    OUTLINE2 = ImageSprite("media/outline.png")
    OUTLINE2.setScale(1 / 6)
    OUTLINE2.setX(86)
    CHARACTER1 = ImageSprite("media/eel/eel1idle.png")
    CHARACTER1.flipSprite()
    CHARACTER1.setY(5)
    CHARACTER1.setX(16.5)

    CHARACTER2 = ImageSprite("media/octopus/oct1idle.png")
    CHARACTER2.flipSprite()
    CHARACTER2.setY(5)
    CHARACTER2.setX(101)




    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()


        WINDOW.clearScreen()
        WINDOW.getSurface().blit(BACKGROUND.getSurface(), BACKGROUND.getPOS())
        WINDOW.getSurface().blit(E_TOWER.getSurface(), E_TOWER.getPOS())
        WINDOW.getSurface().blit(A_TOWER.getSurface(), A_TOWER.getPOS())
        WINDOW.getSurface().blit(OUTLINE1.getSurface(), OUTLINE1.getPOS())
        WINDOW.getSurface().blit(OUTLINE2.getSurface(), OUTLINE2.getPOS())
        WINDOW.getSurface().blit(CHARACTER1.getSurface(), CHARACTER1.getPOS())
        WINDOW.getSurface().blit(CHARACTER2.getSurface(), CHARACTER2.getPOS())

        WINDOW.updateFrame()