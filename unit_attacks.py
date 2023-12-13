"""
TITLE: UNIT ATTACK CLASS
AUTHOR : samuel tran
date: 2023-12-1
"""
from my_sprite import MySprite
from image_sprite import ImageSprite

class Attacks(MySprite):
    def __init__(self, FILENAME, DAMAGE, RANGE):
        MySprite.__init__(self)
        self._SPRITE = ImageSprite(FILENAME)
        self._DAMAGE = DAMAGE
        self._RANGE = RANGE
        self._SURFACE = self._SPRITE.getSurface()

    # -- MODIFERS METHODS --#
    # -- ACCESSOR METHODS  -- #
    def __str__(self):
        return self._NAME

    def getDamage(self):
        return self._DAMAGE

    def getRange(self):
        return self._RANGE

moveSet = {
    # fish attacks
    "flop": Attacks("media/scuba1.png", 60, 45),
    "sting": Attacks(60, 45),
    "swordSlash": Attacks(40, 45),
    "starShine": Attacks(60, 45),
    "bubbleBeam": Attacks(60, 45),

    #"chomp": Attacks("Chomp", 60, 45, 10),
    #"acidShot": Attacks("Acid Shot", 40, 45, 123),
    #"devour": Attacks("Devour", 60, 45, 10),
    # human attacks
    "picture": Attacks("Picture", 60, 45, 10),
    "water push": Attacks("Water Push", 60, 45, 10), # use there strong legs to kick the fish back
    "spear throw": Attacks("Spear Throw", 60, 45, 10),
    "net throw": Attacks("Net Throw", 60, 45, 10),
    "vile fluid": Attacks("Vile Fluid", 35, 45,23),
    #"ram": Attacks("Ram", 35, 45,23),
    #"missile": Attacks("Missile", 35, 45,23),
    #"eat": Attacks("Eat", 35, 45,23),
}