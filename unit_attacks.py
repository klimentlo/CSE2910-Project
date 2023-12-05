"""
TITLE: UNIT ATTACK CLASS
AUTHOR : samuel tran
date: 2023-12-1
"""

class Attacks:
    def __init__(self, NAME, DAMAGE, RANGE, COOLDOWN):
        """

        :param NAME: str
        :param DAMAGE: int
        """
        self._NAME = NAME
        self._DAMAGE = DAMAGE
        self._RANGE = RANGE
        self._COOLDOWN = COOLDOWN

    # -- MODIFERS METHODS --#
    # -- ACCESSOR METHODS  -- #
    def __str__(self):
        return self._NAME

    def getDamage(self):
        return self._DAMAGE

    def getRange(self):
        return self._RANGE

    def getCooldown(self):
        return self._COOLDOWN

moveSet = {
    # fish attacks
    "flop": Attacks("Flop", 60, 45, 10),
    "sting": Attacks("Sting", 60, 45, 10),
    "swordSlash": Attacks("Sword Slash", 40, 45, 2),
    "starShine": Attacks("Star Shine", 60, 45, 10),
    "bubbleBeam": Attacks("Bubble Beam", 60, 45, 10),
    "chomp": Attacks("Chomp", 60, 45, 10),
    "acidShot": Attacks("Acid Shot", 40, 45, 123),
    "devour": Attacks("Devour", 60, 45, 10),
    # human attacks
    "picture": Attacks("Picture", 60, 45, 10),
    "water push": Attacks("Water Push", 60, 45, 10), # use there strong legs to kick the fish back
    "spear throw": Attacks("Spear Throw", 60, 45, 10),
    "net throw": Attacks("Net Throw", 60, 45, 10),
    "vile fluid": Attacks("Vile Fluid", 35, 45,23),
    "ram": Attacks("Ram", 35, 45,23),
    "missile": Attacks("Missile", 35, 45,23),
    "eat": Attacks("Eat", 35, 45,23),
}