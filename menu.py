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

        self.__PLAY = Text("PLAY(p)")
        self.__PLAY.setPOS(self.__WINDOW.getWidth() // 2 - self.__PLAY.getWidth() // 2, 150000)

        self.__SKILL_LEVEL = Text("Skill Level(s)")
        self.__SKILL_LEVEL.setPOS(self.__WINDOW.getWidth() // 2 - self.__SKILL_LEVEL.getWidth() // 2, 250000)

        self.__BATTLE1 = Text("Battle1(t)")
        self.__BATTLE1.setPOS(150000, self.__WINDOW.getHeight() // 2 - self.__BATTLE1.getHeight() // 2)

        self.__BATTLE2 = Text("Battle2(y)")
        self.__BATTLE2.setPOS(400000, self.__WINDOW.getHeight() // 2 - self.__BATTLE2.getHeight() // 2)

        self.__BATTLE3 = Text("Battle3(u)")
        self.__BATTLE3.setPOS(650000, self.__WINDOW.getHeight() // 2 - self.__BATTLE3.getHeight() // 2)

        self.__BATTLE4 = Text("Battle4(i)")
        self.__BATTLE4.setPOS(90000, self.__WINDOW.getHeight() // 2 - self.__BATTLE4.getHeight() // 2)

        self.VICTORY = ImageSprite("media/victory.png")
        self.VICTORY.setX(self.__WINDOW.getWidth() // 2 - self.VICTORY.getWidth() // 2)
        self.VICTORY.setY(20000000)



        self.DEFEAT = ImageSprite("media/defeat.png")
        self.DEFEAT.setX(self.__WINDOW.getWidth() // 2 - self.DEFEAT.getWidth() // 2)
        self.DEFEAT.setY(200000)





    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            KEY_PRESSED = pygame.key.get_pressed()

            # -- PROCESSING

            # PVE #
            if KEY_PRESSED[pygame.K_e] == 1 and self.__PVE.getY() == 250:
                self.__PVP.setPOS(self.__WINDOW.getWidth() // 2 - self.__PVP.getWidth() // 2, 1500000)
                self.__PVE.setPOS(self.__WINDOW.getWidth() // 2 - self.__PVP.getWidth() // 2, 1500000)
                self.__LEARN_TO_PLAY1.setPOS(200, 100)
                self.__LEARN_TO_PLAY2.setPOS(400, 150)
                self.__CONTINUE.setPOS(1040, 340)
            # how to play
            if KEY_PRESSED[pygame.K_c] == 1 and self.__LEARN_TO_PLAY2.getY() == 150:
                self.__LEARN_TO_PLAY1.setPOS(200, 1000000)
                self.__LEARN_TO_PLAY2.setPOS(400, 1500000)
                self.__PLAY.setPOS(self.__WINDOW.getWidth() // 2 - self.__PLAY.getWidth() // 2, 150)
                self.__SKILL_LEVEL.setPOS(self.__WINDOW.getWidth() // 2 - self.__SKILL_LEVEL.getWidth() // 2, 250)
                self.__CONTINUE.setPOS(1040, 34000000)
            # choosing which battle to play
            if KEY_PRESSED[pygame.K_p] == 1 and self.__PLAY.getY() == 150:
                #self.__TITLE_TEXT.setPOS(self.__WINDOW.getWidth() // 2 - self.__TITLE_TEXT.getWidth() // 2, 50000)
                self.__BATTLE1.setPOS(150, self.__WINDOW.getHeight() // 2 - self.__BATTLE1.getHeight() // 2)
                self.__BATTLE2.setPOS(400, self.__WINDOW.getHeight() // 2 - self.__BATTLE2.getHeight() // 2)
                self.__BATTLE3.setPOS(650, self.__WINDOW.getHeight() // 2 - self.__BATTLE3.getHeight() // 2)
                self.__BATTLE4.setPOS(900, self.__WINDOW.getHeight() // 2 - self.__BATTLE4.getHeight() // 2)
                self.__PLAY.setPOS(self.__WINDOW.getWidth() // 2 - self.__PLAY.getWidth() // 2, 15000)
                self.__SKILL_LEVEL.setPOS(self.__WINDOW.getWidth() // 2 - self.__SKILL_LEVEL.getWidth() // 2, 25000)
            # battle one -------
            if KEY_PRESSED[pygame.K_t] == 1 and self.__BATTLE1.getX() == 150:
                self.BACKGROUND.setY(1)
                self.E_TOWER.setY(190)
                self.A_TOWER.setY(50)
                self.OUTLINE1.setY(1)
                self.OUTLINE2.setY(1)
                self.CHARACTER1.setY(1)
                self.CHARACTER2.setY(1)
                self.__TITLE_TEXT.setPOS(self.__WINDOW.getWidth() // 2 - self.__TITLE_TEXT.getWidth() // 2, 50000)
                self.__BATTLE1.setPOS(1500000, self.__WINDOW.getHeight() // 2 - self.__BATTLE1.getHeight() // 2)
                self.__BATTLE2.setPOS(4000000, self.__WINDOW.getHeight() // 2 - self.__BATTLE2.getHeight() // 2)
                self.__BATTLE3.setPOS(6500000, self.__WINDOW.getHeight() // 2 - self.__BATTLE3.getHeight() // 2)
                self.__BATTLE4.setPOS(9000000, self.__WINDOW.getHeight() // 2 - self.__BATTLE4.getHeight() // 2)
            # battle two ------
            if KEY_PRESSED[pygame.K_y] == 1 and self.__BATTLE2.getX() == 400:
                self.BACKGROUND.setY(1)
                self.E_TOWER.setY(190)
                self.A_TOWER.setY(50)
                self.OUTLINE1.setY(1)
                self.OUTLINE2.setY(1)
                self.CHARACTER1.setY(1)
                self.CHARACTER2.setY(1)
                self.__TITLE_TEXT.setPOS(self.__WINDOW.getWidth() // 2 - self.__TITLE_TEXT.getWidth() // 2, 50000)
                self.__BATTLE1.setPOS(1500000, self.__WINDOW.getHeight() // 2 - self.__BATTLE1.getHeight() // 2)
                self.__BATTLE2.setPOS(4000000, self.__WINDOW.getHeight() // 2 - self.__BATTLE2.getHeight() // 2)
                self.__BATTLE3.setPOS(6500000, self.__WINDOW.getHeight() // 2 - self.__BATTLE3.getHeight() // 2)
                self.__BATTLE4.setPOS(9000000, self.__WINDOW.getHeight() // 2 - self.__BATTLE4.getHeight() // 2)

            # battle three ------
            if KEY_PRESSED[pygame.K_u] == 1 and self.__BATTLE3.getX() == 650:
                self.BACKGROUND.setY(1)
                self.E_TOWER.setY(190)
                self.A_TOWER.setY(50)
                self.OUTLINE1.setY(1)
                self.OUTLINE2.setY(1)
                self.CHARACTER1.setY(1)
                self.CHARACTER2.setY(1)
                self.__TITLE_TEXT.setPOS(self.__WINDOW.getWidth() // 2 - self.__TITLE_TEXT.getWidth() // 2, 50000)
                self.__BATTLE1.setPOS(1500000, self.__WINDOW.getHeight() // 2 - self.__BATTLE1.getHeight() // 2)
                self.__BATTLE2.setPOS(4000000, self.__WINDOW.getHeight() // 2 - self.__BATTLE2.getHeight() // 2)
                self.__BATTLE3.setPOS(6500000, self.__WINDOW.getHeight() // 2 - self.__BATTLE3.getHeight() // 2)
                self.__BATTLE4.setPOS(9000000, self.__WINDOW.getHeight() // 2 - self.__BATTLE4.getHeight() // 2)

            # battle four ------
            if KEY_PRESSED[pygame.K_i] == 1 and self.__BATTLE4.getX() == 900:
                self.BACKGROUND.setY(1)
                self.E_TOWER.setY(190)
                self.A_TOWER.setY(50)
                self.OUTLINE1.setY(1)
                self.OUTLINE2.setY(1)
                self.CHARACTER1.setY(1)
                self.CHARACTER2.setY(1)
                self.__TITLE_TEXT.setPOS(self.__WINDOW.getWidth() // 2 - self.__TITLE_TEXT.getWidth() // 2, 50000)
                self.__BATTLE1.setPOS(1500000, self.__WINDOW.getHeight() // 2 - self.__BATTLE1.getHeight() // 2)
                self.__BATTLE2.setPOS(4000000, self.__WINDOW.getHeight() // 2 - self.__BATTLE2.getHeight() // 2)
                self.__BATTLE3.setPOS(6500000, self.__WINDOW.getHeight() // 2 - self.__BATTLE3.getHeight() // 2)
                self.__BATTLE4.setPOS(9000000, self.__WINDOW.getHeight() // 2 - self.__BATTLE4.getHeight() // 2)

            # Win # change the if statement !!!!!!!!!!!!!
            if KEY_PRESSED[pygame.K_n] == 1 and self.E_TOWER.getY() == 190:
                self.BACKGROUND.setY(100000)
                self.E_TOWER.setY(1900000000)
                self.A_TOWER.setY(50000000)
                self.OUTLINE1.setY(100000)
                self.OUTLINE2.setY(10000)
                self.CHARACTER1.setY(1000000)
                self.CHARACTER2.setY(1000000)
                self.VICTORY.setY(1)
                self.__CONTINUE.setPOS(1040, 340)
                # say they unlock a character and level after ????????????????????????????????????????????


            # lose # change the if statement !!!!!!!!!!!
            if KEY_PRESSED[pygame.K_m] == 1 and self.E_TOWER.getY() == 190:
                self.BACKGROUND.setY(100000)
                self.E_TOWER.setY(1900000000)
                self.A_TOWER.setY(50000000)
                self.OUTLINE1.setY(100000)
                self.OUTLINE2.setY(10000)
                self.CHARACTER1.setY(1000000)
                self.CHARACTER2.setY(1000000)
                self.DEFEAT.setY(1)
                self.__CONTINUE.setPOS(1040, 340)

            # return to main menu
            if KEY_PRESSED[pygame.K_c] == 1 and self.VICTORY.getY() == 1 or KEY_PRESSED[pygame.K_c] == 1 and self.DEFEAT.getY() == 1:
                self.__TITLE_TEXT.setPOS(self.__WINDOW.getWidth() // 2 - self.__TITLE_TEXT.getWidth() // 2, 5)
                self.__PVP.setPOS(self.__WINDOW.getWidth() // 2 - self.__PVP.getWidth() // 2, 150)
                self.__PVE.setPOS(self.__WINDOW.getWidth() // 2 - self.__PVE.getWidth() // 2, 250)
                self.DEFEAT.setY(1000000)
                self.VICTORY.setY(100000)
                self.__CONTINUE.setPOS(1040, 34000000)









            self.__updateWindowFrame()








    def __updateWindowFrame(self):
        self.__WINDOW.clearScreen()

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
        self.__WINDOW.getSurface().blit(self.__PLAY.getSurface(), self.__PLAY.getPOS())
        self.__WINDOW.getSurface().blit(self.__SKILL_LEVEL.getSurface(), self.__SKILL_LEVEL.getPOS())
        self.__WINDOW.getSurface().blit(self.__BATTLE1.getSurface(), self.__BATTLE1.getPOS())
        self.__WINDOW.getSurface().blit(self.__BATTLE2.getSurface(), self.__BATTLE2.getPOS())
        self.__WINDOW.getSurface().blit(self.__BATTLE3.getSurface(), self.__BATTLE3.getPOS())
        self.__WINDOW.getSurface().blit(self.__BATTLE4.getSurface(), self.__BATTLE4.getPOS())
        self.__WINDOW.getSurface().blit(self.VICTORY.getSurface(), self.VICTORY.getPOS())
        self.__WINDOW.getSurface().blit(self.DEFEAT.getSurface(), self.DEFEAT.getPOS())

        self.__WINDOW.updateFrame()


if __name__ == "__main__":
    GAME = Menu()
    GAME.run()