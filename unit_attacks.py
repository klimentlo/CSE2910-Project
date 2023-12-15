"""
TITLE: UNIT ATTACK CLASS
AUTHOR : samuel tran
date: 2023-12-1
"""
from my_sprite import MySprite
from image_sprite import ImageSprite
class Attacks(MySprite):
    def __init__(self, FILENAME, DAMAGE, RANGE, SPEED=5, DIRECTION=1, X =40):
        MySprite.__init__(self, 1, 1, X, 300, SPEED, (255, 255, 255), DIRECTION)
        self.__ATTACK = ImageSprite(FILENAME)
        self.__DAMAGE = DAMAGE
        self.__RANGE = RANGE
        self._SURFACE = self.__ATTACK.getSurface()

    # -- MODIFERS METHODS --#
    # -- ACCESSOR METHODS  -- #

    def getDamage(self):
        return self.__DAMAGE

    def getRange(self):
        return self.__RANGE


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