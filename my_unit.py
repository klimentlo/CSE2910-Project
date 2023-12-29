# myunits.py
from my_sprite import MySprite
from image_sprite import ImageSprite
from animation import Octattack
from window import Window
import pygame

class MyUnit(MySprite):
    def __init__(self, FILENAME, X, SPEED, MAX_HEALTH, RANGE, ATTACK, ATTACK_COOLDOWN,DIRECTION=1, IDLE_ANIMATION=None, MOVE_ANIMATION=None, ATTACK_ANIMATION=None, DEATH_ANIMATION=None, GROUP_ANIMATION=None, ATTACK_ANIMATION_DURATION = None):
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
        self.__ATTACKING = False
        self.__ATTACK_ANIMATION_DURATION = float(ATTACK_ANIMATION_DURATION)
        self.__CURRENT_ATTACK_ANIMATION_DURATION = float(ATTACK_ANIMATION_DURATION)

        self.__IDLE_ANIMATION = IDLE_ANIMATION
        self.__MOVE_ANIMATION = MOVE_ANIMATION
        self.__DEATH_ANIMATION = DEATH_ANIMATION
        self.__DEATH_ANIMATION_DURATION = 0.6
        self.__CURRENT_DEATH_ANIMATION_DURATION = 1000.0
        self.__GROUP_ANIMATION = GROUP_ANIMATION

        self.__DEAD = False
        self._SURFACE = self.__UNIT.getSurface()

    def getHealth(self):
        return self.__CURENT_HEALTH

    def takeDamage(self, DAMAGE):
        self.__CURENT_HEALTH -= DAMAGE

    def isDead(self):
        self.__DEAD = True

    def ifDead(self):
        if self.__DEAD == True:
            return True
        else:
            return False




    # Setting position of the animations
    def setAttackPOS(self, X, Y, WIDTH, HEIGHT):
        self.__ATTACK_ANIMATION.setX(X+WIDTH//2-(self.__ATTACK_ANIMATION.getWidth()//2))
        self.__ATTACK_ANIMATION.setY(Y+HEIGHT//2-(self.__ATTACK_ANIMATION.getHeight()//2))

        self.__MOVE_ANIMATION.setX(2000)
        self.__DEATH_ANIMATION.setX(2000)
        self.__IDLE_ANIMATION.setX(2000)

    def setIdlePOS(self, X, Y, WIDTH, HEIGHT):
        self.__IDLE_ANIMATION.setX(X+WIDTH//2-(self.__IDLE_ANIMATION.getWidth()//2))
        self.__IDLE_ANIMATION.setY(Y+HEIGHT//2-(self.__IDLE_ANIMATION.getHeight()//2))
        # Move everything else
        self.__MOVE_ANIMATION.setX(2000)
        self.__DEATH_ANIMATION.setX(2000)
        self.__ATTACK_ANIMATION.setX(2000)


    def setDeathPOS(self, X, Y, WIDTH, HEIGHT):
        self.__DEATH_ANIMATION.setX(X + WIDTH // 2 - (self.__IDLE_ANIMATION.getWidth() // 2))
        self.__DEATH_ANIMATION.setY(Y + HEIGHT // 2 - (self.__IDLE_ANIMATION.getHeight() // 2))
        # Move everything else
        self.__MOVE_ANIMATION.setX(2000)
        self.__IDLE_ANIMATION.setX(2000)
        self.__ATTACK_ANIMATION.setX(2000)

    def setMovePOS(self, X, Y, WIDTH, HEIGHT):
        # PLACES MOVE ANIMATION WHERE IT SHOULD BE
        self.__MOVE_ANIMATION.setX(X+WIDTH//2-(self.__MOVE_ANIMATION.getWidth()//2))
        self.__MOVE_ANIMATION.setY(Y+HEIGHT//2-(self.__MOVE_ANIMATION.getHeight()//2))
        # MOVES EVERYTHING ELSE AWAY
        self.__ATTACK_ANIMATION.setX(2000)
        self.__IDLE_ANIMATION.setX(2000)
        self.__DEATH_ANIMATION.setX(2000)

    def setAnimationPOS(self, X, Y): # setts all of them together (probably uneeded)
        self.__ATTACK_ANIMATION.setX(X)
        self.__ATTACK_ANIMATION.setY(Y)
        self.__IDLE_ANIMATION.setX(X)
        self.__IDLE_ANIMATION.setY(Y)
        self.__DEATH_ANIMATION.setX(X)
        self.__DEATH_ANIMATION.setY(Y)
        self.__MOVE_ANIMATION.setX(X)
        self.__MOVE_ANIMATION.setY(Y)

    # Making The animation move move
    def attackAnimation(self):
        self.__ATTACK_ANIMATION.animate()
        self.__ATTACKING = True

    def moveAnimation(self):
        self.__MOVE_ANIMATION.animate()

    def idleAnimation(self):
        self.__IDLE_ANIMATION.animate()


    def deathAnimation(self):
        self.__DEATH_ANIMATION.animate()

    def getGroupAnimation(self):# Is used to update the animations on the game_engine
        return self.__GROUP_ANIMATION

    def updateGroupAnimation(self):
        self.__GROUP_ANIMATION.update()



    # --- ATTACK RELATED FUNCTIONS --- #

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

    # ATTACK ANIMATION AND ITS TIMINGS
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

    def finishedAttacking(self):
        if self.__CURRENT_ATTACK_ANIMATION_DURATION >= self.__ATTACK_ANIMATION_DURATION and self.__CURRENT_ATTACK_ANIMATION_DURATION <= 999:
            self.__ATTACKING = False
            return True

    # DEATH ANIMATION AND ITS TIMINGS

    def beginDeathAnimationDuration(self):
        self.__CURRENT_DEATH_ANIMATION_DURATION = 0

    def finishedDying(self):
        if self.__CURRENT_DEATH_ANIMATION_DURATION >= self.__DEATH_ANIMATION_DURATION and self.__CURRENT_DEATH_ANIMATION_DURATION <= 999:
            return True

    def getDeathTimers(self):
        print("Current Death Animation Duration: ", self.__CURRENT_DEATH_ANIMATION_DURATION)
        print("Actual Death duration: ", self.__DEATH_ANIMATION_DURATION)

    def updateDeathAnimationDuration(self, TIMEPASSED):
        self.__CURRENT_DEATH_ANIMATION_DURATION += TIMEPASSED



#    def canAtack(self):
#    enemyUnits = [Enemy(), Enemy(), Enemy(), Enemy(), Enemy()]
#        for ENEMIES in enemyUnits:



