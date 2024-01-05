import pygame
from box import Box
from text import Text
from image_sprite import ImageSprite




from window import Window


pygame.init()

class Menu:

    def __init__(self):
        self.__WINDOW = Window("Menu", 1233, 384, 30)
        self.BACKGROUND = ImageSprite("media/underwater-fantasy-background.png")
        self.BACKGROUND.setScale(3)
        self.BACKGROUND.setY(1900000)
        self.E_TOWER = ImageSprite("media/enemybase1.png")
        self.E_TOWER.setScale(4 / 10)
        self.E_TOWER.setY(190000)
        self.E_TOWER.setX(-10)
        self.A_TOWER = ImageSprite("media/allybase11.png")
        self.A_TOWER.setScale(9.2 / 10)
        self.A_TOWER.setY(500000000)
        self.A_TOWER.setX(1015)
        self.OUTLINE1 = ImageSprite("media/outline.png")
        self.OUTLINE1.setScale(1 / 6)
        self.OUTLINE1.setY(500000000)
        self.OUTLINE2 = ImageSprite("media/outline.png")
        self.OUTLINE2.setScale(1 / 6)
        self.OUTLINE2.setX(86)
        self.OUTLINE2.setY(500000000)
        self.CHARACTER1 = ImageSprite("media/eel/eel1idle.png")
        self.CHARACTER1.flipSprite()
        self.CHARACTER1.setY(50000)
        self.CHARACTER1.setX(16.5)
        self.CHARACTER2 = ImageSprite("media/octopus/oct1idle.png")
        self.CHARACTER2.flipSprite()
        self.CHARACTER2.setY(5000000)
        self.CHARACTER2.setX(101)

        self.__TITLE_TEXT = Text("Battle Fish")
        self.__TITLE_TEXT.setScale(2)
        self.__TITLE_TEXT.setPOS(self.__WINDOW.getWidth() // 2 - self.__TITLE_TEXT.getWidth() // 2, 5)

        self.__PVP = Text("PVP(p)")
        self.__PVP.setPOS(self.__WINDOW.getWidth() // 2 - self.__PVP.getWidth() // 2, 150)

        self.__PVE = Text("PVE(e)")
        self.__PVE.setPOS(self.__WINDOW.getWidth() // 2 - self.__PVE.getWidth() // 2, 250)

        self.__LEARN_TO_PLAY1 = Text("In order to win you must to destroy the human base before the humans destroy yours.")
        self.__LEARN_TO_PLAY1.setScale(4 / 5)
        self.__LEARN_TO_PLAY1.setPOS(200, 5000000)
        self.__LEARN_TO_PLAY1.setScale(4/5)
        self.__LEARN_TO_PLAY2 = Text("You can buy fish to defeat the humans")
        self.__LEARN_TO_PLAY2.setScale(3.5 / 5)
        self.__LEARN_TO_PLAY2.setPOS(365, 1000000)

        self.__CONTINUE = Text("Continue(c)")
        self.__CONTINUE.setPOS(1040, 500000000)




    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            KEY_PRESSED = pygame.key.get_pressed()

            # -- PROCESSING


            if KEY_PRESSED[pygame.K_e] == 1:
                self.__PVP.setPOS(self.__WINDOW.getWidth() // 2 - self.__PVP.getWidth() // 2, 1500000)
                self.__PVE.setPOS(self.__WINDOW.getWidth() // 2 - self.__PVP.getWidth() // 2, 1500000)
                self.__LEARN_TO_PLAY1.setPOS(200, 100)
                self.__LEARN_TO_PLAY2.setPOS(365, 150)
                self.__CONTINUE.setPOS(1040, 340)

            if KEY_PRESSED[pygame.K_c] == 1 and self.__CONTINUE.getY() == 340:
                self.__TITLE_TEXT.setPOS(self.__WINDOW.getWidth() // 2 - self.__TITLE_TEXT.getWidth() // 2, 50000)




            self.__updateWindowFrame()








    def __updateWindowFrame(self):
        self.__WINDOW.clearScreen()
        # -- Asteroid sprites
        #for asteroid in self.__ASTEROIDS:
        #    self.__WINDOW.getSurface().blit(asteroid.getSurface(), asteroid.getPOS())
        # --- LAYOUTING
        self.__WINDOW.getSurface().blit(self.__TITLE_TEXT.getSurface(), self.__TITLE_TEXT.getPOS())





        self.__WINDOW.getSurface().blit(self.BACKGROUND.getSurface(), self.BACKGROUND.getPOS())
        self.__WINDOW.getSurface().blit(self.E_TOWER.getSurface(), self.E_TOWER.getPOS())
        self.__WINDOW.getSurface().blit(self.A_TOWER.getSurface(), self.A_TOWER.getPOS())
        self.__WINDOW.getSurface().blit(self.CHARACTER1.getSurface(), self.CHARACTER1.getPOS())
        self.__WINDOW.getSurface().blit(self.CHARACTER2.getSurface(), self.CHARACTER2.getPOS())
        self.__WINDOW.getSurface().blit(self.OUTLINE1.getSurface(), self.OUTLINE1.getPOS())
        self.__WINDOW.getSurface().blit(self.OUTLINE2.getSurface(), self.OUTLINE2.getPOS())
        self.__WINDOW.getSurface().blit(self.__PVP.getSurface(), self.__PVP.getPOS())
        self.__WINDOW.getSurface().blit(self.__PVE.getSurface(), self.__PVE.getPOS())
        self.__WINDOW.getSurface().blit(self.__LEARN_TO_PLAY1.getSurface(), self.__LEARN_TO_PLAY1.getPOS())
        self.__WINDOW.getSurface().blit(self.__LEARN_TO_PLAY2.getSurface(), self.__LEARN_TO_PLAY2.getPOS())
        self.__WINDOW.getSurface().blit(self.__CONTINUE.getSurface(), self.__CONTINUE.getPOS())

        self.__WINDOW.updateFrame()


if __name__ == "__main__":
    GAME = Menu()
    GAME.run()