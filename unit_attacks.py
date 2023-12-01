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
    "chomp": Attacks("Chomp", 60, 45, 10),
    "sword slash": Attacks("Sword Slash", 40, 45, 2),
    "ember": Attacks("Ember", 40, 45, 123),
    "leg kick": Attacks("Leg Kick", 35, 45,23)
}