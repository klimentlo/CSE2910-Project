# myunits.py
from my_sprite import MySprite
from image_sprite import ImageSprite
class MyUnits(MySprite):
    def __init__(self,FILENAME, WIDTH, HEIGHT, MAX_HEALTH, ATTACK, LEVEL=1):
        MySprite.__init__(self, WIDTH, HEIGHT)
        self.__UNIT = ImageSprite(FILENAME)
        self.__MAX_HEALTH = MAX_HEALTH
        self.__CURENT_HEALTH = MAX_HEALTH
        self.__LEVEL = LEVEL
        self.__ATTACK = ATTACK

