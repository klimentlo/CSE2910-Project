# myunits.py
from my_sprite import MySprite
from image_sprite import ImageSprite
from window import Window
import pygame

class MyUnits(MySprite):
    def __init__(self, FILENAME, X, SPEED, SPAWN_COOLDOWN, MAX_HEALTH, RANGE, ATTACK, ATTACK_COOLDOWN, UNIT_TYPE, LEVEL=1):
                                            #   Y \/
        MySprite.__init__(self, X, 300, SPEED)
        self.__UNIT = ImageSprite(FILENAME)
        # will have to add the skill point modifiers later
        self.__SPAWN_COOLDOWN = SPAWN_COOLDOWN
        self.__MAX_HEALTH = MAX_HEALTH
        self.__CURENT_HEALTH = MAX_HEALTH
        self.__RANGE = RANGE
        self.__ATTACKS = []
        self.__ATTACKS.append(ATTACK)
        self.__ATTACK_COOLDOWN = ATTACK_COOLDOWN
        self.__ALIVE = True
        self.__UNIT_TYPE = UNIT_TYPE
        self.__LEVEL = LEVEL
        self._SURFACE = self.__UNIT.getSurface()

    def takeDamage(self, DAMAGE):
        self.__CURENT_HEALTH -= DAMAGE


    def increaseLevel(self):
        self.__LEVEL += 1

    def inHumanRange(self, X):
        '''
        If a fish is in range of a human's attack range
        :param X: gets the X value of the CAT (tuple)
        :return: bool
        '''
        if X < self.__X + self.getWidth() + self.__RANGE:
            return True # Yes, a cat is within the range of the human

    def inCatRange(self, WIDTH, X):
        if X + WIDTH > self.getX() - self.__RANGE:
            return True


#    def canAtack(self):
#    enemyUnits = [Enemy(), Enemy(), Enemy(), Enemy(), Enemy()]
#        for ENEMIES in enemyUnits:

    def addAttack(self, ATTACK):
        self.__ATTACKS.append(ATTACK)

    def isAlive(self):
        if self.__CURENT_HEALTH < 0:
            self.__ALIVE = False
            # will eventually pop it off, which will disappear
            print("Dead")

if __name__ == "__main__":
    pygame.init()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        WINDOW = Window("Image Sprites", 800, 600, 30)
        UNIT = MyUnits("media/pngtree-an-orange-cat-with-squinting-eyes-png-image_2664925.jpg",500, 50, 50, 50, 50, 50, 50, 50 )

        WINDOW.clearScreen()

        WINDOW.updateFrame()
