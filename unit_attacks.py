"""
TITLE: UNIT ATTACK CLASS
AUTHOR : samuel tran
date: 2023-12-1
"""
from my_sprite import MySprite
from image_sprite import ImageSprite
from animation import Lighting
import pygame

class Attacks(MySprite):
    def __init__(self, FILENAME, DAMAGE, RANGE, SPEED=5, DIRECTION=1, X =40, PROJECTILE = False, LIGHTING = False, ANIMATION=None, ATTACK_ANIMATION_DURATION = 0.3):
        MySprite.__init__(self, 1, 1, X, 300, SPEED, (255, 255, 255), DIRECTION)
        self.__ATTACK = ImageSprite(FILENAME)
        self.__DAMAGE = DAMAGE
        self.__RANGE = RANGE
        self.__PROJECTILE = PROJECTILE
        self._SURFACE = self.__ATTACK.getSurface()
        self.__LIGHTING = LIGHTING
        self.__ANIMATION = ANIMATION
        self.__ATTACKING = False
        self.__ATTACK_ANIMATION_DURATION = ATTACK_ANIMATION_DURATION
        self.__CURRENT_ATTACK_ANIMATION_DURATION = ATTACK_ANIMATION_DURATION
        self.__LIVE = False
        self.width = 50
        self.height = 50


    # -- MODIFERS METHODS --#
    # -- ACCESSOR METHODS  -- #

    def getDamage(self):
        return self.__DAMAGE

    def getRange(self):
        return self.__RANGE

    def isProjectile(self):
        return self.__PROJECTILE

    def isLighting(self):
        if self.__LIGHTING == True:
            return True

    def getAnimation(self):
        return self.__ANIMATION

    def attackAnimation(self):
        self.__ANIMATION.animate()

    def setAnimationPOS(self, X, Y):
        self.__ANIMATION.setX(X)
        self.__ANIMATION.setY(Y)

    def update(self):
        self.__ANIMATION.update()

    # ATTACK ANIMATION DURATION
    def getAttackAnimationDuration(self):
        return self.__ATTACK_ANIMATION_DURATION

    def getCurrentAttackAnimationDuration(self):
        return self.__CURRENT_ATTACK_ANIMATION_DURATION

    def updateAttackAnimationDuration(self, TIMEPASSED):
        self.__CURRENT_ATTACK_ANIMATION_DURATION += TIMEPASSED

    def resetCurrentAttackAnimationDuration(self):
        self.__CURRENT_ATTACK_ANIMATION_DURATION = 0

    def isAttacking(self):
        return self.__ATTACKING

    def setLive(self, BOOL):
        self.__LIVE = BOOL

    def isLive(self):
        if self.__LIVE == True:
            return True

    def finishedAttacking(self):
        if self.__CURRENT_ATTACK_ANIMATION_DURATION >= self.__ATTACK_ANIMATION_DURATION and self.__CURRENT_ATTACK_ANIMATION_DURATION <= 999.0:
            self.__ATTACKING = False
            return True

    def setScale(self, WIDTH, HEIGHT):
        self.width = WIDTH
        self.height = HEIGHT
        self._SURFACE = pygame.transform.scale(self._SURFACE, (self.width, self.height))


#moveSet = {
#    # fish attacks
#    "flop": Attacks("media/humanBase.png", 60, 45),
#    "sting": Attacks("media/scuba1.png" , 60, 45),
#    "swordSlash": Attacks("media/scuba1.png", 40, 45),
#    "starShine": Attacks("media/scuba1.png",60, 45),
#    "bubbleBeam": Attacks("media/scuba1.png",60, 45),
#
#    #"chomp": Attacks("Chomp", 60, 45, 10),
#    #"acidShot": Attacks("Acid Shot", 40, 45, 123),
#    #"devour": Attacks("Devour", 60, 45, 10),
#    # human attacks
#    "picture": Attacks("Picture", 60, 45),
#    "water push": Attacks("Water Push", 60, 45), # use there strong legs to kick the fish back
#    "spear throw": Attacks("Spear Throw", 60, 45),
#    "net throw": Attacks("Net Throw", 60, 45),
#    "vile fluid": Attacks("Vile Fluid", 35, 45),
#    #"ram": Attacks("Ram", 35, 45,23),
#    #"missile": Attacks("Missile", 35, 45,23),
#    #"eat": Attacks("Eat", 35, 45,23),
#}