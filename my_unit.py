# myunits.py
from my_sprite import MySprite
from image_sprite import ImageSprite
class MyUnits(MySprite):
    def __init__(self, FILENAME, WIDTH, HEIGHT, X, SPEED, SPAWN_COOLDOWN, MAX_HEALTH, RANGE, ATTACK, ATTACK_COOLDOWN, UNIT_TYPE, LEVEL=1):
                                            #   Y \/
        MySprite.__init__(self, WIDTH, HEIGHT, X, 300, SPEED)
        self.__UNIT = ImageSprite(FILENAME)
        # will have to add the skill point modifiers later
        self.__SPAWN_COOLDOWN = SPAWN_COOLDOWN
        self.__MAX_HEALTH = MAX_HEALTH
        self.__CURENT_HEALTH = MAX_HEALTH
        self.__RANGE = RANGE
        self.__ATTACKS = []
        self.__ATTACK_COOLDOWN = ATTACK_COOLDOWN
        self.__ALIVE = True
        self.__UNIT_TYPE = UNIT_TYPE
        self.__LEVEL = LEVEL

    def takeDamage(self, DAMAGE):
        self.__CURENT_HEALTH -= DAMAGE

    def increaseLevel(self):
        self.__LEVEL += 1

#    def canAtack(self):
#    enemyUnits = [Enemy(), Enemy(), Enemy(), Enemy(), Enemy()]
#        for ENEMIES in enemyUnits:

    def addAttack(self, ATTACK):
        self.__ATTACKS.append(ATTACK)

    def isAlive(self):
        if self.__ALIVE == False:
            # will eventually pop it off, which will disappear
            print("Dead")
