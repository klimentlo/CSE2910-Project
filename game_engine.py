
from color import Color
from image_sprite import ImageSprite
from my_sprite import MySprite
from my_unit import MyUnit
from text import Text
from unit_attacks import Attacks
from unit_attacks import moveSet
from window import Window
import time, random, copy
import pygame
pygame.init()

class Game():
    '''
    game class
    '''
    def __init__(self):
        self.__WINDOW = Window("Fighting Fish", 960, 400, 30)
        self.__BACKGROUND = ImageSprite("media/b228ea58-42fe-43eb-9f60-07622a4072f9.png")
        self.__BACKGROUND.setY(-500)
        self.__INCOME = 0
        self.__INCOME_TEXT = Text(f"${self.__INCOME}")
        self.__INCOME_TEXT.setPOS(self.__WINDOW.getWidth() - self.__INCOME_TEXT.getWidth() - 25, 25)

        self.__DEPlOYED_FISHES = []
        self.__DEPLOYED_HUMANS = []
        self.__LIVE_ATTACKS = []
        self.__TIME = time.time()
        self.__PREVIOUS_TIME = self.__TIME
        self.__TIME_PASSED = 1

        # Fish Spawning Cooldown
        self.__FISH_COOLDOWN = [2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0]
        self.__FISH_CURRENT_COOLDOWN = [2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0]
        # (self, FILENAME, X, SPEED, MAX_HEALTH, RANGE, ATTACK, ATTACK_COOLDOWN, UNIT_TYPE, LEVEL=1)
        # Fish attacking cooldown
        self.__FISH_ATTACK_COOLDOWN = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]


        self.__X_SPAWN_LOCATION = 900

        self.__FISH_SPEED = [1, 2, 3, 4, 5]
        self.__FISH_MAX_HEALTH = [50, 100, 150, 200, 250]
        self.__FISH_RANGE = [50, 100, 150, 200, 250]

        self.__SALMON = MyUnit("media/image-removebg-preview.png", self.__X_SPAWN_LOCATION, self.__FISH_SPEED[0], self.__FISH_MAX_HEALTH[0], self.__FISH_RANGE[0], moveSet["flop"], 2, "Fish", -1)
        self.__SALMON_COST = 50
        self.__SALMON.setScale(0.5)

        self.__STING_RAY = MyUnit("media/scuba1.png", self.__X_SPAWN_LOCATION, self.__FISH_SPEED[1], self.__FISH_MAX_HEALTH[1], self.__FISH_RANGE[1], moveSet["sting"], 2, "Fish", -1)
        self.__STING_RAY_COST = 100
        self.__STING_RAY.setScale(0.5)

        self.__SWORD_FISH = MyUnit("media/submarine2.png", self.__X_SPAWN_LOCATION, self.__FISH_SPEED[2], self.__FISH_MAX_HEALTH[2], self.__FISH_RANGE[2], moveSet["sting"], 2, "Fish", -1)
        self.__SWORD_FISH_COST = 150
        self.__SWORD_FISH.setScale(0.5)

        self.__STAR_FISH = MyUnit("media/catpaws.jpg", self.__X_SPAWN_LOCATION, self.__FISH_SPEED[3], self.__FISH_MAX_HEALTH[3], self.__FISH_RANGE[3], moveSet["sting"], 2, "Fish", -1)
        self.__STAR_FISH_COST = 250
        self.__STAR_FISH.setScale(0.1)

        self.__SEA_HORSE = MyUnit("media/humanBase.png", self.__X_SPAWN_LOCATION, self.__FISH_SPEED[4], self.__FISH_MAX_HEALTH[4], self.__FISH_RANGE[4],moveSet["sting"], 2, "Fish", -1)
        self.__SEA_HORSE_COST = 400
        self.__SEA_HORSE.setScale(0.25)






    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
            self.__INCOME += 1
            self.__INCOME_TEXT.setText(f"$ {self.__INCOME}")
            self.__INCOME_TEXT.setPOS(self.__WINDOW.getWidth() - self.__INCOME_TEXT.getWidth() - 25, 25)
            # - - - SPAWNING
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
                    self.__DEPLOYED_HUMANS.append(SPAWNEDHUMAN)
                else:
                    self.__DEPLOYED_HUMANS.insert(random.randrange(0, len(self.__DEPLOYED_HUMANS)), SPAWNEDHUMAN)  # deploy the wanted fish

            # - - - MOVEMENT - - - #
            for FISH in self.__DEPlOYED_FISHES: # For all the fish in existence
                for HUMAN in self.__DEPLOYED_HUMANS:
                    if FISH.inFishRange(HUMAN.getWidth(), HUMAN.getX()):
                        FISH.setSpeed(0)
                        print("nice")
                    else:
                        FISH.setSpeed(FISH.getSpeed())
                FISH.marqueeX(self.__WINDOW.getWidth())  # make it move


            for HUMAN in self.__DEPLOYED_HUMANS: # For all the fish in existence
                for FISH in self.__DEPlOYED_FISHES:
                    if HUMAN.inHumanRange(FISH.getX()):
                        HUMAN.setSpeed(0)
                KEYSPRESSED = pygame.key.get_pressed()
                HUMAN.WASDmove(KEYSPRESSED)

            for FISH in self.__DEPlOYED_FISHES:
                if FISH.getSpeed() == 0:
                    FISH.attack()

            self.__updateWindowFrame()

    def __timePassed(self, TIME_PASSED):
        self.__TIME = time.time()
        if self.__TIME >= self.__PREVIOUS_TIME + TIME_PASSED:
            self.__PREVIOUS_TIME = self.__TIME # updates previous time to what self.__TIME is right now, and returns the fact that a milisend
            return True

    def __spawnFish(self, KEYPRESSED):
        '''
        checks if they clicked any of the following buttons
        :param KEYPRESSED:
        :return:
        '''
        SPAWN = 900

        # COOLDOWN CODE
        if self.__timePassed(self.__TIME_PASSED): # if the wanted time interval has passed
            for i in range(len(self.__FISH_CURRENT_COOLDOWN)): # for every unique fish
                self.__FISH_CURRENT_COOLDOWN[i] += self.__TIME_PASSED # updates the cooldown timers by the time passed

        # If Salmon cooldown is above the current cooldown, allow it to be spawned
        if self.__FISH_CURRENT_COOLDOWN[0] >= self.__FISH_COOLDOWN[0]:
            if KEYPRESSED[pygame.K_1] == 1:
                if self.__INCOME >= self.__SALMON_COST:
                    UNIT = copy.copy(self.__SALMON)
                    self.__FISH_CURRENT_COOLDOWN[0] = 0
                    self.__INCOME -= self.__SALMON_COST


        if self.__FISH_CURRENT_COOLDOWN[1] >= self.__FISH_COOLDOWN[1]:
            if KEYPRESSED[pygame.K_2] == 1:
                # Stingray
                if self.__INCOME >= self.__STING_RAY_COST:
                    UNIT = copy.copy(self.__STING_RAY)
                    self.__FISH_CURRENT_COOLDOWN[1] = 0
                    self.__INCOME -= self.__STING_RAY_COST

        if self.__FISH_CURRENT_COOLDOWN[2] >= self.__FISH_COOLDOWN[2]:
            if KEYPRESSED[pygame.K_3] == 1:
                if self.__INCOME >= self.__SWORD_FISH_COST:
                    UNIT = copy.copy(self.__SWORD_FISH)
                    self.__FISH_CURRENT_COOLDOWN[2] = 0
                    self.__INCOME -= self.__SWORD_FISH_COST

        if self.__FISH_CURRENT_COOLDOWN[3] >= self.__FISH_COOLDOWN[3]:

            if KEYPRESSED[pygame.K_4] == 1:
                if self.__INCOME >= self.__STAR_FISH_COST:
                    UNIT = copy.copy(self.__STAR_FISH)
                    self.__FISH_CURRENT_COOLDOWN[3] = 0
                    self.__INCOME -= self.__STAR_FISH_COST

        if self.__FISH_CURRENT_COOLDOWN[4] >= self.__FISH_COOLDOWN[4]:
            if KEYPRESSED[pygame.K_5] == 1:
                if self.__INCOME >= self.__SEA_HORSE_COST:
                    UNIT = copy.copy(self.__SEA_HORSE)
                    self.__FISH_CURRENT_COOLDOWN[4] = 0
                    self.__INCOME -= self.__SEA_HORSE_COST
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
        # (self, FILENAME, X, SPEED, SPAWN_COOLDOWN, MAX_HEALTH, RANGE, ATTACK, ATTACK_COOLDOWN, UNIT_TYPE, LEVEL=1)
        SPAWN = 60

        if KEYPRESSED[pygame.K_q] == 1:
            # Salmon
            UNIT = MyUnit("media/image-removebg-preview.png", SPAWN, 5, 500, 100, moveSet["flop"], 2, "Human")
        if KEYPRESSED[pygame.K_w] == 1:
            # Stingray
            UNIT = MyUnit("media/pngtree-an-orange-cat-with-squinting-eyes-png-image_2664925.jpg", SPAWN, 5, 500, 100,
                          moveSet["sting"], 2, "Human")

        if KEYPRESSED[pygame.K_e] == 1:
            UNIT = MyUnit("media/pngtree-an-orange-cat-with-squinting-eyes-png-image_2664925.jpg", SPAWN, 5, 500, 100,
                          moveSet["flop"], 2, "Human")
        if KEYPRESSED[pygame.K_r] == 1:
            UNIT = MyUnit("media/scuba1.png", SPAWN, 5, 500, 100, moveSet["flop"], 2, "Human")
        if KEYPRESSED[pygame.K_t] == 1:
            UNIT = MyUnit("media/scuba2.png", SPAWN, 5, 500, 100, moveSet["flop"], 2, "Human")
        if KEYPRESSED[pygame.K_y] == 1:
            UNIT = MyUnit("media/scuba 3.png", SPAWN, 5, 500, 100, moveSet["flop"], 2, "Human")
        if KEYPRESSED[pygame.K_u] == 1:
            UNIT = MyUnit("media/humanBase.png", SPAWN, 5, 500, 100, moveSet["flop"], 2, "Human")
        if KEYPRESSED[pygame.K_i] == 1:
            UNIT = MyUnit("media/image-removebg-preview.png", SPAWN, 5, 500, 100, moveSet["flop"], 2, "Human")
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
        self.__WINDOW.getSurface().blit(self.__BACKGROUND.getSurface(), self.__BACKGROUND.getPOS())
        self.__WINDOW.getSurface().blit(self.__INCOME_TEXT.getSurface(), self.__INCOME_TEXT.getPOS())

        for FISH in self.__DEPlOYED_FISHES:
            self.__WINDOW.getSurface().blit(FISH.getSurface(), FISH.getPOS())

        for HUMAN in self.__DEPLOYED_HUMANS:
            self.__WINDOW.getSurface().blit(HUMAN.getSurface(), HUMAN.getPOS())

        for ATTACK in self.__LIVE_ATTACKS:
            self.__WINDOW.getSurface().blit(ATTACK.getSurface(), ATTACK.getPOS())

        self.__WINDOW.updateFrame()

    def attack(self):



if __name__ == "__main__":
    GAME = Game()
    GAME.run()
