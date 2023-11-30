# myunits.py
from my_sprite import MySprite

class MyUnits(MySprite):
    def __init__(self, WIDTH, HEIGHT, MAX_HEALTH):
        MySprite.__init__(self, WIDTH, HEIGHT)
        self.__MAX_HEALTH = MAX_HEALTH
        self.__CURENT_HEALTH = MAX_HEALTH
