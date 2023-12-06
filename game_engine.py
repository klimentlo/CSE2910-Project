
from color import Color
from image_sprite import ImageSprite
from my_sprite import MySprite
from my_unit import MyUnit
from text import Text
from unit_attacks import Attacks
from unit_attacks import moveSet
from window import Window
import pygame
pygame.init()

class Game():
    '''
    game class
    '''
    def __init__(self):
        self.__WINDOW = Window("Fighting Fish", 960, 400, 30)
        self.__MONEY = 0
        self.__DEPlOYED_FISHES = []
        self.__DEPLOYED_HUMANS = []
        self.__LIVE_ATTACKS = []


    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()


            # SPAWNING
            KEYPRESSED = pygame.key.get_pressed()
            SPAWNEDFISH = self.__spawnFish(KEYPRESSED)
            SPAWNEDHUMAN = self.__spawnHuman(KEYPRESSED)
            if SPAWNEDFISH != None: # if a key was pressed
                self.__DEPlOYED_FISHES.append(SPAWNEDFISH) # deploy the wanted fish
            if SPAWNEDHUMAN != None:
                self.__DEPLOYED_HUMANS.append(SPAWNEDHUMAN)  # deploy the wanted fish

            # MOVEMENT
            for FISH in self.__DEPlOYED_FISHES: # For all the fish in existence
                FISH.marqueeX(self.__WINDOW.getWidth()) # make it move
                for HUMAN in self.__DEPLOYED_HUMANS:
                    if FISH.inFishRange(HUMAN.getWidth(), HUMAN.getX()):
                        print("nice")

            for HUMAN in self.__DEPLOYED_HUMANS: # For all the fish in existence
                HUMAN.marqueeX(self.__WINDOW.getWidth()) # make it move






            self.__updateWindowFrame()

    def __spawnFish(self, KEYPRESSED):
        '''
        checks if they clicked any of the following buttons
        :param KEYPRESSED:
        :return:
        '''
        # (self, FILENAME, X, SPEED, SPAWN_COOLDOWN, MAX_HEALTH, RANGE, ATTACK, ATTACK_COOLDOWN, UNIT_TYPE, LEVEL=1)
        if KEYPRESSED[pygame.K_1] == 1:
            # Salmon
            UNIT = MyUnit("media/image-removebg-preview.png", 700, 5, 8,500, 100, moveSet["flop"], 2, "Fish", -1)
            UNIT.setScale(0.3)
        if KEYPRESSED[pygame.K_2] == 1:
            # Stingray
            UNIT =  MyUnit("media/pngtree-an-orange-cat-with-squinting-eyes-png-image_2664925.jpg", 700, 5, 8,500, 100, moveSet["sting"], 2, "Fish", -1)
            UNIT.setScale(0.3)

        if KEYPRESSED[pygame.K_3] == 1:
            UNIT = MyUnit("media/pngtree-an-orange-cat-with-squinting-eyes-png-image_2664925.jpg", 700, 5, 8, 500, 100, moveSet["flop"], 2, "Fish", -1)
            UNIT.setScale(0.2)
        if KEYPRESSED[pygame.K_4] == 1:
            UNIT = MyUnit("media/image-removebg-preview.png", 700, 5, 8, 500, 100, moveSet["flop"], 2, "Fish", -1)
            UNIT.setScale(0.2)
        if KEYPRESSED[pygame.K_5] == 1:
            UNIT = MyUnit("media/image-removebg-preview.png", 700, 5, 8, 500, 100, moveSet["flop"], 2, "Fish", -1)
            UNIT.setScale(0.2)
        if KEYPRESSED[pygame.K_6] == 1:
            UNIT = MyUnit("media/image-removebg-preview.png", 700, 5, 8, 500, 100, moveSet["flop"], 2, "Fish", -1)
            UNIT.setScale(0.2)
        if KEYPRESSED[pygame.K_7] == 1:
            UNIT = MyUnit("media/image-removebg-preview.png", 700, 5, 8, 500, 100, moveSet["flop"], 2, "Fish", -1)
            UNIT.setScale(0.2)
        if KEYPRESSED[pygame.K_8] == 1:
            UNIT = MyUnit("media/image-removebg-preview.png", 700, 5, 8, 500, 100, moveSet["flop"], 2, "Fish", -1)
            UNIT.setScale(0.2)
        try:
            UNIT.setY(300 - UNIT.getHeight())
            return UNIT
        except UnboundLocalError:
            return None

    def __spawnHuman(self, KEYPRESSED):
        '''
        checks if they clicked any of the following buttons
        :param KEYPRESSED:
        :return:
        '''
        # (self, FILENAME, X, SPEED, SPAWN_COOLDOWN, MAX_HEALTH, RANGE, ATTACK, ATTACK_COOLDOWN, UNIT_TYPE, LEVEL=1)
        if KEYPRESSED[pygame.K_1] == 1:
            # Salmon
            UNIT = MyUnit("media/image-removebg-preview.png", 700, 5, 8, 500, 100, moveSet["flop"], 2, "Human")
            UNIT.setScale(0.3)
        if KEYPRESSED[pygame.K_2] == 1:
            # Stingray
            UNIT = MyUnit("media/pngtree-an-orange-cat-with-squinting-eyes-png-image_2664925.jpg", 700, 5, 8, 500, 100,
                          moveSet["sting"], 2, "Human")
            UNIT.setScale(0.3)

        if KEYPRESSED[pygame.K_3] == 1:
            UNIT = MyUnit("media/pngtree-an-orange-cat-with-squinting-eyes-png-image_2664925.jpg", 700, 5, 8, 500, 100,
                          moveSet["flop"], 2, "Human")
            UNIT.setScale(0.2)
        if KEYPRESSED[pygame.K_4] == 1:
            UNIT = MyUnit("media/image-removebg-preview.png", 700, 5, 8, 500, 100, moveSet["flop"], 2, "Human")
            UNIT.setScale(0.2)
        if KEYPRESSED[pygame.K_5] == 1:
            UNIT = MyUnit("media/image-removebg-preview.png", 700, 5, 8, 500, 100, moveSet["flop"], 2, "Human")
            UNIT.setScale(0.2)
        if KEYPRESSED[pygame.K_6] == 1:
            UNIT = MyUnit("media/image-removebg-preview.png", 700, 5, 8, 500, 100, moveSet["flop"], 2, "Human")
            UNIT.setScale(0.2)
        if KEYPRESSED[pygame.K_7] == 1:
            UNIT = MyUnit("media/image-removebg-preview.png", 700, 5, 8, 500, 100, moveSet["flop"], 2, "Human")
            UNIT.setScale(0.2)
        if KEYPRESSED[pygame.K_8] == 1:
            UNIT = MyUnit("media/image-removebg-preview.png", 700, 5, 8, 500, 100, moveSet["flop"], 2, "Human")
            UNIT.setScale(0.2)
        try:
            UNIT.setY(300 - UNIT.getHeight())
            return UNIT
        except UnboundLocalError:
            return None

    def __updateWindowFrame(self):
        self.__WINDOW.clearScreen()

        for FISH in self.__DEPlOYED_FISHES:
            self.__WINDOW.getSurface().blit(FISH.getSurface(), FISH.getPOS())

        for HUMAN in self.__DEPLOYED_HUMANS:
            self.__WINDOW.getSurface().blit(HUMAN.getSurface(), HUMAN.getPOS())

        for ATTACK in self.__LIVE_ATTACKS:
            self.__WINDOW.getSurface().blit(ATTACK.getSurface(), ATTACK.getPOS())


        self.__WINDOW.updateFrame()




if __name__ == "__main__":
    GAME = Game()
    GAME.run()
