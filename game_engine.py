
from image_sprite import ImageSprite
from my_unit import MyUnit
from text import Text
from unit_attacks import Attacks
from window import Window
import time, random, copy
from threading import Timer
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
        self.__FISH_SPAWN_COOLDOWN = [2.0, 3.0, 4.0, 5.0, 1.0]
        self.__FISH_CURRENT_SPAWN_COOLDOWN = [2.0, 3.0, 4.0, 5.0, 1.0]



        self.__FISH_SPAWN_LOCATION = 900
        self.__FISH_SPEED = [1, 2, 3, 4, 5]
        self.__FISH_MAX_HEALTH = [5, 5, 5, 5, 5]
        self.__FISH_RANGE = [50, 100, 150, 200, 50]
        self.__FISH_ATTACK_COOLDOWN = [1, 2, 3, 4, 5]

                                                # (self, FILENAME, X, SPEED, MAX_HEALTH, RANGE, ATTACK, ATTACK_COOLDOWN, UNIT_TYPE, LEVEL=1)
        #self.__SALMON = MyUnit("media/00.png", self.__FISH_SPAWN_LOCATION, self.__FISH_SPEED[0], self.__FISH_MAX_HEALTH[0], self.__FISH_RANGE[0], Attacks("media/humanBase.png", 60, 45, 5, -1), self.__FISH_ATTACK_COOLDOWN[0], -1)
        #self.__SALMON_COST = 50
        #self.__SALMON.setScale(0.5)
#
        #self.__STING_RAY = MyUnit("media/00.png", self.__FISH_SPAWN_LOCATION, self.__FISH_SPEED[1], self.__FISH_MAX_HEALTH[1], self.__FISH_RANGE[1], Attacks("media/humanBase.png", 60, 45, 5, -1), self.__FISH_ATTACK_COOLDOWN[1], -1)
        #self.__STING_RAY_COST = 100
        #self.__STING_RAY.setScale(0.5)
#
        #self.__SWORD_FISH = MyUnit("media/00.png", self.__FISH_SPAWN_LOCATION, self.__FISH_SPEED[2], self.__FISH_MAX_HEALTH[2], self.__FISH_RANGE[2], Attacks("media/humanBase.png", 60, 45, 5, -1), self.__FISH_ATTACK_COOLDOWN[2], -1)
        #self.__SWORD_FISH_COST = 150
        #self.__SWORD_FISH.setScale(0.5)
#
        #self.__STAR_FISH = MyUnit("media/00.png", self.__FISH_SPAWN_LOCATION, self.__FISH_SPEED[3], self.__FISH_MAX_HEALTH[3], self.__FISH_RANGE[3], Attacks("media/humanBase.png", 60, 45, 5, -1), self.__FISH_ATTACK_COOLDOWN[3], -1)
        #self.__STAR_FISH_COST = 250
        #self.__STAR_FISH.setScale(0.1)

        #self.__oct_moving_sprites = pygame.sprite.Group()
        #self.__OCTATTACK = Octattack(100, 300)
        #self.__oct_moving_sprites.add(self.__OCTATTACK)
        #self.__OCTMOVE = Octmove(100, 250)
        #self.__oct_moving_sprites.add(self.__OCTMOVE)
        #self.__OCTIDLE = Octidle(100, 200)
        #self.__oct_moving_sprites.add(self.__OCTIDLE)
        #self.__OCTDEATH = Octdeath(100, 150)
        #self.__oct_moving_sprites.add(self.__OCTDEATH)
#
        #self.__OCTOPUS = MyUnit("media/octopus/oct6attack.png", self.__FISH_SPAWN_LOCATION, self.__FISH_SPEED[4], self.__FISH_MAX_HEALTH[4], self.__FISH_RANGE[4], Attacks("media/humanBase.png", 60, 45, 5, -1), self.__FISH_ATTACK_COOLDOWN[4], -1, copy.copy(self.__OCTIDLE), copy.copy(self.__OCTMOVE), copy.copy(self.__OCTATTACK), copy.copy(self.__OCTDEATH), copy.copy(self.__oct_moving_sprites))
        #self.__OCTOPUS_COST = 400
        #self.__OCTOPUS.setScale(2)
        self.__OCTOPUS_COST = 400

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
        self.__SPEAR_FISHERMAN = MyUnit("media/00.png", self.__HUMAN_SPAWN_LOCATION, self.__HUMAN_SPEED[0],self.__HUMAN_MAX_HEALTH[0], self.__HUMAN_RANGE[0],Attacks("media/humanBase.png", 60, 45, 5, 1), self.__HUMAN_ATTACK_COOLDOWN[0], 1, 1.0, 1.0, 1.0, 1.0,1.0,1.0)
        self.__SPEAR_FISHERMAN_COST = 0
        self.__SPEAR_FISHERMAN.setScale(0.5)

        self.__SUBMARINE = MyUnit("media/00.png", self.__HUMAN_SPAWN_LOCATION, self.__HUMAN_SPEED[1],self.__HUMAN_MAX_HEALTH[1], self.__HUMAN_RANGE[1],Attacks("media/humanBase.png", 60, 45, 5, 1), self.__HUMAN_ATTACK_COOLDOWN[1], 1, 1.0, 1.0, 1.0, 1.0,1.0,1.0)
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
                if FISH.getSpeed() != 0: # if they are moving
                    FISH.setMovePOS(FISH.getX(), FISH.getY(), FISH.getWidth(), FISH.getHeight()) # make move animation on screen
                    FISH.moveAnimation() # make it animate
                FISH.marqueeX(self.__WINDOW.getWidth())  # make it move horizontally
                FISH.setSpeed(FISH.getInitialSpeed()) # sets it's speed back to its originial amount
                for HUMAN in self.__DEPLOYED_HUMANS: #
                    if FISH.inFishRange(HUMAN.getWidth(), HUMAN.getX()): # when fish encounters a human
                        FISH.setSpeed(0) # make fish speed zero
                        if FISH.isAttacking() == False: # they aren't attacking
                            FISH.idleAnimation() # idle animation
                            FISH.setIdlePOS(FISH.getX(), FISH.getY(), FISH.getWidth(), FISH.getHeight()) #make it on screen




            for HUMAN in self.__DEPLOYED_HUMANS: # For all the human in existence
                HUMAN.marqueeX(self.__WINDOW.getWidth())
                HUMAN.setSpeed(HUMAN.getInitialSpeed())
                for FISH in self.__DEPlOYED_FISHES:
                    if HUMAN.inHumanRange(FISH.getX()):
                        HUMAN.setSpeed(0)


            for ATTACK in self.__LIVE_FISH_ATTACKS:
                ATTACK.marqueeX(self.__WINDOW.getWidth())

            for ATTACK in self.__LIVE_HUMAN_ATTACKS:
                ATTACK.marqueeX(self.__WINDOW.getWidth())

            self.__fishOutputAttack()
            #self.__humanOutputAttack()
            self.__humanAttackCollision()
            self.__fishAttackCollision()
            self.__updateTimers()
            self.__updateWindowFrame()



#


    def __updateTimers(self):
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
                FISH.updateAttackAnimationDuration(self.__TIME_PASSED)

            for HUMAN in self.__DEPLOYED_HUMANS:
                HUMAN.updateAttackCooldown(self.__TIME_PASSED)
                HUMAN.updateAttackAnimationDuration(self.__TIME_PASSED)








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
                if self.__INCOME >= self.__OCTOPUS_COST:
                    self.__createOctopus()
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

        for FISH in self.__DEPlOYED_FISHES:
            FISH.getGroupAnimation().draw(self.__WINDOW.getSurface())
            FISH.updateGroupAnimation()

        self.__WINDOW.updateFrame()


    def __fishOutputAttack(self):
        for FISH in self.__DEPlOYED_FISHES:
            if FISH.getSpeed() == 0: # if their movement speed is zero
                if FISH.getCurrentAttackCooldown() >= FISH.getAttackCooldown(): # if its allowed to attack again
                    FISH.attackAnimation() # activates attack animation
                    FISH.setAttackPOS(FISH.getX(), FISH.getY(), FISH.getWidth(), FISH.getHeight()) # makes attack animation come on screen
                    FISH.resetCurrentAttackAnimationDuration()  # makes attack duration = 0
                    FISH.resetAttackCooldown() # makes cooldown to 0, so it has to wait again before it can attack again
                if FISH.finishedAttacking(): # if their attack animation has finished
                    ATTACK = copy.copy(FISH.getAttack()) # create the actual attack
                    self.__LIVE_FISH_ATTACKS.append(ATTACK) #make it exist
                    self.__LIVE_FISH_ATTACKS[-1].setX(FISH.getX() - ATTACK.getWidth())# place it where the unit is positions on the X axis
                    self.__LIVE_FISH_ATTACKS[-1].setY(FISH.getY() + FISH.getWidth() // 2 - ATTACK.getWidth() // 2) # place it at proper height of the unit
                    FISH.updateAttackAnimationDuration(1000) # make the cooldown 1000, so that it wont continuously attack. So now, I acutally dont know how this works but it seems fine


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
                try:
                    if self.__LIVE_HUMAN_ATTACKS[i].isCollision(self.__DEPlOYED_FISHES[j].getWidth(), self.__DEPlOYED_FISHES[j].getHeight(), self.__DEPlOYED_FISHES[j].getPOS()):
                        self.__DEPlOYED_FISHES[j].takeDamage(self.__LIVE_HUMAN_ATTACKS[i].getDamage())
                        self.__LIVE_HUMAN_ATTACKS.pop(i)
                        if self.__DEPlOYED_FISHES[j].getHealth() <= 0:
                            self.__DEPlOYED_FISHES.pop(j)
                except IndexError:
                    print("Errored")
                    pass


    def __fishAttackCollision(self):
        for i in range(len(self.__LIVE_FISH_ATTACKS)-1,-1,-1):
            for j in range(len(self.__DEPLOYED_HUMANS)-1,-1,-1): # for all the fish deployed
                try:
                    if self.__LIVE_FISH_ATTACKS[i].isCollision(self.__DEPLOYED_HUMANS[j].getWidth(), self.__DEPLOYED_HUMANS[j].getHeight(), self.__DEPLOYED_HUMANS[j].getPOS()):
                        self.__DEPLOYED_HUMANS[j].takeDamage(self.__LIVE_FISH_ATTACKS[i].getDamage())
                        self.__LIVE_FISH_ATTACKS.pop(i)
                        if self.__DEPLOYED_HUMANS[j].getHealth() <= 0:
                            self.__DEPLOYED_HUMANS.pop(j)
                except IndexError:
                    print("Errored")
                    pass


    def __createOctopus(self):
        # OCTOPUS COST
        # ANIMATION CREATION
        self.__oct_moving_sprites = pygame.sprite.Group()
        self.__OCTATTACK = Octattack(100, 300)
        self.__oct_moving_sprites.add(self.__OCTATTACK)
        self.__OCTMOVE = Octmove(100, 250)
        self.__oct_moving_sprites.add(self.__OCTMOVE)
        self.__OCTIDLE = Octidle(100, 200)
        self.__oct_moving_sprites.add(self.__OCTIDLE)
        self.__OCTDEATH = Octdeath(100, 150)
        self.__oct_moving_sprites.add(self.__OCTDEATH)
        # CREATES OCTOPUS BASE UNIT
        self.__OCTOPUS = MyUnit("media/octopus/oct6attack.png", self.__FISH_SPAWN_LOCATION, self.__FISH_SPEED[4],self.__FISH_MAX_HEALTH[4], self.__FISH_RANGE[4],Attacks("media/humanBase.png", 60, 45, 5, -1), self.__FISH_ATTACK_COOLDOWN[4], -1,self.__OCTIDLE, self.__OCTMOVE, self.__OCTATTACK,self.__OCTDEATH, self.__oct_moving_sprites, 0.8)
        self.__OCTOPUS.setScale(2)
        # RESETS COOLDOWN, SUBRACTS MONEY, AND ADDS IT TO DEPLOYED UNITS
        self.__FISH_CURRENT_SPAWN_COOLDOWN[4] = 0
        self.__INCOME -= self.__OCTOPUS_COST
        self.__DEPlOYED_FISHES.append(self.__OCTOPUS)
        self.__OCTOPUS.setY(300 - self.__OCTOPUS.getHeight())





if __name__ == "__main__":
    GAME = Game()
    GAME.run()
