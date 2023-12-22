# myunits.py
from my_sprite import MySprite
from image_sprite import ImageSprite
from animation import Octattack
from window import Window
import pygame

class MyUnit(MySprite):
    def __init__(self, FILENAME, X, SPEED, MAX_HEALTH, RANGE, ATTACK, ATTACK_COOLDOWN,DIRECTION=1, IDLE_ANIMATION=None, MOVE_ANIMATION=None, ATTACK_ANIMATION=None, DEATH_ANIMATION=None, GROUP_ANIMATION=None):
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
        self.__GROUP_ANIMATION = GROUP_ANIMATION


        self._SURFACE = self.__UNIT.getSurface()


    def takeDamage(self, DAMAGE):
        self.__CURENT_HEALTH -= DAMAGE

    def getGroupAnimation(self):
        return self.__GROUP_ANIMATION

    def setAttackPOS(self, X, Y):
        self.__ATTACK_ANIMATION.setX(X)
        self.__ATTACK_ANIMATION.setY(Y)

    def setIdlePOS(self, X, Y):
        self.__IDLE_ANIMATION.setX(X)
        self.__IDLE_ANIMATION.setY(Y)

    def setDeathPOS(self, X, Y):
        self.__DEATH_ANIMATION.setX(X)
        self.__DEATH_ANIMATION.setY(Y)

    def setMovePOS(self, X, Y):
        self.__MOVE_ANIMATION.setX(X)
        self.__MOVE_ANIMATION.setY(Y)

    def setAnimationPOS(self, X, Y):
        self.__ATTACK_ANIMATION.setX(X)
        self.__ATTACK_ANIMATION.setY(Y)
        self.__IDLE_ANIMATION.setX(X)
        self.__IDLE_ANIMATION.setY(Y)
        self.__DEATH_ANIMATION.setX(X)
        self.__DEATH_ANIMATION.setY(Y)
        self.__MOVE_ANIMATION.setX(X)
        self.__MOVE_ANIMATION.setY(Y)

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
        print("Boom animation completed")

    def moveAnimation(self):
        self.__MOVE_ANIMATION.animate()
        print("Moving")

    def idleAnimation(self):
        self.__IDLE_ANIMATION.animate()


    def deathAnimation(self):
        self.__DEATH_ANIMATION.animate()



#    def canAtack(self):
#    enemyUnits = [Enemy(), Enemy(), Enemy(), Enemy(), Enemy()]
#        for ENEMIES in enemyUnits:

    def isAlive(self, LIST):
        if self.__CURENT_HEALTH < 0:
            # will eventually pop it off, which will disappear
            print("Dead")

    def updateGroupAnimation(self):
        self.__GROUP_ANIMATION.update()