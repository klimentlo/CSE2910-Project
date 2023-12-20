# myunits.py
from my_sprite import MySprite
from image_sprite import ImageSprite
from animation import Octattack
from window import Window
import pygame

class MyUnit(MySprite):
    def __init__(self, FILENAME, X, SPEED, MAX_HEALTH, RANGE, ATTACK, ATTACK_COOLDOWN,DIRECTION=1, IDLE_ANIMATION=None, MOVE_ANIMATION=None, ATTACK_ANIMATION=None, DEATH_ANIMATION=None):
                                            #   Y \/
        MySprite.__init__(self, 1, 1, X, 300, SPEED, (255, 255, 255), DIRECTION)
        self.__UNIT = ImageSprite(FILENAME)
        # will have to add the skill point modifiers later
        self.__MAX_HEALTH = MAX_HEALTH
        self.__CURENT_HEALTH = MAX_HEALTH
        self.__RANGE = RANGE
        self.__ATTACK = ATTACK
        self.__ATTACK_COOLDOWN = float(ATTACK_COOLDOWN)
        self.__CURRENT_ATTACK_COOLDOWN = float(ATTACK_COOLDOWN)
        self.__ATTACK_ANIMATION = ATTACK_ANIMATION
        self.__IDLE_ANIMATION = IDLE_ANIMATION
        self.__MOVE_ANIMATION = MOVE_ANIMATION
        self.__DEATH_ANIMATION = DEATH_ANIMATION
        self._SURFACE = self.__UNIT.getSurface()

    def takeDamage(self, DAMAGE):
        self.__CURENT_HEALTH -= DAMAGE

    def getHealth(self):
        return self.__CURENT_HEALTH

    def getAttackCooldown(self):
        return self.__ATTACK_COOLDOWN

    def getCurrentAttackCooldown(self):
        return self.__CURRENT_ATTACK_COOLDOWN

    def getAttack(self):
        return self.__ATTACK

    def updateAttackCooldown(self, TIMEPASSED):
        self.__CURRENT_ATTACK_COOLDOWN += TIMEPASSED

    def resetAttackCooldown(self):
        self.__CURRENT_ATTACK_COOLDOWN = 0

    def inHumanRange(self, X):
        '''
        If a fish is in range of a human's attack range
        :param X: gets the X value of the CAT (tuple)
        :return: bool
        '''
        if X < self.getX() + self.getWidth() + self.__RANGE and X > self.getX():
            self.setSpeed(0)
            return True # Yes, a cat is within the range of the human

    def inFishRange(self, WIDTH, X):
        if X + WIDTH > self.getX() - self.__RANGE and X < self.getX():
            return True

    def attackAnimation(self):
        self.__ATTACK_ANIMATION.animate()

    def moveAnimation(self):
        self.__MOVE_ANIMATION.animate()

    def idleAnimation(self):
        self.__ATTACK_ANIMATION.animate()

    def deathAnimation(self):
        self.__DEATH_ANIMATION.animate()



#    def canAtack(self):
#    enemyUnits = [Enemy(), Enemy(), Enemy(), Enemy(), Enemy()]
#        for ENEMIES in enemyUnits:

    def isAlive(self, LIST):
        if self.__CURENT_HEALTH < 0:
            # will eventually pop it off, which will disappear
            print("Dead")


if __name__ == "__main__":
    pygame.init()
    WINDOW = Window("Image Sprites", 800, 600, 30)                                                         # \/RANGE
    UNIT2 = MyUnits("media/pngtree-an-orange-cat-with-squinting-eyes-png-image_2664925.jpg", 600, 5, 50, 50, 100, 50, 50,
                    50)
    UNIT2.setScale(0.2)
                                                                                                        #  \/ RANGE
    UNIT = MyUnits("media/pngtree-an-orange-cat-with-squinting-eyes-png-image_2664925.jpg", 100, 5, 0, 50, 100, 50 , 50,50)
    UNIT.setScale(0.2)




    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()


        WINDOW.clearScreen()

        if UNIT.inHumanRange(UNIT2.getX()):
            print("CAT IN RANGE!")
        else:
            UNIT.setSpeed(1)
        UNIT.marqueeX(WINDOW.getWidth())

        if UNIT2.inCatRange(UNIT.getWidth(), UNIT.getX()):
            print("HUMAN IN RANGE")
        else:
            UNIT.setSpeed(1)

        KEYPRESSES = pygame.key.get_pressed()
        UNIT2.WASDmove(KEYPRESSES)
        WINDOW.getSurface().blit(UNIT.getSurface(), UNIT.getPOS())
        WINDOW.getSurface().blit(UNIT2.getSurface(), UNIT2.getPOS())
        WINDOW.updateFrame()
