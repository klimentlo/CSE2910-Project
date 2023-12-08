
from color import Color
from image_sprite import ImageSprite
from my_sprite import MySprite
from my_unit import MyUnit
from text import Text
from unit_attacks import Attacks
from unit_attacks import moveSet
from window import Window
import time, random
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
        self.__TIME = time.time()
        self.__SECOND_PASSED = self.__TIME
        self.__FISH_COOLDOWN = [2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0]
        self.__FISH_CURRENT_COOLDOWN = [2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0]


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
                if len(self.__DEPlOYED_FISHES) == 0:
                    self.__DEPlOYED_FISHES.append(SPAWNEDFISH)
                else:
                    self.__DEPlOYED_FISHES.insert(random.randrange(0, len(self.__DEPlOYED_FISHES)), SPAWNEDFISH) # deploy the wanted fish

            if SPAWNEDHUMAN != None:
                if len(self.__DEPLOYED_HUMANS) == 0:
                    self.__DEPLOYED_HUMANS.append((SPAWNEDHUMAN))
                else:
                    self.__DEPLOYED_HUMANS.insert(random.randrange(0, len(self.__DEPLOYED_HUMANS)), SPAWNEDHUMAN)  # deploy the wanted fish

            # MOVEMENT
            for FISH in self.__DEPlOYED_FISHES: # For all the fish in existence

                for HUMAN in self.__DEPLOYED_HUMANS:
                    if FISH.inFishRange(HUMAN.getWidth(), HUMAN.getX()):
                        FISH.setSpeed(0)
                        print("nice")
                FISH.marqueeX(self.__WINDOW.getWidth())  # make it move


            for HUMAN in self.__DEPLOYED_HUMANS: # For all the fish in existence
                for FISH in self.__DEPlOYED_FISHES:
                    if HUMAN.inHumanRange(FISH.getX()):
                        HUMAN.setSpeed(0)
                HUMAN.marqueeX(self.__WINDOW.getWidth())  # make it move





            self.__updateWindowFrame()

    def __milisecondPassed(self):
        self.__TIME = time.time()
        if self.__TIME >= self.__SECOND_PASSED + 0.1:
            self.__SECOND_PASSED = self.__TIME
            return True

    def __spawnFish(self, KEYPRESSED):
        '''
        checks if they clicked any of the following buttons
        :param KEYPRESSED:
        :return:
        '''
        SPAWN = 900
        if self.__milisecondPassed():
            print("hi")
            for i in range(len(self.__FISH_CURRENT_COOLDOWN)):
                self.__FISH_CURRENT_COOLDOWN[i] += 0.1 # updates the cooldown timers, adding one

        # (self, FILENAME, X, SPEED, SPAWN_COOLDOWN, MAX_HEALTH, RANGE, ATTACK, ATTACK_COOLDOWN, UNIT_TYPE, LEVEL=1)
        if self.__FISH_CURRENT_COOLDOWN[0] >= self.__FISH_COOLDOWN[0]:
            if KEYPRESSED[pygame.K_1] == 1:
                # Salmon
                UNIT = MyUnit("media/image-removebg-preview.png", SPAWN, 5,500, 100, moveSet["flop"], 2, "Fish", -1)
                UNIT.setScale(0.3)
                self.__FISH_CURRENT_COOLDOWN[0] = 0

        if self.__FISH_CURRENT_COOLDOWN[1] >= self.__FISH_COOLDOWN[1]:
            if KEYPRESSED[pygame.K_2] == 1:
                # Stingray
                UNIT =  MyUnit("media/catpaws.jpg", SPAWN, 5,500, 100, moveSet["sting"], 2, "Fish", -1)
                UNIT.setScale(0.3)
                self.__FISH_CURRENT_COOLDOWN[1] = 0

        if self.__FISH_CURRENT_COOLDOWN[2] >= self.__FISH_COOLDOWN[2]:
            if KEYPRESSED[pygame.K_3] == 1:
                UNIT = MyUnit("media/pngtree-an-orange-cat-with-squinting-eyes-png-image_2664925.jpg", SPAWN, 5, 500, 100, moveSet["flop"], 2, "Fish", -1)
                UNIT.setScale(0.2)
                self.__FISH_CURRENT_COOLDOWN[2] = 0

        if self.__FISH_CURRENT_COOLDOWN[3] >= self.__FISH_COOLDOWN[3]:
            if KEYPRESSED[pygame.K_4] == 1:
                UNIT = MyUnit("media/image-removebg-preview.png", SPAWN, 5, 500, 100, moveSet["flop"], 2, "Fish", -1)
                UNIT.setScale(0.2)
                self.__FISH_CURRENT_COOLDOWN[3] = 0

        if self.__FISH_CURRENT_COOLDOWN[4] >= self.__FISH_COOLDOWN[4]:
            if KEYPRESSED[pygame.K_5] == 1:
                UNIT = MyUnit("media/image-removebg-preview.png", SPAWN, 5, 500, 100, moveSet["flop"], 2, "Fish", -1)
                UNIT.setScale(0.2)
                self.__FISH_CURRENT_COOLDOWN[4] = 0

        if self.__FISH_CURRENT_COOLDOWN[5] >= self.__FISH_COOLDOWN[6]:
            if KEYPRESSED[pygame.K_6] == 1:
                UNIT = MyUnit("media/image-removebg-preview.png", SPAWN, 5, 500, 100, moveSet["flop"], 2, "Fish", -1)
                UNIT.setScale(0.2)
                self.__FISH_CURRENT_COOLDOWN[5] = 0

        if self.__FISH_CURRENT_COOLDOWN[6] >= self.__FISH_COOLDOWN[6]:
            if KEYPRESSED[pygame.K_7] == 1:
                UNIT = MyUnit("media/image-removebg-preview.png", SPAWN, 5, 500, 100, moveSet["flop"], 2, "Fish", -1)
                UNIT.setScale(0.2)
                self.__FISH_CURRENT_COOLDOWN[6] = 0

        if self.__FISH_CURRENT_COOLDOWN[7] >= self.__FISH_COOLDOWN[7]:
            if KEYPRESSED[pygame.K_8] == 1:
                UNIT = MyUnit("media/image-removebg-preview.png", SPAWN, 5, 500, 100, moveSet["flop"], 2, "Fish", -1)
                UNIT.setScale(0.2)
                self.__FISH_CURRENT_COOLDOWN[7] = 0
        try:
            UNIT.setY(300 - UNIT.getHeight())
            UNIT.setX(SPAWN - UNIT.getWidth() // 2)
            return UNIT
        except UnboundLocalError:
            return None

    def __spawnHuman(self, KEYPRESSED):
        '''
        checks if they clicked any of the following buttons
        :param KEYPRESSED:
        :return:
        '''

        SPAWN = 60
        # (self, FILENAME, X, SPEED, SPAWN_COOLDOWN, MAX_HEALTH, RANGE, ATTACK, ATTACK_COOLDOWN, UNIT_TYPE, LEVEL=1)

        if KEYPRESSED[pygame.K_q] == 1:
            # Salmon
            UNIT = MyUnit("media/image-removebg-preview.png", SPAWN, 5, 500, 100, moveSet["flop"], 2, "Human")
            UNIT.setScale(0.3)
        if KEYPRESSED[pygame.K_w] == 1:
            # Stingray
            UNIT = MyUnit("media/pngtree-an-orange-cat-with-squinting-eyes-png-image_2664925.jpg", SPAWN, 5, 500, 100,
                          moveSet["sting"], 2, "Human")
            UNIT.setScale(0.3)

        if KEYPRESSED[pygame.K_e] == 1:
            UNIT = MyUnit("media/pngtree-an-orange-cat-with-squinting-eyes-png-image_2664925.jpg", SPAWN, 5, 500, 100,
                          moveSet["flop"], 2, "Human")
            UNIT.setScale(0.2)
        if KEYPRESSED[pygame.K_r] == 1:
            UNIT = MyUnit("media/scuba1.png", SPAWN, 5, 500, 100, moveSet["flop"], 2, "Human")
            UNIT.setScale(0.2)
        if KEYPRESSED[pygame.K_t] == 1:
            UNIT = MyUnit("media/scuba2.png", SPAWN, 5, 500, 100, moveSet["flop"], 2, "Human")
            UNIT.setScale(0.2)
        if KEYPRESSED[pygame.K_y] == 1:
            UNIT = MyUnit("media/scuba 3.png", SPAWN, 5, 500, 100, moveSet["flop"], 2, "Human")
            UNIT.setScale(0.2)
        if KEYPRESSED[pygame.K_u] == 1:
            UNIT = MyUnit("media/humanBase.png", SPAWN, 5, 500, 100, moveSet["flop"], 2, "Human")
            UNIT.setScale(0.2)
        if KEYPRESSED[pygame.K_i] == 1:
            UNIT = MyUnit("media/image-removebg-preview.png", SPAWN, 5, 500, 100, moveSet["flop"], 2, "Human")
            UNIT.setScale(0.2)
        try:
            UNIT.setY(300 - UNIT.getHeight())
            return UNIT
        except UnboundLocalError:
            return None

    def fishAttack(self):
        print("Fish attacking!")

    def humanAttack(self):
        print("Human attacking")


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
