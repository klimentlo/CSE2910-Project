
from image_sprite import ImageSprite
from my_unit import MyUnit
from text import Text
from unit_attacks import Attacks
from window import Window
from box import Box
from color import Color
import time, random, copy
import pygame

from animation import Octidle, Octmove, Octattack, Octdeath
from animation import Wandidle, Wandmove, Wandattack, Wanddeath
from animation import Swordidle, Swordmove, Swordattack, Sworddeath
from animation import Eelidle, Eelmove, Eelattack, Eeldeath
pygame.init()


class Game():
    '''
    game class
    '''
    def __init__(self):
        # Window & Background
        self.__WINDOW = Window("background", 1233, 384, 30)
        self.__BACKGROUND = ImageSprite("media/underwater-fantasy-background.png")
        self.__BACKGROUND.setScale(3)
        # Income
        self.__INCOME = 5000
        self.__INCOME_TEXT = Text(f"${self.__INCOME}")
        self.__INCOME_TEXT.setPOS(self.__WINDOW.getWidth() - self.__INCOME_TEXT.getWidth() - 25, 25)

        # - - - Bases
        self.__TOWERS = []
        # - Enemy Tower
        self.__E_MAX_HEALTH = 5000
        self.__E_TOWER = MyUnit("media/enemybase1.png", None , None ,self.__E_MAX_HEALTH, None, None, None, None , None, None, None, None, None, None)
        self.__E_TOWER.setScale(4 / 10)
        self.__E_TOWER.setY(190)
        self.__E_TOWER.setX(-10)
        self.__TOWERS.append(self.__E_TOWER)

        # Health Text & Bar
        self.__E_TOWER_HEALTH_TEXT = Text(f"{self.__E_MAX_HEALTH}", "ComicSans", 18)
        self.__E_TOWER_HEALTH_TEXT.setPOS(self.__E_TOWER.getX() + (self.__E_TOWER.getWidth()//2 - self.__E_TOWER_HEALTH_TEXT.getWidth()//2),self.__E_TOWER.getY() - 5)
        self.__E_TOWER_HEALTH_BAR = Box(100, 10)
        self.__E_TOWER_HEALTH_BAR.setPOS(self.__E_TOWER_HEALTH_TEXT.getX() + (self.__E_TOWER_HEALTH_TEXT.getWidth()//2 - self.__E_TOWER_HEALTH_BAR.getWidth()//2), self.__E_TOWER_HEALTH_TEXT.getY() + self.__E_TOWER_HEALTH_TEXT.getHeight())
        self.__E_TOWER_HEALTH_BAR.setColor(Color.GREEN)

        self.__E_TOWER_DAMAGE_BAR = Box(100, 10)
        self.__E_TOWER_DAMAGE_BAR.setPOS(self.__E_TOWER_HEALTH_TEXT.getX() + (self.__E_TOWER_HEALTH_TEXT.getWidth() // 2 - self.__E_TOWER_HEALTH_BAR.getWidth() // 2),self.__E_TOWER_HEALTH_TEXT.getY() + self.__E_TOWER_HEALTH_TEXT.getHeight())

        self.__E_TOWER_DAMAGE_BAR.setColor(Color.RED)




        self.__A_HEALTH = 5000
        self.__A_TOWER = MyUnit("media/allybase11.png", None, None, self.__A_HEALTH, None, None, None, None, None, None,None, None, None, None)
        self.__A_TOWER.setScale(0.80)
        self.__A_TOWER.setY(90)
        self.__A_TOWER.setX(1015)
        self.__TOWERS.append(self.__A_TOWER)


        #
        self.__DEPLOYED_FISHES = []
        self.__DEPLOYED_HUMANS = []
        self.__LIVE_FISH_ATTACKS = []
        self.__LIVE_HUMAN_ATTACKS = []
        self.__TIME = time.time()
        self.__PREVIOUS_TIME = self.__TIME
        self.__TIME_PASSED = 0.12

        # - - - - - - - - - - - - - - - - - - - - #
        #   -  -  - FISH CONFIGURATIONS -  -  -   #
        # - - - - - - - - - - - - - - - - - - - - #

        # --- GENERAL ATTRIBUTE CONFIGURATION --- #

        self.__FISH_SPAWN_LOCATION = self.__WINDOW.getWidth()-200

        self.__FISH_SPAWN_COOLDOWN = [2.0, 3.0, 4.0, 5.0, 1.0]
        self.__FISH_CURRENT_SPAWN_COOLDOWN = [2.0, 3.0, 4.0, 5.0, 1.0]
        self.__FISH_MAX_HEALTH = [200, 5, 5, 50, 200]
        self.__FISH_RANGE = [50, 100, 150, 200, -50]
        self.__FISH_SPEED = [1, 2, 3, 4, 5]
        self.__FISH_ATTACK_COOLDOWN = [1, 2, 3, 4, 3]
        self.__FISH_ATTACK_DAMAGE = [5, 10, 15, 20, 300]

        # --- COST OF THE UNITS --- #
        self.__OCTOPUS_COST = 400
        self.__EEL_COST = 300

        # - - - - - - - - - - - - - - - - - - - - - #
        #    -  -  - HUMAN CONFIGURATIONS -  -  -   #
        # - - - - - - - - - - - - - - - - - - - - - #

        # Human Spawning Cooldown
        self.__HUMAN_SPAWN_COOLDOWN = [10.0, 10.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0]
        self.__HUMAN_CURRENT_SPAWN_COOLDOWN = [8.0, 9.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0]


        self.__HUMAN_SPAWN_LOCATION = 60
        self.__HUMAN_SPEED = [2.5, 1.5, 3, 4, 5]
        self.__HUMAN_MAX_HEALTH = [250, 100, 150, 200, 250]
        self.__HUMAN_RANGE = [-80, 100, 150, 200, 250]
        self.__HUMAN_ATTACK_COOLDOWN = [1.2, 2, 3, 4, 5]
        self.__HUMAN_ATTACK_DAMAGE = [5.0, 10.0, 15.0, 20.0]


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

                if FISH.inFishRange(self.__E_TOWER.getWidth(), self.__E_TOWER.getX()):  # when fish encounters a human
                    FISH.setSpeed(0)  # make fish speed zero
                    if FISH.isAttacking() == False:  # they aren't attacking
                        FISH.idleAnimation()  # idle animation
                        FISH.setIdlePOS(FISH.getX(), FISH.getY(), FISH.getWidth(),
                                        FISH.getHeight())  # make it on screen


            # --- HUMANS --- #
            for HUMAN in self.__DEPLOYED_HUMANS: # For all the HUMAN in existence
                if HUMAN.ifDead() == False:
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
                    # TOWERS
                    if HUMAN.inHumanRange(self.__A_TOWER.getX()):  # when in human's range
                        HUMAN.setSpeed(0)  # make HUMAN speed zero
                        if HUMAN.isAttacking() == False:  # they aren't attacking
                            HUMAN.idleAnimation()  # idle animation
                            HUMAN.setIdlePOS(HUMAN.getX(), HUMAN.getY(), HUMAN.getWidth(),
                                             HUMAN.getHeight())  # make it on screen





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

        if self.__FISH_CURRENT_SPAWN_COOLDOWN[3] >= self.__FISH_SPAWN_COOLDOWN[3]:
            if KEYPRESSED[pygame.K_4] == 1:
                if self.__INCOME >= self.__EEL_COST:
                    self.__createEel()

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
            self.__createHumanSword()

        if self.__HUMAN_CURRENT_SPAWN_COOLDOWN[1] >= self.__HUMAN_SPAWN_COOLDOWN[1]:
            self.__createHumanWand()

    def __updateWindowFrame(self):
        self.__WINDOW.clearScreen()
        self.__WINDOW.getSurface().blit(self.__BACKGROUND.getSurface(), self.__BACKGROUND.getPOS())
        self.__WINDOW.getSurface().blit(self.__INCOME_TEXT.getSurface(), self.__INCOME_TEXT.getPOS())

        for TOWER in self.__TOWERS:
            self.__WINDOW.getSurface().blit(TOWER.getSurface(), TOWER.getPOS())

        self.__WINDOW.getSurface().blit(self.__E_TOWER_HEALTH_TEXT.getSurface(), self.__E_TOWER_HEALTH_TEXT.getPOS())
        self.__WINDOW.getSurface().blit(self.__E_TOWER_DAMAGE_BAR.getSurface(), self.__E_TOWER_DAMAGE_BAR.getPOS())
        self.__WINDOW.getSurface().blit(self.__E_TOWER_HEALTH_BAR.getSurface(), self.__E_TOWER_HEALTH_BAR.getPOS())

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
                        self.__LIVE_FISH_ATTACKS.pop(i)
                except IndexError:
                    print("Errored")
                    pass
            # enemy towwer collides with fish attack
            try:
                if self.__LIVE_FISH_ATTACKS[i].isCollision(self.__E_TOWER.getWidth(), self.__E_TOWER.getHeight(),self.__E_TOWER.getPOS()):

                    self.__E_TOWER.takeDamage(self.__LIVE_FISH_ATTACKS[i].getDamage())
                    self.__E_TOWER_HEALTH_TEXT.setText(f"{self.__E_TOWER.getHealth()}")
                    self.__E_TOWER_HEALTH_TEXT.setPOS(self.__E_TOWER.getX() + (self.__E_TOWER.getWidth() // 2 - self.__E_TOWER_HEALTH_TEXT.getWidth() // 2),self.__E_TOWER.getY() - 5)
                    try:
                        self.__E_TOWER_HEALTH_BAR = Box((self.__E_TOWER.getHealth()/self.__E_MAX_HEALTH) * self.__E_TOWER_DAMAGE_BAR.getWidth(), self.__E_TOWER_DAMAGE_BAR.getHeight())
                        self.__E_TOWER_HEALTH_BAR.setColor(Color.GREEN)
                        self.__E_TOWER_HEALTH_BAR.setPOS(self.__E_TOWER_HEALTH_TEXT.getX() + (self.__E_TOWER_HEALTH_TEXT.getWidth() // 2 - self.__E_TOWER_DAMAGE_BAR.getWidth() // 2),self.__E_TOWER_HEALTH_TEXT.getY() + self.__E_TOWER_HEALTH_TEXT.getHeight())
                    except pygame.error:
                        self.__ROUND = "Complete"
                    self.__LIVE_FISH_ATTACKS.pop(i)
            except IndexError:
                pass





    def __checkDeath(self):
        for i in range(len(self.__DEPLOYED_FISHES)-1,-1,-1):
            if self.__DEPLOYED_FISHES[i].ifDead() == False:
                if self.__DEPLOYED_FISHES[i].getHealth() <= 0:
                    self.__DEPLOYED_FISHES[i].isDead()
                    self.__DEPLOYED_FISHES[i].deathAnimation()
                    self.__DEPLOYED_FISHES[i].setDeathPOS(self.__DEPLOYED_FISHES[i].getX(), self.__DEPLOYED_FISHES[i].getY(), self.__DEPLOYED_FISHES[i].getWidth(), self.__DEPLOYED_FISHES[i].getHeight())
                    self.__DEPLOYED_FISHES[i].beginDeathAnimationDuration()  # makes attack duration = 0
            if self.__DEPLOYED_FISHES[i].finishedDying(): # if their attack animation has finished
                self.__DEPLOYED_FISHES.pop(i)


        for i in range(len(self.__DEPLOYED_HUMANS)-1,-1,-1):
            if self.__DEPLOYED_HUMANS[i].ifDead() == False:
                if self.__DEPLOYED_HUMANS[i].getHealth() <= 0:
                    self.__DEPLOYED_HUMANS[i].isDead()
                    self.__DEPLOYED_HUMANS[i].deathAnimation()
                    self.__DEPLOYED_HUMANS[i].setDeathPOS(self.__DEPLOYED_HUMANS[i].getX(), self.__DEPLOYED_HUMANS[i].getY(), self.__DEPLOYED_HUMANS[i].getWidth(), self.__DEPLOYED_HUMANS[i].getHeight())
                    self.__DEPLOYED_HUMANS[i].beginDeathAnimationDuration()  # makes attack duration = 0
                    print("I JUST DIED")
            if self.__DEPLOYED_HUMANS[i].finishedDying(): # if their attack animation has finished
                print("Finished Dying")
                self.__DEPLOYED_HUMANS.pop(i)





    # --- FISH CREATION FUNCTIONS --- #
    def __createOctopus(self):
        # OCTOPUS (index 4)
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
        self.__OCTOPUS = MyUnit("media/octopus/oct6attack.png", self.__FISH_SPAWN_LOCATION, self.__FISH_SPEED[4],self.__FISH_MAX_HEALTH[4], self.__FISH_RANGE[4],Attacks("media/sword/sword1death.png", self.__FISH_ATTACK_DAMAGE[4], self.__FISH_RANGE[4], 5, -1), self.__FISH_ATTACK_COOLDOWN[4], -1,self.__OCTIDLE, self.__OCTMOVE, self.__OCTATTACK,self.__OCTDEATH, self.__oct_moving_sprites, 0.8)
        self.__OCTOPUS.setScale(3)
        self.__OCTOPUS.flipSprite()
        # RESETS COOLDOWN, SUBRACTS MONEY, AND ADDS IT TO DEPLOYED UNITS
        self.__FISH_CURRENT_SPAWN_COOLDOWN[4] = 0
        self.__INCOME -= self.__OCTOPUS_COST
        self.__DEPLOYED_FISHES.append(self.__OCTOPUS)
        self.__OCTOPUS.setY(375 - self.__OCTOPUS.getHeight())


    def __createEel(self):
        # OCTOPUS (index 4)
        # ANIMATION CREATION
        self.__eel_moving_sprites = pygame.sprite.Group()
        self.__EELATTACK = Eelattack(300, 300)
        self.__eel_moving_sprites.add(self.__EELATTACK)
        self.__EELMOVE = Eelmove(300, 144)
        self.__eel_moving_sprites.add(self.__EELMOVE)
        self.__EELIDLE = Eelidle(300, 200)
        self.__eel_moving_sprites.add(self.__EELIDLE)
        self.__EELDEATH = Eeldeath(300, 150)
        self.__eel_moving_sprites.add(self.__EELDEATH)
        # CREATES OCTOPUS BASE UNIT
        # ATTACK CONFIG (DAMAGE, RANGE, SPEED)
        self.__EEL = MyUnit("media/octopus/oct6attack.png", self.__FISH_SPAWN_LOCATION, self.__FISH_SPEED[3],self.__FISH_MAX_HEALTH[3], self.__FISH_RANGE[3],Attacks("media/sword/sword1death.png", self.__FISH_ATTACK_DAMAGE[3], self.__FISH_RANGE[3], 5, -1), self.__FISH_ATTACK_COOLDOWN[3], -1,self.__EELIDLE, self.__EELMOVE, self.__EELATTACK, self.__EELDEATH, self.__eel_moving_sprites, 0.8)
        self.__EEL.setScale(3)
        self.__EEL.flipSprite()
        # RESETS COOLDOWN, SUBRACTS MONEY, AND ADDS IT TO DEPLOYED UNITS
        self.__FISH_CURRENT_SPAWN_COOLDOWN[3] = 0
        self.__INCOME -= self.__EEL_COST
        self.__DEPLOYED_FISHES.append(self.__EEL)
        self.__EEL.setY(375 - self.__EEL.getHeight())



    # --- HUMAN CREATION FUNCTIONS -- #


    def __createHumanSword(self):
        self.__human_sword_moving_sprites = pygame.sprite.Group()
        self.__SWORDATTACK = Swordattack(300, 150)
        self.__human_sword_moving_sprites.add(self.__SWORDATTACK)
        self.__SWORDMOVE = Swordmove(400, 200)
        self.__human_sword_moving_sprites.add(self.__SWORDMOVE)
        self.__SWORDDEATH = Sworddeath(400, 300)
        self.__human_sword_moving_sprites.add(self.__SWORDDEATH)
        self.__SWORDIDLE = Swordidle(400, 400)
        self.__human_sword_moving_sprites.add(self.__SWORDIDLE)
        self.__SWORD = MyUnit("media/sword/sword1idle.png", self.__HUMAN_SPAWN_LOCATION, self.__HUMAN_SPEED[0],
                             self.__HUMAN_MAX_HEALTH[0], self.__HUMAN_RANGE[0],
                             Attacks("media/wand/Projectile.png", self.__HUMAN_ATTACK_DAMAGE[0], self.__HUMAN_RANGE[0], 4, 1, 40, False),
                             self.__HUMAN_ATTACK_COOLDOWN[0], 1, self.__SWORDIDLE, self.__SWORDMOVE, self.__SWORDATTACK,
                             self.__SWORDDEATH, self.__human_sword_moving_sprites, 10.0)
        self.__SWORD.setScale(3)
        # RESETS COOLDOWN, SUBRACTS MONEY, AND ADDS IT TO DEPLOYED UNITS
        self.__HUMAN_CURRENT_SPAWN_COOLDOWN[0] = 0
        self.__SWORD.setY(375 - self.__SWORD.getHeight())
        self.__DEPLOYED_HUMANS.append(self.__SWORD)

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
        self.__WAND = MyUnit("media/wand/wand1idle.png", self.__HUMAN_SPAWN_LOCATION, self.__HUMAN_SPEED[1],self.__HUMAN_MAX_HEALTH[1], self.__HUMAN_RANGE[1], Attacks("media/wand/Projectile.png", self.__HUMAN_ATTACK_DAMAGE[1], self.__HUMAN_RANGE[1], 4, 1, 40, True), self.__HUMAN_ATTACK_COOLDOWN[1], 1 , self.__WANDIDLE, self.__WANDMOVE, self.__WANDATTACK, self.__WANDDEATH, self.__human_wand_moving_sprites, 0.8)
        self.__WAND.setScale(3)
        # RESETS COOLDOWN, SUBRACTS MONEY, AND ADDS IT TO DEPLOYED UNITS
        self.__HUMAN_CURRENT_SPAWN_COOLDOWN[1] = 0
        self.__WAND.setY(375 - self.__WAND.getHeight())
        self.__DEPLOYED_HUMANS.append(self.__WAND)





if __name__ == "__main__":
    GAME = Game()
    GAME.run()
