
from image_sprite import ImageSprite
from my_unit import MyUnit
from text import Text
from unit_attacks import Attacks
from window import Window
import time, random, copy
from threading import Timer
import pygame

from animation import Octidle, Octmove, Octattack, Octdeath
from animation import Wandidle, Wandmove, Wandattack, Wanddeath
from animation import Swordidle, Swordmove, Swordattack, Sworddeath
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

        self.__DEPLOYED_FISHES = []
        self.__DEPLOYED_HUMANS = []
        self.__LIVE_FISH_ATTACKS = []
        self.__LIVE_HUMAN_ATTACKS = []
        self.__TIME = time.time()
        self.__PREVIOUS_TIME = self.__TIME
        self.__TIME_PASSED = 0.1

        # - - - - - - - - - - - - - - - - - - - - #
        #   -  -  - FISH CONFIGURATIONS -  -  -   #
        # - - - - - - - - - - - - - - - - - - - - #

        # --- GENERAL ATTRIBUTE CONFIGURATION --- #

        self.__FISH_SPAWN_LOCATION = 900

        self.__FISH_SPAWN_COOLDOWN = [2.0, 3.0, 4.0, 5.0, 1.0]
        self.__FISH_CURRENT_SPAWN_COOLDOWN = [2.0, 3.0, 4.0, 5.0, 1.0]
        self.__FISH_MAX_HEALTH = [200, 5, 5, 0, 2500]
        self.__FISH_RANGE = [50, 100, 150, 200, -50]
        self.__FISH_SPEED = [1, 2, 3, 4, 5]
        self.__FISH_ATTACK_COOLDOWN = [1, 2, 3, 4, 5]

        # --- COST OF THE UNITS --- #
        self.__OCTOPUS_COST = 400

        # - - - - - - - - - - - - - - - - - - - - - #
        #    -  -  - HUMAN CONFIGURATIONS -  -  -   #
        # - - - - - - - - - - - - - - - - - - - - - #

        # Human Spawning Cooldown
        self.__HUMAN_SPAWN_COOLDOWN = [10.0, 5000.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0]
        self.__HUMAN_CURRENT_SPAWN_COOLDOWN = [8.0, 9.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0]


        self.__HUMAN_SPAWN_LOCATION = 60
        self.__HUMAN_SPEED = [1, 5, 3, 4, 5]
        self.__HUMAN_MAX_HEALTH = [50, 100, 150, 200, 250]
        self.__HUMAN_RANGE = [300, 100, 150, 200, 250]
        self.__HUMAN_ATTACK_COOLDOWN = [0.9, 2, 3, 4, 5]


        # (self, FILENAME, X, SPEED, MAX_HEALTH, RANGE, ATTACK, ATTACK_COOLDOWN, UNIT_TYPE, LEVEL=1)
        self.__SPEAR_FISHERMAN = MyUnit("media/00.png", self.__HUMAN_SPAWN_LOCATION, self.__HUMAN_SPEED[0],self.__HUMAN_MAX_HEALTH[0], self.__HUMAN_RANGE[0],Attacks("media/wand/Projectile.png", 1, 45, 5, 1), self.__HUMAN_ATTACK_COOLDOWN[0], 1, 1.0, 1.0, 1.0, 1.0,1.0,1.0)
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
            # How the user makes money
            self.__INCOME += 1
            self.__INCOME_TEXT.setText(f"$ {self.__INCOME}")
            self.__INCOME_TEXT.setPOS(self.__WINDOW.getWidth() - self.__INCOME_TEXT.getWidth() - 25, 25)



            # - - - SPAWNING - - - #
            KEYPRESSED = pygame.key.get_pressed()
            SPAWNEDFISH = self.__spawnFish(KEYPRESSED)
            SPAWNEDHUMAN = self.__spawnHuman()



            if SPAWNEDFISH != None: # if a key was pressed
                if len(self.__DEPLOYED_FISHES) == 0:
                    self.__DEPLOYED_FISHES.append(SPAWNEDFISH)
                else:
                    self.__DEPLOYED_FISHES.insert(random.randrange(0, len(self.__DEPLOYED_FISHES)), SPAWNEDFISH) # deploy the wanted fish

            if SPAWNEDHUMAN != None:
                if len(self.__DEPLOYED_HUMANS) == 0:
                    self.__DEPLOYED_HUMANS.append(SPAWNEDHUMAN)
                else:
                    self.__DEPLOYED_HUMANS.insert(random.randrange(0, len(self.__DEPLOYED_HUMANS)), SPAWNEDHUMAN)  # deploy the wanted fish



            # - - - - - - MOVEMENT - - - - - - #


            # --- FISHES --- #

            for FISH in self.__DEPLOYED_FISHES: # For all the fish in existence
                if FISH.ifDead() == False:
                    if FISH.getSpeed() != 0: # if they are moving
                        FISH.setMovePOS(FISH.getX(), FISH.getY(), FISH.getWidth(), FISH.getHeight()) # make move animation on screen
                        FISH.moveAnimation() # make it animate
                    FISH.marqueeX(self.__WINDOW.getWidth())  # make it move horizontally
                    FISH.setSpeed(FISH.getInitialSpeed()) # sets it's speed back to its originial amount
                    # --- FISH RANGE MECHANICS --- #
                    for HUMAN in self.__DEPLOYED_HUMANS: #
                        if FISH.inFishRange(HUMAN.getWidth(), HUMAN.getX()): # when fish encounters a human
                            FISH.setSpeed(0) # make fish speed zero
                            if FISH.isAttacking() == False: # they aren't attacking
                                FISH.idleAnimation() # idle animation
                                FISH.setIdlePOS(FISH.getX(), FISH.getY(), FISH.getWidth(), FISH.getHeight()) #make it on screen


            # --- HUMANS --- #
            for HUMAN in self.__DEPLOYED_HUMANS: # For all the HUMAN in existence
                if HUMAN.getSpeed() != 0: # if they are moving
                    HUMAN.setMovePOS(HUMAN.getX(), HUMAN.getY(), HUMAN.getWidth(), HUMAN.getHeight()) # make move animation on screen
                    HUMAN.moveAnimation() # make it animate
                HUMAN.marqueeX(self.__WINDOW.getWidth())  # make it move horizontally
                HUMAN.setSpeed(HUMAN.getInitialSpeed()) # sets it's speed back to its originial amount
                # --- HUMAN RANGE MECHANICS - - - #
                for FISH in self.__DEPLOYED_FISHES: #
                    if HUMAN.inHumanRange(FISH.getX()): # when HUMAN encounters a human
                        HUMAN.setSpeed(0) # make HUMAN speed zero
                        if HUMAN.isAttacking() == False: # they aren't attacking
                            HUMAN.idleAnimation() # idle animation
                            HUMAN.setIdlePOS(HUMAN.getX(), HUMAN.getY(), HUMAN.getWidth(), HUMAN.getHeight()) #make it on screen



            for ATTACK in self.__LIVE_FISH_ATTACKS:
                ATTACK.marqueeX(self.__WINDOW.getWidth())

            for ATTACK in self.__LIVE_HUMAN_ATTACKS:
                ATTACK.marqueeX(self.__WINDOW.getWidth())


            self.__fishOutputAttack()
            self.__humanAttackCollision()
            self.__humanOutputAttack()
            self.__fishAttackCollision()
            self.__checkDeath()


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

            for FISH in self.__DEPLOYED_FISHES:
                FISH.updateAttackCooldown(self.__TIME_PASSED)
                FISH.updateAttackAnimationDuration(self.__TIME_PASSED)
                FISH.updateDeathAnimationDuration(self.__TIME_PASSED)

            for HUMAN in self.__DEPLOYED_HUMANS:
                HUMAN.updateAttackCooldown(self.__TIME_PASSED)
                HUMAN.updateAttackAnimationDuration(self.__TIME_PASSED)
                HUMAN.updateDeathAnimationDuration(self.__TIME_PASSED)









    def __spawnFish(self, KEYPRESSED):
        '''
        checks if they clicked any of the following buttons
        :param KEYPRESSED:
        :return:
        '''

        if self.__FISH_CURRENT_SPAWN_COOLDOWN[4] >= self.__FISH_SPAWN_COOLDOWN[4]:
            if KEYPRESSED[pygame.K_5] == 1:
                if self.__INCOME >= self.__OCTOPUS_COST:
                    self.__createOctopus()

    def __spawnHuman(self):
        '''
        checks if they clicked any of the following buttons
        :return:
        '''

        if self.__HUMAN_CURRENT_SPAWN_COOLDOWN[0] >= self.__HUMAN_SPAWN_COOLDOWN[0]:
            self.__createHumanWand()

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

        #for FISH in self.__DEPLOYED_FISHES:
        #    self.__WINDOW.getSurface().blit(FISH.getSurface(), FISH.getPOS())
##
        #for HUMAN in self.__DEPLOYED_HUMANS:
        #    self.__WINDOW.getSurface().blit(HUMAN.getSurface(), HUMAN.getPOS())

        for ATTACK in self.__LIVE_FISH_ATTACKS:
            self.__WINDOW.getSurface().blit(ATTACK.getSurface(), ATTACK.getPOS())

        for ATTACK in self.__LIVE_HUMAN_ATTACKS:
            self.__WINDOW.getSurface().blit(ATTACK.getSurface(), ATTACK.getPOS())

        for FISH in self.__DEPLOYED_FISHES:
            FISH.getGroupAnimation().draw(self.__WINDOW.getSurface())
            FISH.updateGroupAnimation()

        for HUMAN in self.__DEPLOYED_HUMANS:
            HUMAN.getGroupAnimation().draw(self.__WINDOW.getSurface())
            HUMAN.updateGroupAnimation()

        self.__WINDOW.updateFrame()


    def __fishOutputAttack(self):
        for FISH in self.__DEPLOYED_FISHES:
            if FISH.ifDead() == False:
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
                if HUMAN.getCurrentAttackCooldown() >= HUMAN.getAttackCooldown(): # if its allowed to attack again
                    HUMAN.attackAnimation() # activates attack animation
                    HUMAN.setAttackPOS(HUMAN.getX(), HUMAN.getY(), HUMAN.getWidth(), HUMAN.getHeight()) # makes attack animation come on screen
                    HUMAN.resetCurrentAttackAnimationDuration()  # makes attack duration = 0
                    HUMAN.resetAttackCooldown() # makes cooldown to 0, so it has to wait again before it can attack again
                if HUMAN.finishedAttacking(): # if their attack animation has finished
                    ATTACK = copy.copy(HUMAN.getAttack()) # create the actual attack
                    self.__LIVE_HUMAN_ATTACKS.append(ATTACK) #make it exist
                    if self.__LIVE_HUMAN_ATTACKS[-1].isProjectile():
                        self.__LIVE_HUMAN_ATTACKS[-1].setScale(15, 15)
                        self.__LIVE_HUMAN_ATTACKS[-1].setY(HUMAN.getY() + HUMAN.getWidth() // 5)  # place it at proper height of the unit
                    else:
                        self.__LIVE_HUMAN_ATTACKS[-1].setY(HUMAN.getY() + HUMAN.getWidth() // 2 - ATTACK.getWidth() // 2)  # place it at proper height of the unit
                    self.__LIVE_HUMAN_ATTACKS[-1].setX(HUMAN.getX() + HUMAN.getWidth())  # place it where the unit is positions on the X axis


                    HUMAN.updateAttackAnimationDuration(1000) # make the cooldown 1000, so that it wont continuously attack. So now, I acutally dont know how this works but it seems fine





    def __humanAttackCollision(self):
        for i in range(len(self.__LIVE_HUMAN_ATTACKS)-1,-1,-1):
            for j in range(len(self.__DEPLOYED_FISHES)-1,-1,-1): # for all the fish deployed
                if self.__DEPLOYED_FISHES[j].ifDead() == False:
                    try:
                        if self.__LIVE_HUMAN_ATTACKS[i].isCollision(self.__DEPLOYED_FISHES[j].getWidth(), self.__DEPLOYED_FISHES[j].getHeight(), self.__DEPLOYED_FISHES[j].getPOS()):
                            self.__DEPLOYED_FISHES[j].takeDamage(self.__LIVE_HUMAN_ATTACKS[i].getDamage())
                            self.__LIVE_HUMAN_ATTACKS.pop(i)
                    except IndexError:
                        print("Errored")
                        pass


    def __fishAttackCollision(self):
        for i in range(len(self.__LIVE_FISH_ATTACKS)-1,-1,-1):
            for j in range(len(self.__DEPLOYED_HUMANS)-1,-1,-1): # for all the fish deployed
                try:
                    if self.__LIVE_FISH_ATTACKS[i].isCollision(self.__DEPLOYED_HUMANS[j].getWidth(), self.__DEPLOYED_HUMANS[j].getHeight(), self.__DEPLOYED_HUMANS[j].getPOS()):
                        self.__DEPLOYED_HUMANS[j].takeDamage(self.__LIVE_FISH_ATTACKS[i].getDamage())
                        print(self.__DEPLOYED_HUMANS[j].getHealth())
                        self.__LIVE_FISH_ATTACKS.pop(i)
                except IndexError:
                    print("Errored")
                    pass

    def __checkDeath(self):
        for i in range(len(self.__DEPLOYED_FISHES)-1,-1,-1):
            if self.__DEPLOYED_FISHES[i].ifDead() == False:
                if self.__DEPLOYED_FISHES[i].getHealth() <= 0:
                    self.__DEPLOYED_FISHES[i].isDead()
                    self.__DEPLOYED_FISHES[i].deathAnimation()
                    self.__DEPLOYED_FISHES[i].setDeathPOS(self.__DEPLOYED_FISHES[i].getX(), self.__DEPLOYED_FISHES[i].getY(), self.__DEPLOYED_FISHES[i].getWidth(), self.__DEPLOYED_FISHES[i].getHeight())
                    self.__DEPLOYED_FISHES[i].beginDeathAnimationDuration()  # makes attack duration = 0
                    self.__DEPLOYED_FISHES[i].getDeathTimers()
            if self.__DEPLOYED_FISHES[i].finishedDying(): # if their attack animation has finished
                self.__DEPLOYED_FISHES.pop(i)


        for i in range(len(self.__DEPLOYED_HUMANS)-1,-1,-1):
            if self.__DEPLOYED_HUMANS[i].ifDead() == False:
                if self.__DEPLOYED_HUMANS[i].getHealth() <= 0:
                    self.__DEPLOYED_HUMANS[i].isDead()
                    self.__DEPLOYED_HUMANS[i].deathAnimation()
                    self.__DEPLOYED_HUMANS[i].setDeathPOS(self.__DEPLOYED_HUMANS[i].getX(), self.__DEPLOYED_HUMANS[i].getY(), self.__DEPLOYED_HUMANS[i].getWidth(), self.__DEPLOYED_HUMANS[i].getHeight())
                    self.__DEPLOYED_HUMANS[i].beginDeathAnimationDuration()  # makes attack duration = 0
                    self.__DEPLOYED_HUMANS[i].getDeathTimers()
            if self.__DEPLOYED_HUMANS[i].finishedDying(): # if their attack animation has finished
                self.__DEPLOYED_HUMANS.pop(i)





    # --- FISH CREATION FUNCTIONS --- #
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
        # ATTACK CONFIG (DAMAGE, RANGE, SPEED)
        self.__OCTOPUS = MyUnit("media/octopus/oct6attack.png", self.__FISH_SPAWN_LOCATION, self.__FISH_SPEED[4],self.__FISH_MAX_HEALTH[4], self.__FISH_RANGE[4],Attacks("media/humanBase.png", 50000000, 45, 5, -1), self.__FISH_ATTACK_COOLDOWN[4], -1,self.__OCTIDLE, self.__OCTMOVE, self.__OCTATTACK,self.__OCTDEATH, self.__oct_moving_sprites, 0.8)

        self.__OCTOPUS.setScale(3)
        self.__OCTOPUS.flipSprite()
        # RESETS COOLDOWN, SUBRACTS MONEY, AND ADDS IT TO DEPLOYED UNITS
        self.__FISH_CURRENT_SPAWN_COOLDOWN[4] = 0
        self.__INCOME -= self.__OCTOPUS_COST
        self.__DEPLOYED_FISHES.append(self.__OCTOPUS)
        self.__OCTOPUS.setY(300 - self.__OCTOPUS.getHeight())


    # --- HUMAN CREATION FUNCTIONS -- #


    def __createHumanWand(self):
        # Animation Creation
        self.__human_wand_moving_sprites = pygame.sprite.Group()

        self.__WANDATTACK = Wandattack(500, 800)

        self.__human_wand_moving_sprites.add(self.__WANDATTACK)


        self.__WANDMOVE = Wandmove(500, 800)

        self.__human_wand_moving_sprites.add(self.__WANDMOVE)

        self.__WANDDEATH = Wanddeath(500, 800)

        self.__human_wand_moving_sprites.add(self.__WANDDEATH)

        self.__WANDIDLE = Wandidle(500, 800)

        self.__human_wand_moving_sprites.add(self.__WANDIDLE)

        # ACTUALLY CREATES THE UNIT WITH ALL THEIR RESPECTIVE ATTRIBUTES
        # ATTACK CONFIGURATIONS (DAMAGE, RANGE, SPEED)
        self.__WAND = MyUnit("media/wand/wand1idle.png", self.__HUMAN_SPAWN_LOCATION, self.__HUMAN_SPEED[0],self.__HUMAN_MAX_HEALTH[0], self.__HUMAN_RANGE[0], Attacks("media/wand/Projectile.png", 50, self.__HUMAN_RANGE[0], 4, 1, 40, True), self.__HUMAN_ATTACK_COOLDOWN[0], 1 , self.__WANDIDLE, self.__WANDMOVE, self.__WANDATTACK, self.__WANDDEATH, self.__human_wand_moving_sprites, 0.8)
        print("Object Width: ", self.__WAND.getWidth())
        print("Animation Width", self.__WANDIDLE.getWidth())
        self.__WAND.setScale(3)


        # RESETS COOLDOWN, SUBRACTS MONEY, AND ADDS IT TO DEPLOYED UNITS
        self.__HUMAN_CURRENT_SPAWN_COOLDOWN[0] = 0
        self.__WAND.setY(300 - self.__WAND.getHeight())
        self.__DEPLOYED_HUMANS.append(self.__WAND)





if __name__ == "__main__":
    GAME = Game()
    GAME.run()
