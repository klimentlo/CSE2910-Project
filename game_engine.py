
from image_sprite import ImageSprite
from my_unit import MyUnit
from text import Text
from unit_attacks import Attacks
from window import Window
import time, random, copy
import pygame
from animation import Octdeath, Octidle, Octattack, Octmove
pygame.init()



class Game():
    '''
    game class
    '''
    def __init__(self):
        self.__WINDOW = Window("Fighting Fish", 960, 400, 30)
        self.__BACKGROUND = ImageSprite("media/b228ea58-42fe-43eb-9f60-07622a4072f9.png")
        self.__BACKGROUND.setY(-500)
        self.__INCOME = 5000
        self.__INCOME_TEXT = Text(f"${self.__INCOME}")
        self.__INCOME_TEXT.setPOS(self.__WINDOW.getWidth() - self.__INCOME_TEXT.getWidth() - 25, 25)

        self.__DEPlOYED_FISHES = []
        self.__DEPLOYED_HUMANS = []
        self.__LIVE_FISH_ATTACKS = []
        self.__LIVE_HUMAN_ATTACKS = []
        self.__TIME = time.time()
        self.__PREVIOUS_TIME = self.__TIME
        self.__TIME_PASSED = 0.1

        # - - - - - - - - - - - - - - - - - - - - #
        #   -  -  - FISH CONFIGURATIONS -  -  -   #
        # - - - - - - - - - - - - - - - - - - - - #

        # Fish Spawning Cooldown
        self.__FISH_SPAWN_COOLDOWN = [2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0]
        self.__FISH_CURRENT_SPAWN_COOLDOWN = [2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0]



        self.__FISH_SPAWN_LOCATION = 900
        self.__FISH_SPEED = [1, 2, 3, 4, 5]
        self.__FISH_MAX_HEALTH = [50, 100, 150, 200, 250]
        self.__FISH_RANGE = [50, 100, 150, 200, 250]
        self.__FISH_ATTACK_COOLDOWN = [1, 2, 3, 4, 5]

                                                # (self, FILENAME, X, SPEED, MAX_HEALTH, RANGE, ATTACK, ATTACK_COOLDOWN, UNIT_TYPE, LEVEL=1)
        self.__SALMON = MyUnit("media/00.png", self.__FISH_SPAWN_LOCATION, self.__FISH_SPEED[0], self.__FISH_MAX_HEALTH[0], self.__FISH_RANGE[0], Attacks("media/humanBase.png", 60, 45, 5, -1), self.__FISH_ATTACK_COOLDOWN[0], "Fish", -1)
        self.__SALMON_COST = 50
        self.__SALMON.setScale(0.5)

        self.__STING_RAY = MyUnit("media/00.png", self.__FISH_SPAWN_LOCATION, self.__FISH_SPEED[1], self.__FISH_MAX_HEALTH[1], self.__FISH_RANGE[1], Attacks("media/humanBase.png", 60, 45, 5, -1), self.__FISH_ATTACK_COOLDOWN[1], "Fish", -1)
        self.__STING_RAY_COST = 100
        self.__STING_RAY.setScale(0.5)

        self.__SWORD_FISH = MyUnit("media/00.png", self.__FISH_SPAWN_LOCATION, self.__FISH_SPEED[2], self.__FISH_MAX_HEALTH[2], self.__FISH_RANGE[2], Attacks("media/humanBase.png", 60, 45, 5, -1), self.__FISH_ATTACK_COOLDOWN[2], "Fish", -1)
        self.__SWORD_FISH_COST = 150
        self.__SWORD_FISH.setScale(0.5)

        self.__STAR_FISH = MyUnit("media/00.png", self.__FISH_SPAWN_LOCATION, self.__FISH_SPEED[3], self.__FISH_MAX_HEALTH[3], self.__FISH_RANGE[3], Attacks("media/humanBase.png", 60, 45, 5, -1), self.__FISH_ATTACK_COOLDOWN[3], "Fish", -1)
        self.__STAR_FISH_COST = 250
        self.__STAR_FISH.setScale(0.1)

        self.__SEA_HORSE = MyUnit("media/humanBase.png", self.__FISH_SPAWN_LOCATION, self.__FISH_SPEED[4], self.__FISH_MAX_HEALTH[4], self.__FISH_RANGE[4], Attacks("media/humanBase.png", 60, 45, 5, -1), self.__FISH_ATTACK_COOLDOWN[4], "Fish", -1)
        self.__SEA_HORSE_COST = 400
        self.__SEA_HORSE.setScale(0.25)
        self.__oct_moving_sprites = pygame.sprite.Group()
        self.__OCTATTACK = Octattack(100, 300)
        self.__oct_moving_sprites.add(self.__OCTATTACK)
        self.__OCTMOVE = Octmove(100, 250)
        self.__oct_moving_sprites.add(self.__OCTMOVE)
        self.__OCTIDLE = Octidle(100, 200)
        self.__oct_moving_sprites.add(self.__OCTIDLE)
        self.__OCTDEATH = Octdeath(100, 150)
        self.__oct_moving_sprites.add(self.__OCTDEATH)


        # - - - - - - - - - - - - - - - - - - - - - #
        #    -  -  - HUMAN CONFIGURATIONS -  -  -   #
        # - - - - - - - - - - - - - - - - - - - - - #

        # Human Spawning Cooldown
        self.__HUMAN_SPAWN_COOLDOWN = [1000.0, 10.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0]
        self.__HUMAN_CURRENT_SPAWN_COOLDOWN = [1.0, 9.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0]


        self.__HUMAN_SPAWN_LOCATION = 60
        self.__HUMAN_SPEED = [1, 5, 3, 4, 5]
        self.__HUMAN_MAX_HEALTH = [50, 100, 150, 200, 250]
        self.__HUMAN_RANGE = [50, 100, 150, 200, 250]
        self.__HUMAN_ATTACK_COOLDOWN = [1, 2, 3, 4, 5]


        # (self, FILENAME, X, SPEED, MAX_HEALTH, RANGE, ATTACK, ATTACK_COOLDOWN, UNIT_TYPE, LEVEL=1)
        self.__SPEAR_FISHERMAN = MyUnit("media/00.png", self.__HUMAN_SPAWN_LOCATION, self.__HUMAN_SPEED[0],self.__HUMAN_MAX_HEALTH[0], self.__HUMAN_RANGE[0],Attacks("media/humanBase.png", 60, 45, 5, 1), self.__HUMAN_ATTACK_COOLDOWN[0], 1)
        self.__SPEAR_FISHERMAN_COST = 0
        self.__SPEAR_FISHERMAN.setScale(0.5)

        self.__SUBMARINE = MyUnit("media/00.png", self.__HUMAN_SPAWN_LOCATION, self.__HUMAN_SPEED[1],self.__HUMAN_MAX_HEALTH[1], self.__HUMAN_RANGE[1],Attacks("media/humanBase.png", 60, 45, 5, 1), self.__HUMAN_ATTACK_COOLDOWN[1], 1)
        self.__SUBMARINE_COST = 0
        self.__SUBMARINE.setScale(0.5)







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
            SPAWNEDHUMAN = self.__spawnHuman()

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
                    else:
                        FISH.setSpeed(FISH.getSpeed())
                FISH.marqueeX(self.__WINDOW.getWidth())  # make it move


            for HUMAN in self.__DEPLOYED_HUMANS: # For all the fish in existence
                HUMAN.marqueeX(self.__WINDOW.getWidth())
                HUMAN.setSpeed(HUMAN.getInitialSpeed())
                for FISH in self.__DEPlOYED_FISHES:
                    if HUMAN.inHumanRange(FISH.getX()):
                        HUMAN.setSpeed(0)


            for ATTACK in self.__LIVE_FISH_ATTACKS:
                ATTACK.marqueeX(self.__WINDOW.getWidth())

            for ATTACK in self.__LIVE_HUMAN_ATTACKS:
                ATTACK.marqueeX(self.__WINDOW.getWidth())

            #self.__fishOutputAttack()
            self.__humanOutputAttack()
            self.__humanAttackCollision()
            self.__fishAttackCollision()
            self.__updateCooldowns()
            self.__updateWindowFrame()
            print(self.__oct_moving_sprites)






    def __updateCooldowns(self):
        self.__TIME = time.time()
        if self.__TIME >= self.__PREVIOUS_TIME + self.__TIME_PASSED:
            self.__PREVIOUS_TIME = self.__TIME # saves its current time, so when another second passes, it will do this again

            # updates the cooldowns
            for i in range(len(self.__FISH_CURRENT_SPAWN_COOLDOWN)): # for every unique fish
                self.__FISH_CURRENT_SPAWN_COOLDOWN[i] += self.__TIME_PASSED # updates the cooldown timers by the time passed

            for i in range(len(self.__HUMAN_CURRENT_SPAWN_COOLDOWN)):
                self.__HUMAN_CURRENT_SPAWN_COOLDOWN[i] += self.__TIME_PASSED

            for FISH in self.__DEPlOYED_FISHES:
                FISH.updateAttackCooldown(self.__TIME_PASSED)

            for HUMAN in self.__DEPLOYED_HUMANS:
                HUMAN.updateAttackCooldown(self.__TIME_PASSED)






    def __spawnFish(self, KEYPRESSED):
        '''
        checks if they clicked any of the following buttons
        :param KEYPRESSED:
        :return:
        '''
        SPAWN = 900

        # If Salmon cooldown is above the current cooldown, allow it to be spawned
        if self.__FISH_CURRENT_SPAWN_COOLDOWN[0] >= self.__FISH_SPAWN_COOLDOWN[0]:
            if KEYPRESSED[pygame.K_1] == 1:
                if self.__INCOME >= self.__SALMON_COST:
                    UNIT = copy.copy(self.__SALMON)
                    self.__FISH_CURRENT_SPAWN_COOLDOWN[0] = 0
                    self.__INCOME -= self.__SALMON_COST


        if self.__FISH_CURRENT_SPAWN_COOLDOWN[1] >= self.__FISH_SPAWN_COOLDOWN[1]:
            if KEYPRESSED[pygame.K_2] == 1:
                # Stingray
                if self.__INCOME >= self.__STING_RAY_COST:
                    UNIT = copy.copy(self.__STING_RAY)
                    self.__FISH_CURRENT_SPAWN_COOLDOWN[1] = 0
                    self.__INCOME -= self.__STING_RAY_COST

        if self.__FISH_CURRENT_SPAWN_COOLDOWN[2] >= self.__FISH_SPAWN_COOLDOWN[2]:
            if KEYPRESSED[pygame.K_3] == 1:
                if self.__INCOME >= self.__SWORD_FISH_COST:
                    UNIT = copy.copy(self.__SWORD_FISH)
                    self.__FISH_CURRENT_SPAWN_COOLDOWN[2] = 0
                    self.__INCOME -= self.__SWORD_FISH_COST

        if self.__FISH_CURRENT_SPAWN_COOLDOWN[3] >= self.__FISH_SPAWN_COOLDOWN[3]:

            if KEYPRESSED[pygame.K_4] == 1:
                if self.__INCOME >= self.__STAR_FISH_COST:
                    UNIT = copy.copy(self.__STAR_FISH)
                    self.__FISH_CURRENT_SPAWN_COOLDOWN[3] = 0
                    self.__INCOME -= self.__STAR_FISH_COST

        if self.__FISH_CURRENT_SPAWN_COOLDOWN[4] >= self.__FISH_SPAWN_COOLDOWN[4]:
            if KEYPRESSED[pygame.K_5] == 1:
                if self.__INCOME >= self.__SEA_HORSE_COST:
                    UNIT = copy.copy(self.__SEA_HORSE)
                    self.__FISH_CURRENT_SPAWN_COOLDOWN[4] = 0
                    self.__INCOME -= self.__SEA_HORSE_COST
        try:
            UNIT.setY(300 - UNIT.getHeight())
            UNIT.setX(SPAWN - UNIT.getWidth() // 2)
            return UNIT
        except UnboundLocalError:
            return None

    def __spawnHuman(self):
        '''
        checks if they clicked any of the following buttons
        :return:
        '''

        if self.__HUMAN_CURRENT_SPAWN_COOLDOWN[0] >= self.__HUMAN_SPAWN_COOLDOWN[0]:
            UNIT = copy.copy(self.__SPEAR_FISHERMAN)
            self.__HUMAN_CURRENT_SPAWN_COOLDOWN[0] = 0

        if self.__HUMAN_CURRENT_SPAWN_COOLDOWN[1] >= self.__HUMAN_SPAWN_COOLDOWN[1]:
            UNIT = copy.copy(self.__SUBMARINE)
            self.__HUMAN_CURRENT_SPAWN_COOLDOWN[1] = 0
        try:
            UNIT.setY(300 - UNIT.getHeight())
            UNIT.setX( - UNIT.getWidth() // 2)
            return UNIT
        except UnboundLocalError:
            return None


    def __updateWindowFrame(self):
        self.__WINDOW.clearScreen()
        self.__WINDOW.getSurface().blit(self.__BACKGROUND.getSurface(), self.__BACKGROUND.getPOS())
        self.__WINDOW.getSurface().blit(self.__INCOME_TEXT.getSurface(), self.__INCOME_TEXT.getPOS())

        for FISH in self.__DEPlOYED_FISHES:
            self.__WINDOW.getSurface().blit(FISH.getSurface(), FISH.getPOS())

        for HUMAN in self.__DEPLOYED_HUMANS:
            self.__WINDOW.getSurface().blit(HUMAN.getSurface(), HUMAN.getPOS())

        for ATTACK in self.__LIVE_FISH_ATTACKS:
            self.__WINDOW.getSurface().blit(ATTACK.getSurface(), ATTACK.getPOS())

        for ATTACK in self.__LIVE_HUMAN_ATTACKS:
            self.__WINDOW.getSurface().blit(ATTACK.getSurface(), ATTACK.getPOS())
        KEYS_PRESSED = pygame.key.get_pressed()
        if KEYS_PRESSED[pygame.K_SPACE] == 1:
            self.__OCTDEATH.animate()
            self.__OCTIDLE.animate()
            self.__OCTATTACK.animate()
            self.__OCTMOVE.animate()
        self.__oct_moving_sprites.draw(self.__WINDOW.getSurface())
        self.__oct_moving_sprites.update()
        self.__WINDOW.updateFrame()


    def __fishOutputAttack(self):
        for FISH in self.__DEPlOYED_FISHES:
            if FISH.getSpeed() == 0: # if their movement speed is zero
                FISH.getAttackCooldown()
                if FISH.getCurrentAttackCooldown() >= FISH.getAttackCooldown():
                    ATTACK = copy.copy(FISH.getAttack())
                    self.__LIVE_FISH_ATTACKS.append(ATTACK)
                    self.__LIVE_FISH_ATTACKS[-1].setX(FISH.getX()-ATTACK.getWidth())
                    self.__LIVE_FISH_ATTACKS[-1].setY(FISH.getY()+FISH.getWidth()//2-ATTACK.getWidth()//2)
                    FISH.resetAttackCooldown()

    def __humanOutputAttack(self):
        for HUMAN in self.__DEPLOYED_HUMANS:
            if HUMAN.getSpeed() == 0: # if their movement speed is zero
                HUMAN.getAttackCooldown()
                if HUMAN.getCurrentAttackCooldown() >= HUMAN.getAttackCooldown():
                    ATTACK = copy.copy(HUMAN.getAttack())
                    self.__LIVE_HUMAN_ATTACKS.append(ATTACK)
                    self.__LIVE_HUMAN_ATTACKS[-1].setX(HUMAN.getX())
                    self.__LIVE_HUMAN_ATTACKS[-1].setY(HUMAN.getY()+HUMAN.getWidth()//2-ATTACK.getWidth()//2)
                    HUMAN.resetAttackCooldown()


    def __humanAttackCollision(self):
        for i in range(len(self.__LIVE_HUMAN_ATTACKS)-1,-1,-1):
            for j in range(len(self.__DEPlOYED_FISHES)-1,-1,-1): # for all the fish deployed
                if self.__LIVE_HUMAN_ATTACKS[i].isCollision(self.__DEPlOYED_FISHES[j].getWidth(), self.__DEPlOYED_FISHES[j].getHeight(), self.__DEPlOYED_FISHES[j].getPOS()):
                    self.__DEPlOYED_FISHES[j].takeDamage(self.__LIVE_HUMAN_ATTACKS[i].getDamage())
                    self.__LIVE_HUMAN_ATTACKS.pop(i)
                    if self.__DEPlOYED_FISHES[j].getHealth() <= 0:
                        self.__DEPlOYED_FISHES.pop(j)


    def __fishAttackCollision(self):
        ""
        #lol




if __name__ == "__main__":
    GAME = Game()
    GAME.run()
