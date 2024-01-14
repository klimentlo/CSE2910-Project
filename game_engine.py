
from image_sprite import ImageSprite
from my_unit import MyUnit
from text import Text
from unit_attacks import Attacks
from window import Window
from box import Box
from color import Color
import time, copy, random
import pygame

from animation import Octidle, Octmove, Octattack, Octdeath
from animation import Wandidle, Wandmove, Wandattack, Wanddeath
from animation import Swordidle, Swordmove, Swordattack, Sworddeath
from animation import Eelidle, Eelmove, Eelattack, Eeldeath
from animation import Swordfishidle, Swordfishmove, Swordfishattack, Swordfishdeath
from animation import Lighting
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


        # Menu related
        self.__PLAYING = False
        self.__FIRST_SCREEN = []
        self.__MENU_BACKGROUND = ImageSprite("media/menu/fullimage.png")
        self.__MENU_BACKGROUND.setScale(1.61, 2)
        self.__TITLE_TEXT = ImageSprite("media/menu/title.png")
        self.__TITLE_TEXT.setScale(0.5)
        self.__TITLE_TEXT.setPOS(self.__WINDOW.getWidth() // 2 - self.__TITLE_TEXT.getWidth() // 2, 0)
        self.__PVP_TEXT = ImageSprite("media/menu/pve.png")
        self.__PVP_TEXT.setScale(0.2)
        self.__PVP_TEXT.setPOS(self.__WINDOW.getWidth() // 2 - self.__PVP_TEXT.getWidth() // 2, 220)
        self.__FIRST_SCREEN.append(self.__TITLE_TEXT)
        self.__FIRST_SCREEN.append(self.__PVP_TEXT)
        self.__DISPLAY = self.__FIRST_SCREEN
        self.__CURRENT_SCREEN = 0
        self.__CURRENT_LEVEL = 0
        self.__LEVEL = 4
        self.__SKILLPOINTS = 4
        self.__LEVEL_SELECTOR = False
        self.__SKILLPOINTS_SELECTOR = False
        self.__WIN = None
        self.__HEALTH_SPAWN1 = True
        self.__HEALTH_SPAWN2 = True
        self.__HEALTH_SPAWN3 = True
        self.__HEALTH_SPAWN4 = True

        self.__INCOME = 0
        self.__INCOME_TEXT = Text(f"${self.__INCOME}", "Times New Roman")
        self.__INCOME_TEXT.setPOS(self.__WINDOW.getWidth() - self.__INCOME_TEXT.getWidth() - 25, 25)
        self.__FISH_SPAWN_LOCATION = self.__WINDOW.getWidth() - 175
        self.__HUMAN_SPAWN_LOCATION = 60

        self.__INCOME_MULTIPLIER = 1
        self.__DAMAGE_MULTIPLIER = 1
        self.__HEALTH_MULTIPLIER = 1

        # Lists for the objects in the game
        self.__TIME = time.time()
        self.__PREVIOUS_TIME = self.__TIME
        self.__TIME_PASSED = 0.05
        self.__SPAWN_TIME_PASSED = 0.1
        self.__SP_TIME_PASSED = 0.3









    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()


                while self.__PLAYING == False:
                    self.__menu()
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            exit()

            self.__incomeGeneration(self.__INCOME_MULTIPLIER)
            # - - - SPAWNING - - - #
            self.__spawnControl()
            # Movement Functions
            self.__fishMovement()
            self.__humanMovement()
            self.__attackMovement()
            # Attack Functions
            self.__checkDeath()
            self.__fishOutputAttack()
            self.__humanOutputAttack()

            # Collision Functions
            self.__humanAttackCollision()
            self.__fishAttackCollision()

            # Death Detection


            # Updates
            self.__updateTimers()
            self.__updateWindowFrame()
            self.__endScreen()










    def __incomeGeneration(self, MULTIPLIER=1):
        if self.__WIN == None:
            self.__INCOME += (1 * MULTIPLIER)
            self.__INCOME_TEXT.setText(f"$ {round(self.__INCOME)}")
            self.__INCOME_TEXT.setPOS(self.__WINDOW.getWidth() - self.__INCOME_TEXT.getWidth() - 25, 25)


    def __fishMovement(self):
        for FISH in self.__DEPLOYED_FISHES:  # For all the fish in existence
            if FISH.ifDead() == False:
                if FISH.getSpeed() != 0:  # if they are moving
                    FISH.setMovePOS(FISH.getX(), FISH.getY(), FISH.getWidth(),
                                    FISH.getHeight())  # make move animation on screen
                    FISH.moveAnimation()  # make it animate
                FISH.marqueeX(self.__WINDOW.getWidth())  # make it move horizontally
                if FISH.getUnit() != "media/swordfish/sfidle1.png":
                    FISH.setSpeed(FISH.getInitialSpeed())
                # --- FISH RANGE MECHANICS --- #
                if len(self.__DEPLOYED_HUMANS) > 0:
                    for h in range(len(self.__DEPLOYED_HUMANS) - 1, -1, -1):  #
                        if self.__DEPLOYED_HUMANS[h].ifDead() == False:
                            if FISH.inFishRange(self.__DEPLOYED_HUMANS[h].getWidth(),
                                                self.__DEPLOYED_HUMANS[h].getX()):  # when fish encounters a human
                                FISH.setSpeed(0)  # make fish speed zero
                                FISH.marqueeX(self.__WINDOW.getWidth())  # make it move horizontally
                                if FISH.isAttacking() == False:  # they aren't attacking
                                    FISH.idleAnimation()  # idle animation
                                    FISH.setIdlePOS(FISH.getX(), FISH.getY(), FISH.getWidth(),
                                                    FISH.getHeight())  # make it on screen
                else:
                    if FISH.finishedAttacking() == True:
                        FISH.setSpeed(FISH.getInitialSpeed())

            if FISH.inFishRange(self.__E_TOWER.getWidth(), self.__E_TOWER.getX()):  # when fish encounters a human
                FISH.setSpeed(0)  # make fish speed zero
                if FISH.isAttacking() == False:  # they aren't attacking
                    FISH.idleAnimation()  # idle animation
                    FISH.setIdlePOS(FISH.getX(), FISH.getY(), FISH.getWidth(),
                                    FISH.getHeight())  # make it on screen



    def __humanMovement(self):
        for HUMAN in self.__DEPLOYED_HUMANS:  # For all the HUMAN in existence
            if HUMAN.ifDead() == False:
                if HUMAN.getSpeed() != 0:  # if they are moving
                    HUMAN.setMovePOS(HUMAN.getX(), HUMAN.getY(), HUMAN.getWidth(),
                                     HUMAN.getHeight())  # make move animation on screen
                    HUMAN.moveAnimation()  # make it animate
                HUMAN.marqueeX(self.__WINDOW.getWidth())  # make it move horizontally
                HUMAN.setSpeed(HUMAN.getInitialSpeed())
                # --- HUMAN RANGE MECHANICS - - - #
                for FISH in self.__DEPLOYED_FISHES:  #
                    if FISH.ifDead() == False:
                        if HUMAN.inHumanRange(FISH.getX()):  # when HUMAN encounters a human
                            HUMAN.setSpeed(0)  # make HUMAN speed zero
                            if HUMAN.isAttacking() == False:  # they aren't attacking
                                HUMAN.idleAnimation()  # idle animation
                                HUMAN.setIdlePOS(HUMAN.getX(), HUMAN.getY(), HUMAN.getWidth(),
                                                 HUMAN.getHeight())  # make it on screen
                # TOWERS
                if HUMAN.inHumanRange(self.__A_TOWER.getX()):  # when in human's range
                    HUMAN.setSpeed(0)  # make HUMAN speed zero
                    if HUMAN.isAttacking() == False:  # they aren't attacking
                        HUMAN.idleAnimation()  # idle animation

                        HUMAN.setIdlePOS(HUMAN.getX(), HUMAN.getY(), HUMAN.getWidth(),
                                         HUMAN.getHeight())  # make it on screen


    def __spawnControl(self):
        KEYPRESSED = pygame.key.get_pressed()
        SPAWNEDFISH = self.__spawnFish(KEYPRESSED)
        SPAWNEDHUMAN = self.__spawnHuman()
        if SPAWNEDFISH != None:  # if a key was pressed
            self.__DEPLOYED_FISHES.append(SPAWNEDFISH)

        if SPAWNEDHUMAN != None:
            self.__DEPLOYED_HUMANS.append(SPAWNEDHUMAN)








    # - - - - - - - - - - - - - - - - - - - #
    # - - - - -  ATTACK FUNCTIONS - - - - - #
    # - - - - - - - - - - - - - - - - - - - #

    def __attackMovement(self):
        for ATTACK in self.__LIVE_FISH_ATTACKS:
            ATTACK.marqueeX(self.__WINDOW.getWidth())

        for ATTACK in self.__LIVE_HUMAN_ATTACKS:
            ATTACK.marqueeX(self.__WINDOW.getWidth())


    def __fishOutputAttack(self):
        # GENERAL FISH ATTACK CODE
        for FISH in self.__DEPLOYED_FISHES:
            if FISH.ifDead() == False:
                if FISH.getSpeed() == 0: # if their movement speed is zero
                    if FISH.getCurrentAttackCooldown() >= FISH.getAttackCooldown(): # if its allowed to attack again
                        FISH.updateAttackAnimationDuration(1000)  # make the cooldown 1000, so that it wont continuously attack. So now, I acutally dont know how this works but it seems fine
                        FISH.attackAnimation() # activates attack animation
                        FISH.setAttackPOS(FISH.getX(), FISH.getY(), FISH.getWidth(), FISH.getHeight()) # makes attack animation come on screen
                        FISH.resetCurrentAttackAnimationDuration()  # makes attack duration = 0
                        FISH.resetAttackCooldown() # makes cooldown to 0, so it has to wait again before it can attack again
                    if FISH.finishedAttacking(): # if their attack animation has finished
                        ATTACK = copy.copy(FISH.getAttack()) # create the actual attack
                        if FISH.ifDead() == False:
                            FISH.updateAttackAnimationDuration(1000)  # make the cooldown 1000, so that it wont continuously attack. So now, I acutally dont know how this works but it seems fine
                            self.__LIVE_FISH_ATTACKS.append(ATTACK)  # make it exist
                            self.__LIVE_FISH_ATTACKS[-1].setX(FISH.getX() - ATTACK.getWidth()+30)  # place it where the unit is positions on the X axis
                            self.__LIVE_FISH_ATTACKS[-1].setY(FISH.getY() + (FISH.getWidth() // 2 - ATTACK.getWidth() // 2))  # place it at proper height of the unit
                            # Checks if its spearfishes' attack, if so, itll continue on to the code below
                            if self.__LIVE_FISH_ATTACKS[-1].isLighting():
                                self.__LIVE_FISH_ATTACKS[-1].setLive(True)
                                self.__LIVE_FISH_ATTACKS[-1].setX(-500)  # place it where the unit is positions on the X axis

                    # ALL RELATED TO SPEAR FISH'S ATTACK
                    if len(self.__LIVE_FISH_ATTACKS) > 0:
                        for i in range(len(self.__LIVE_FISH_ATTACKS)-1, -1, -1):
                            if self.__LIVE_FISH_ATTACKS[i].isLive() == True: # identifies if it's been triggered and if it's lighting
                                FISH.setSpeed(0)
                                FISH.idleAnimation()
                                self.__LIVE_FISH_ATTACKS[i].updateAttackAnimationDuration(1000)
                                self.__LIVE_FISH_ATTACKS[i].attackAnimation()
                                self.__LIVE_FISH_ATTACKS[i].setAnimationPOS(FISH.getX() - self.__LIVE_FISH_ATTACKS[i].getWidth()+10, FISH.getY() + (FISH.getHeight()//2 - self.__LIVE_FISH_ATTACKS[i].getWidth()//2)+48)
                                self.__LIVE_FISH_ATTACKS[i].resetCurrentAttackAnimationDuration()  # makes attack duration = 0
                                self.__LIVE_FISH_ATTACKS[i].setLive(False)
                                self.__LIVE_FISH_ATTACKS[i].setX(FISH.getX() - self.__LIVE_FISH_ATTACKS[i].getWidth()+22)  # place it where the unit is positions on the X axis
                            if self.__LIVE_FISH_ATTACKS[i].isLighting():
                                if self.__LIVE_FISH_ATTACKS[i].finishedAttacking():
                                    if FISH.ifDead() == False:
                                        FISH.updateAttackAnimationDuration(1000)
                                        FISH.resetCurrentAttackAnimationDuration()  # makes attack duration = 0
                                        FISH.resetAttackCooldown()  # makes cooldown to 0, so it has to wait again before it can attack again
                                        self.__LIVE_FISH_ATTACKS[i].setAnimationPOS(1000, 1000)
                                        self.__LIVE_FISH_ATTACKS[i].updateAttackAnimationDuration(1000)
                                        self.__LIVE_FISH_ATTACKS.pop(i)  # place it where the unit is positions on the X axis
                                        FISH.setSpeed(FISH.getInitialSpeed())









    def __humanOutputAttack(self):
        for HUMAN in self.__DEPLOYED_HUMANS:
                if HUMAN.getSpeed() == 0: # if their movement speed is zero
                    if HUMAN.getCurrentAttackCooldown() >= HUMAN.getAttackCooldown(): # if its allowed to attack again
                        HUMAN.updateAttackAnimationDuration(1000)  # make the cooldown 1000, so that it wont continuously attack. So now, I acutally dont know how this works but it seems fine
                        HUMAN.attackAnimation() # activates attack animation

                        HUMAN.setAttackPOS(HUMAN.getX(), HUMAN.getY(), HUMAN.getWidth(), HUMAN.getHeight()) # makes attack animation come on screen
                        HUMAN.resetCurrentAttackAnimationDuration()  # makes attack duration = 0
                        HUMAN.resetAttackCooldown() # makes cooldown to 0, so it has to wait again before it can attack again
                    if HUMAN.finishedAttacking(): # if their attack animation has finished
                        HUMAN.updateAttackAnimationDuration(1000)  # make the cooldown 1000, so that it wont continuously attack. So now, I acutally dont know how this works but it seems fine
                        if HUMAN.ifDead() == False:
                            ATTACK = copy.copy(HUMAN.getAttack()) # create the actual attack
                            self.__LIVE_HUMAN_ATTACKS.append(ATTACK) #make it exist
                            if self.__LIVE_HUMAN_ATTACKS[-1].isProjectile():
                                self.__LIVE_HUMAN_ATTACKS[-1].setScale(15, 15)
                                self.__LIVE_HUMAN_ATTACKS[-1].setY(HUMAN.getY() + HUMAN.getWidth() // 5)  # place it at proper height of the unit
                                self.__LIVE_HUMAN_ATTACKS[-1].setX(HUMAN.getX() + HUMAN.getWidth() - 50)  # place it where the unit is positions on the X axis
                            else:
                                self.__LIVE_HUMAN_ATTACKS[-1].setY(HUMAN.getY() + HUMAN.getWidth() // 2 - ATTACK.getWidth() // 2)  # place it at proper height of the unit
                                self.__LIVE_HUMAN_ATTACKS[-1].setX(HUMAN.getX() + HUMAN.getWidth()-30)  # place it where the unit is positions on the X axis









    # - - - - - - - - - - - - - - - - - - - #
    # - - - - - ATTACK COLLISIONS - - - - - #
    # - - - - - AND DEATH CHECKIN - - - - - #
    # - - - - - - - - - - - - - - - - - - - #

    def __humanAttackCollision(self):
        for i in range(len(self.__LIVE_HUMAN_ATTACKS)-1,-1,-1):
            for j in range(len(self.__DEPLOYED_FISHES)-1,-1,-1): # for all the fish deployed
                if self.__DEPLOYED_FISHES[j].ifDead() == False:
                    try:
                        if self.__LIVE_HUMAN_ATTACKS[i].isCollision(self.__DEPLOYED_FISHES[j].getWidth(), self.__DEPLOYED_FISHES[j].getHeight(), self.__DEPLOYED_FISHES[j].getPOS()):
                            self.__DEPLOYED_FISHES[j].takeDamage(self.__LIVE_HUMAN_ATTACKS[i].getDamage())
                            self.__LIVE_HUMAN_ATTACKS.pop(i)
                    except IndexError:
                        pass
            try:
                if self.__LIVE_HUMAN_ATTACKS[i].isCollision(self.__A_TOWER.getWidth(), self.__A_TOWER.getHeight(),self.__A_TOWER.getPOS()):
                    self.__A_TOWER.takeDamage(self.__LIVE_HUMAN_ATTACKS[i].getDamage())
                    if self.__A_TOWER.getHealth() > 0:
                        self.__A_TOWER_HEALTH_TEXT.setText(f"{self.__A_TOWER.getHealth()}")
                    else:
                        self.__A_TOWER_HEALTH_TEXT.setText("0")
                    self.__A_TOWER_HEALTH_TEXT.setPOS(self.__A_TOWER.getX() + (self.__A_TOWER.getWidth() // 2 - self.__A_TOWER_HEALTH_TEXT.getWidth() // 2 +15),self.__A_TOWER.getY() + 95)
                    try:
                        self.__A_TOWER_HEALTH_BAR = Box((self.__A_TOWER.getHealth() / self.__A_MAX_HEALTH) * self.__A_TOWER_DAMAGE_BAR.getWidth(),self.__A_TOWER_DAMAGE_BAR.getHeight())
                        self.__A_TOWER_HEALTH_BAR.setColor(Color.GREEN)
                        self.__A_TOWER_HEALTH_BAR.setPOS(self.__A_TOWER_HEALTH_TEXT.getX() + (self.__A_TOWER_HEALTH_TEXT.getWidth() // 2 - self.__A_TOWER_DAMAGE_BAR.getWidth() // 2),self.__A_TOWER_HEALTH_TEXT.getY() + self.__A_TOWER_HEALTH_TEXT.getHeight())
                    except pygame.error:
                        self.__ROUND = "Complete"
                        self.__A_TOWER_HEALTH_BAR = Box(0, self.__A_TOWER_DAMAGE_BAR.getHeight())
                        self.__A_TOWER_HEALTH_BAR.setColor(Color.GREEN)
                        self.__A_TOWER_HEALTH_BAR.setPOS(self.__A_TOWER_HEALTH_TEXT.getX() + (self.__A_TOWER_HEALTH_TEXT.getWidth() // 2 - self.__A_TOWER_DAMAGE_BAR.getWidth() // 2),self.__A_TOWER_HEALTH_TEXT.getY() + self.__A_TOWER_HEALTH_TEXT.getHeight())
                    self.__LIVE_HUMAN_ATTACKS.pop(i)

            except IndexError:
                pass


    def __fishAttackCollision(self):
        for i in range(len(self.__LIVE_FISH_ATTACKS)-1,-1,-1):
            for j in range(len(self.__DEPLOYED_HUMANS)-1,-1,-1): # for all the fish deployed
                try:
                    if self.__LIVE_FISH_ATTACKS[i].isCollision(self.__DEPLOYED_HUMANS[j].getWidth(), self.__DEPLOYED_HUMANS[j].getHeight(), self.__DEPLOYED_HUMANS[j].getPOS()):
                        self.__DEPLOYED_HUMANS[j].takeDamage(self.__LIVE_FISH_ATTACKS[i].getDamage())
                        if self.__LIVE_FISH_ATTACKS[i].isLighting():
                            pass
                        else:
                            self.__POP_LATER = False
                            self.__LIVE_FISH_ATTACKS.pop(i)
                except IndexError:
                    pass
            # enemy towwer collides with fish attack
            try:
                if self.__LIVE_FISH_ATTACKS[i].isCollision(self.__E_TOWER.getWidth(), self.__E_TOWER.getHeight(),self.__E_TOWER.getPOS()):

                    self.__E_TOWER.takeDamage(self.__LIVE_FISH_ATTACKS[i].getDamage())
                    if self.__E_TOWER.getHealth() > 0:
                        self.__E_TOWER_HEALTH_TEXT.setText(f"{self.__E_TOWER.getHealth()}")
                    else:
                        self.__E_TOWER_HEALTH_TEXT.setText("0")
                    self.__E_TOWER_HEALTH_TEXT.setPOS(self.__E_TOWER.getX() + (self.__E_TOWER.getWidth() // 2 - self.__E_TOWER_HEALTH_TEXT.getWidth() // 2),self.__E_TOWER.getY() - 5)
                    try:
                        self.__E_TOWER_HEALTH_BAR = Box((self.__E_TOWER.getHealth()/self.__E_MAX_HEALTH) * self.__E_TOWER_DAMAGE_BAR.getWidth(), self.__E_TOWER_DAMAGE_BAR.getHeight())
                        self.__E_TOWER_HEALTH_BAR.setColor(Color.GREEN)
                        self.__E_TOWER_HEALTH_BAR.setPOS(self.__E_TOWER_HEALTH_TEXT.getX() + (self.__E_TOWER_HEALTH_TEXT.getWidth() // 2 - self.__E_TOWER_DAMAGE_BAR.getWidth() // 2),self.__E_TOWER_HEALTH_TEXT.getY() + self.__E_TOWER_HEALTH_TEXT.getHeight())
                    except pygame.error:
                        self.__ROUND = "Complete"
                        self.__E_TOWER_HEALTH_BAR = Box(0,self.__E_TOWER_DAMAGE_BAR.getHeight())
                        self.__E_TOWER_HEALTH_BAR.setColor(Color.GREEN)
                        self.__E_TOWER_HEALTH_BAR.setPOS(self.__E_TOWER_HEALTH_TEXT.getX() + (self.__E_TOWER_HEALTH_TEXT.getWidth() // 2 - self.__E_TOWER_DAMAGE_BAR.getWidth() // 2),self.__E_TOWER_HEALTH_TEXT.getY() + self.__E_TOWER_HEALTH_TEXT.getHeight())
                    if self.__LIVE_FISH_ATTACKS[i].isLighting():
                        pass
                    else:
                        self.__POP_LATER = False
                        self.__LIVE_FISH_ATTACKS.pop(i)
            except IndexError:
                pass


    def __checkDeath(self):
        for i in range(len(self.__DEPLOYED_FISHES)-1,-1,-1):
            if self.__DEPLOYED_FISHES[i].ifDead() == False:
                if self.__DEPLOYED_FISHES[i].getHealth() <= 0:
                    self.__DEPLOYED_FISHES[i].beginDeathAnimationDuration()  # makes attack duration = 0
                    self.__DEPLOYED_FISHES[i].isDead()
                    self.__DEPLOYED_FISHES[i].deathAnimation()
                    self.__DEPLOYED_FISHES[i].setDeathPOS(self.__DEPLOYED_FISHES[i].getX(), self.__DEPLOYED_FISHES[i].getY(), self.__DEPLOYED_FISHES[i].getWidth(), self.__DEPLOYED_FISHES[i].getHeight())
            if self.__DEPLOYED_FISHES[i].finishedDying(): # if their attack animation has finished
                self.__DEPLOYED_FISHES.pop(i)


        for i in range(len(self.__DEPLOYED_HUMANS)-1,-1,-1):
            if self.__DEPLOYED_HUMANS[i].ifDead() == False:
                if self.__DEPLOYED_HUMANS[i].getHealth() <= 0:
                    self.__DEPLOYED_HUMANS[i].beginDeathAnimationDuration()  # makes attack duration = 0
                    self.__DEPLOYED_HUMANS[i].isDead()
                    self.__DEPLOYED_HUMANS[i].deathAnimation()
                    self.__DEPLOYED_HUMANS[i].setDeathPOS(self.__DEPLOYED_HUMANS[i].getX(), self.__DEPLOYED_HUMANS[i].getY(), self.__DEPLOYED_HUMANS[i].getWidth(), self.__DEPLOYED_HUMANS[i].getHeight())

            if self.__DEPLOYED_HUMANS[i].finishedDying(): # if their attack animation has finished
                self.__DEPLOYED_HUMANS.pop(i)











    # - - - - - - - - - - - - - - - -  - #
    # - - - - - SPAWNING UNITS - - - - - #
    # -  - - - - - - - - - - - - - - - - #

    def __spawnFish(self, KEYPRESSED):
        '''
        checks if they clicked any of the following buttons
        :param KEYPRESSED:
        :return:
        '''
        if self.__WIN == None:
            if self.__FISH_CURRENT_SPAWN_COOLDOWN[0] >= self.__FISH_SPAWN_COOLDOWN[0]:
                if KEYPRESSED[pygame.K_1] == 1:
                    if self.__INCOME >= self.__OCTOPUS_COST:
                        self.__createOctopus()


            if self.__FISH_CURRENT_SPAWN_COOLDOWN[1] >= self.__FISH_SPAWN_COOLDOWN[1]:
                if KEYPRESSED[pygame.K_2] == 1:
                    if self.__INCOME >= self.__EEL_COST:
                        self.__createEel()

            if self.__LEVEL >= 3:
                if self.__FISH_CURRENT_SPAWN_COOLDOWN[2] >= self.__FISH_SPAWN_COOLDOWN[2]:
                    if KEYPRESSED[pygame.K_3] == 1:
                        if self.__INCOME >= self.__SWORDFISH_COST:
                            self.__createSwordfish()


    def __spawnHuman(self):
        '''
        checks if they clicked any of the following buttons
        :return:
        '''
        if self.__WIN == None:
            if self.__CURRENT_LEVEL == 1:
                if self.__HUMAN_CURRENT_SPAWN_COOLDOWN[0] >= self.__HUMAN_SPAWN_COOLDOWN[0]:
                    self.__createHumanSword()

                if self.__HUMAN_CURRENT_SPAWN_COOLDOWN[1] >= self.__HUMAN_SPAWN_COOLDOWN[1]:
                    self.__createHumanWand()

            if self.__CURRENT_LEVEL == 2:
                if self.__HUMAN_CURRENT_SPAWN_COOLDOWN[0] >= self.__HUMAN_SPAWN_COOLDOWN[0]:
                    self.__createHumanSword()

                if self.__HUMAN_CURRENT_SPAWN_COOLDOWN[1] >= self.__HUMAN_SPAWN_COOLDOWN[1]:
                    self.__createHumanWand()

                if self.__HEALTH_SPAWN1 == True:
                    if self.__E_TOWER.getHealth() <= self.__E_MAX_HEALTH * 0.7: # if health of the base reaches 70%
                        self.__createHumanSword() # immediately spanw these
                        self.__createHumanWand() # spawn these
                        self.__HEALTH_SPAWN1 = False # spawn these

                if self.__HEALTH_SPAWN2 == True:
                    if self.__E_TOWER.getHealth() <= self.__E_MAX_HEALTH * 0.3: # if health of the base reaches 70%
                        self.__createHumanSword() # immediately spanw these
                        self.__HEALTH_SPAWN2 = False # spawn these

            if self.__CURRENT_LEVEL == 3:
                if self.__HUMAN_CURRENT_SPAWN_COOLDOWN[0] >= self.__HUMAN_SPAWN_COOLDOWN[0]:
                    self.__createHumanSword()

                if self.__HUMAN_CURRENT_SPAWN_COOLDOWN[1] >= self.__HUMAN_SPAWN_COOLDOWN[1]:
                    self.__createHumanWand()

                if self.__HEALTH_SPAWN1 == True:
                    if self.__E_TOWER.getHealth() <= self.__E_MAX_HEALTH * 0.7:  # if health of the base reaches 70%
                        self.__createHumanSword()  # immediately spanw these
                        self.__createHumanSword()  # immediately spanw these
                        self.__createHumanWand()  # spawn these
                        self.__HEALTH_SPAWN1 = False  # spawn these

                if self.__HEALTH_SPAWN2 == True:
                    if self.__E_TOWER.getHealth() <= self.__E_MAX_HEALTH * 0.3:  # if health of the base reaches 70%
                        self.__createHumanSword()  # immediately spanw these
                        self.__HEALTH_SPAWN2 = False  # spawn these

                if self.__HEALTH_SPAWN3 == True:
                    if self.__E_TOWER.getHealth() <= self.__E_MAX_HEALTH * 0.5:  # if health of the base reaches 70%
                        self.__createHumanSword()  # immediately spawned these
                        self.__createHumanWand()  # spawn these
                        self.__createHumanWand()  # spawn these
                        self.__HEALTH_SPAWN3 = False  # spawn these



            if self.__CURRENT_LEVEL == 4:
                if self.__HUMAN_CURRENT_SPAWN_COOLDOWN[0] >= self.__HUMAN_SPAWN_COOLDOWN[0]:
                    self.__createHumanSword()

                if self.__HUMAN_CURRENT_SPAWN_COOLDOWN[1] >= self.__HUMAN_SPAWN_COOLDOWN[1]:
                    self.__createHumanWand()

                if self.__HEALTH_SPAWN1 == True:
                    if self.__E_TOWER.getHealth() <= self.__E_MAX_HEALTH * 0.7:  # if health of the base reaches 70%
                        self.__createHumanSword()  # immediately spanw these
                        self.__createHumanSword()  # immediately spanw these
                        self.__createHumanWand()  # spawn these
                        self.__HEALTH_SPAWN1 = False  # spawn these

                if self.__HEALTH_SPAWN2 == True:
                    if self.__E_TOWER.getHealth() <= self.__E_MAX_HEALTH * 0.3:  # if health of the base reaches 70%
                        self.__createHumanSword()  # immediately spanw these
                        self.__HEALTH_SPAWN2 = False  # spawn these

                if self.__HEALTH_SPAWN3 == True:
                    if self.__E_TOWER.getHealth() <= self.__E_MAX_HEALTH * 0.7:  # if health of the base reaches 70%
                        self.__createHumanSword()  # immediately spawned these
                        self.__createHumanWand()  # spawn these
                        self.__createHumanWand()  # spawn these
                        self.__HEALTH_SPAWN3 = False  # spawn these

                if self.__HEALTH_SPAWN4 == True:
                    if self.__E_TOWER.getHealth() <= self.__E_MAX_HEALTH * 0.99:  # if health of the base reaches 70%
                        for i in range(4):
                            self.__TIME = time.time()
                            if self.__TIME >= self.__PREVIOUS_TIME + self.__SPAWN_TIME_PASSED:  # self.__TIME_PASSED = 0.10. So when 0.10 seconds pass
                                self.__PREVIOUS_TIME = self.__TIME  # saves its current time, so when another second passes, it will do this again
                                self.__createHumanSword()  # immediately spawned these











    # - - - - - - - - - - - - - - - - - #
    # - - - - - UNIT CREATION - - - - - #
    # - - - - - - - - - - - - - - - - - #

    # Fish
    def __createOctopus(self):


        # OCTOPUS (index 0)
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
        self.__OCTOPUS = MyUnit("media/octopus/oct6attack.png", self.__FISH_SPAWN_LOCATION, self.__FISH_SPEED[0],self.__FISH_MAX_HEALTH[0], self.__FISH_RANGE[0],Attacks("media/sword/sword1death.png", self.__FISH_ATTACK_DAMAGE[0], self.__FISH_RANGE[0], 5, -1), self.__FISH_ATTACK_COOLDOWN[0], -1,self.__OCTIDLE, self.__OCTMOVE, self.__OCTATTACK,self.__OCTDEATH, self.__oct_moving_sprites, 0.7, 0.3)
        self.__OCTOPUS.setScale(3)
        self.__OCTOPUS.flipSprite()
        # RESETS COOLDOWN, SUBRACTS MONEY, AND ADDS IT TO DEPLOYED UNITS
        self.__FISH_CURRENT_SPAWN_COOLDOWN[0] = 0
        self.__INCOME -= self.__OCTOPUS_COST
        self.__DEPLOYED_FISHES.append(self.__OCTOPUS)
        self.__OCTOPUS.setY(375 - self.__OCTOPUS.getHeight())



    def __createEel(self):


        # EEL (index 1)
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
        self.__EEL = MyUnit("media/eel/eel1idle.png", self.__FISH_SPAWN_LOCATION, self.__FISH_SPEED[1],self.__FISH_MAX_HEALTH[1], self.__FISH_RANGE[1],Attacks("media/eelAttackSprite.png", self.__FISH_ATTACK_DAMAGE[1], self.__FISH_RANGE[1], 5, -1, 40, True), self.__FISH_ATTACK_COOLDOWN[1], -1,self.__EELIDLE, self.__EELMOVE, self.__EELATTACK, self.__EELDEATH, self.__eel_moving_sprites, 0.8, 0.3)
        self.__EEL.setScale(3)
        self.__EEL.flipSprite()
        # RESETS COOLDOWN, SUBRACTS MONEY, AND ADDS IT TO DEPLOYED UNITS
        self.__FISH_CURRENT_SPAWN_COOLDOWN[1] = 0
        self.__INCOME -= self.__EEL_COST
        self.__DEPLOYED_FISHES.append(self.__EEL)
        self.__EEL.setY(390 - self.__EEL.getHeight())

    def __createSwordfish(self):


        self.__LIGHTING_ANIMATION = Lighting(-200, -100)
        self.__sword_fish_moving_sprites = pygame.sprite.Group()
        self.__SWORDFISHATTACK = Swordfishattack(700, 20)
        self.__sword_fish_moving_sprites.add(self.__LIGHTING_ANIMATION)

        self.__sword_fish_moving_sprites.add(self.__SWORDFISHATTACK)
        self.__SWORDFISHDEATH = Swordfishdeath(700, 150)
        self.__sword_fish_moving_sprites.add(self.__SWORDFISHDEATH)
        self.__SWORDFISHIDLE = Swordfishidle(700, 300)
        self.__sword_fish_moving_sprites.add(self.__SWORDFISHIDLE)
        self.__SWORDFISHMOVE = Swordfishmove(700, 400)
        self.__sword_fish_moving_sprites.add(self.__SWORDFISHMOVE)
        self.__SWORDFISH = MyUnit("media/swordfish/sfidle1.png", self.__FISH_SPAWN_LOCATION, self.__FISH_SPEED[2],
                              self.__FISH_MAX_HEALTH[2], self.__FISH_RANGE[2],
                              Attacks("media/lightingHitbox.jpg", self.__FISH_ATTACK_DAMAGE[2], self.__FISH_RANGE[2],
                                      0, -1, 40, False, True, self.__LIGHTING_ANIMATION, 1.8),
                              self.__FISH_ATTACK_COOLDOWN[2], -1, self.__SWORDFISHIDLE, self.__SWORDFISHMOVE,
                              self.__SWORDFISHATTACK,
                              self.__SWORDFISHDEATH, self.__sword_fish_moving_sprites, 0.5, 0.4)
        self.__SWORDFISH.setScale(3)

        # RESETS COOLDOWN, SUBRACTS MONEY, AND ADDS IT TO DEPLOYED UNITS
        self.__FISH_CURRENT_SPAWN_COOLDOWN[2] = 0
        self.__SWORDFISH.setY(375 - self.__SWORDFISH.getHeight())
        self.__INCOME -= self.__SWORDFISH_COST
        self.__DEPLOYED_FISHES.append(self.__SWORDFISH)




    # Humans
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
                             self.__SWORDDEATH, self.__human_sword_moving_sprites, 0.7, 0.4)
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
        self.__WAND = MyUnit("media/wand/wand1idle.png", self.__HUMAN_SPAWN_LOCATION, self.__HUMAN_SPEED[1],self.__HUMAN_MAX_HEALTH[1], self.__HUMAN_RANGE[1], Attacks("media/wand/Projectile.png", self.__HUMAN_ATTACK_DAMAGE[1], self.__HUMAN_RANGE[1], 4, 1, 40, True), self.__HUMAN_ATTACK_COOLDOWN[1], 1 , self.__WANDIDLE, self.__WANDMOVE, self.__WANDATTACK, self.__WANDDEATH, self.__human_wand_moving_sprites, 0.8, 0.4)
        self.__WAND.setScale(3)
        # RESETS COOLDOWN, SUBRACTS MONEY, AND ADDS IT TO DEPLOYED UNITS
        self.__HUMAN_CURRENT_SPAWN_COOLDOWN[1] = 0
        self.__WAND.setY(375 - self.__WAND.getHeight())
        self.__DEPLOYED_HUMANS.append(self.__WAND)








    # - - - - - - - - - - - - - - - - - #
    # - - - -UPDATING/REFRESHING- - - - #
    # - - - - - - - - - - - - - - - - - #


    def __updateTimers(self):
        self.__TIME = time.time()
        if self.__TIME >= self.__PREVIOUS_TIME + self.__TIME_PASSED: # self.__TIME_PASSED = 0.10. So when 0.10 seconds pass
            self.__PREVIOUS_TIME = self.__TIME  # saves its current time, so when another second passes, it will do this again

            # updates the cooldowns
            for i in range(len(self.__FISH_CURRENT_SPAWN_COOLDOWN)):  # for every unique fish
                self.__FISH_CURRENT_SPAWN_COOLDOWN[i] += self.__TIME_PASSED  # updates the cooldown timers by the time passed

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

            for ATTACK in self.__LIVE_FISH_ATTACKS:
                if ATTACK.isLighting():
                    ATTACK.updateAttackAnimationDuration(self.__TIME_PASSED)

            # Visual cooldownTimers
            if self.__FISH_CURRENT_SPAWN_COOLDOWN[0] <= self.__FISH_SPAWN_COOLDOWN[0]:
                self.__CHARACTER1_CD_TEXT.setText(
                    f"{round(self.__FISH_SPAWN_COOLDOWN[0] - self.__FISH_CURRENT_SPAWN_COOLDOWN[0], 1)}")
            else:
                self.__CHARACTER1_CD_TEXT.setText(f"Ready", Color.GREEN)
            self.__CHARACTER1_CD_TEXT.setPOS(
                self.__OUTLINE1.getX() + (self.__OUTLINE1.getWidth() // 2 - self.__CHARACTER1_CD_TEXT.getWidth() // 2),
                self.__OUTLINE1.getY() + (
                            self.__OUTLINE1.getHeight() // 2 - self.__CHARACTER1_CD_TEXT.getHeight() // 2) + 26)

            if self.__FISH_CURRENT_SPAWN_COOLDOWN[1] <= self.__FISH_SPAWN_COOLDOWN[1]:
                self.__CHARACTER2_CD_TEXT.setText(
                    f"{round(self.__FISH_SPAWN_COOLDOWN[1] - self.__FISH_CURRENT_SPAWN_COOLDOWN[1], 1)}")
            else:
                self.__CHARACTER2_CD_TEXT.setText(f"Ready", Color.GREEN)
            self.__CHARACTER2_CD_TEXT.setPOS(
                self.__OUTLINE2.getX() + (self.__OUTLINE2.getWidth() // 2 - self.__CHARACTER2_CD_TEXT.getWidth() // 2),
                self.__OUTLINE2.getY() + (
                            self.__OUTLINE2.getHeight() // 2 - self.__CHARACTER2_CD_TEXT.getHeight() // 2) + 26)
            if self.__LEVEL <= 2:
                self.__CHARACTER3_CD_TEXT.setText(
                    f"")
            else:
                if self.__FISH_CURRENT_SPAWN_COOLDOWN[2] <= self.__FISH_SPAWN_COOLDOWN[2]:
                    self.__CHARACTER3_CD_TEXT.setText(
                        f"{round(self.__FISH_SPAWN_COOLDOWN[2] - self.__FISH_CURRENT_SPAWN_COOLDOWN[2], 1)}")
                else:
                    self.__CHARACTER3_CD_TEXT.setText(f"Ready", Color.GREEN)

                    self.__CHARACTER3_CD_TEXT.setPOS(
                        self.__OUTLINE3.getX() + (self.__OUTLINE3.getWidth() // 2 - self.__CHARACTER3_CD_TEXT.getWidth() // 2),
                        self.__OUTLINE3.getY() + (
                                    self.__OUTLINE3.getHeight() // 2 - self.__CHARACTER3_CD_TEXT.getHeight() // 2) + 26)





    def __updateWindowFrame(self):
        self.__WINDOW.clearScreen()
        self.__WINDOW.getSurface().blit(self.__BACKGROUND.getSurface(), self.__BACKGROUND.getPOS())
        self.__WINDOW.getSurface().blit(self.__INCOME_TEXT.getSurface(), self.__INCOME_TEXT.getPOS())



        for OBJECTS in self.__VISUAL_TIMERS:
            self.__WINDOW.getSurface().blit(OBJECTS.getSurface(), OBJECTS.getPOS())


        for TOWER in self.__TOWERS:
            self.__WINDOW.getSurface().blit(TOWER.getSurface(), TOWER.getPOS())

        self.__WINDOW.getSurface().blit(self.__E_TOWER_HEALTH_TEXT.getSurface(), self.__E_TOWER_HEALTH_TEXT.getPOS())
        self.__WINDOW.getSurface().blit(self.__E_TOWER_DAMAGE_BAR.getSurface(), self.__E_TOWER_DAMAGE_BAR.getPOS())
        self.__WINDOW.getSurface().blit(self.__E_TOWER_HEALTH_BAR.getSurface(), self.__E_TOWER_HEALTH_BAR.getPOS())

        self.__WINDOW.getSurface().blit(self.__A_TOWER_HEALTH_TEXT.getSurface(), self.__A_TOWER_HEALTH_TEXT.getPOS())
        self.__WINDOW.getSurface().blit(self.__A_TOWER_DAMAGE_BAR.getSurface(), self.__A_TOWER_DAMAGE_BAR.getPOS())
        self.__WINDOW.getSurface().blit(self.__A_TOWER_HEALTH_BAR.getSurface(), self.__A_TOWER_HEALTH_BAR.getPOS())

        for HUMAN in self.__DEPLOYED_HUMANS:
            HUMAN.getGroupAnimation().draw(self.__WINDOW.getSurface())
            HUMAN.updateGroupAnimation()

        for FISH in self.__DEPLOYED_FISHES:
            FISH.getGroupAnimation().draw(self.__WINDOW.getSurface())
            FISH.updateGroupAnimation()

        for ATTACK in self.__LIVE_FISH_ATTACKS:
            if ATTACK.isProjectile():
                self.__WINDOW.getSurface().blit(ATTACK.getSurface(), ATTACK.getPOS())

        for ATTACK in self.__LIVE_HUMAN_ATTACKS:
            if ATTACK.isProjectile():
                self.__WINDOW.getSurface().blit(ATTACK.getSurface(), ATTACK.getPOS())
            if ATTACK.isLighting():
                ATTACK.getAnimation().draw(self.__WINDOW.getSurface())
                ATTACK.update()


        if self.__LEVEL <= 2:
            self.__WINDOW.getSurface().blit(self.__swordFishLock.getSurface(), self.__swordFishLock.getPOS())

        if self.__WIN != None:
            for i in range(len(self.__END_SCREEN)):
                self.__WINDOW.getSurface().blit(self.__END_SCREEN[i].getSurface(), self.__END_SCREEN[i].getPOS())



        self.__WINDOW.updateFrame()

    def __applyVisuals(self):
        # - - - - - - - - - - - - - - - - - - #
        #    -  -  - VISUAL TIMERS  -  -  -   #
        # - - - - - - - - - - - - - - - - - - #

        self.__VISUAL_TIMERS = []
        self.__OUTLINE1 = ImageSprite("media/outline.png")
        self.__OUTLINE1.setScale(1 / 6)
        self.__OUTLINE1.setY(5)
        self.__OUTLINE1.setX(5)
        self.__OUTLINE2 = ImageSprite("media/outline.png")
        self.__OUTLINE2.setScale(1 / 6)
        self.__OUTLINE2.setX(self.__OUTLINE1.getX() + self.__OUTLINE1.getWidth() + 10)
        self.__OUTLINE2.setY(5)
        self.__OUTLINE3 = ImageSprite("media/outline.png")
        self.__OUTLINE3.setScale(1 / 6)
        self.__OUTLINE3.setX(self.__OUTLINE2.getX() + self.__OUTLINE2.getWidth() + 10)
        self.__OUTLINE3.setY(5)
        self.__NUM1 = Text("1", "TimesNewRoman", 15)
        self.__NUM1.setPOS(self.__OUTLINE1.getX() + 8, self.__OUTLINE1.getY() + 5)
        self.__NUM2 = Text("2", "ComicSans", 15)
        self.__NUM2.setPOS(self.__OUTLINE2.getX() + 8, self.__OUTLINE2.getY() + 5)
        self.__NUM3 = Text("3", "ComicSans", 15)
        self.__NUM3.setPOS(self.__OUTLINE3.getX() + 8, self.__OUTLINE3.getY() + 5)

        self.__CHARACTER1 = ImageSprite("media/octopus/oct1idle.png")  # FISH THING
        self.__CHARACTER1.flipSprite()
        self.__CHARACTER1.setPOS(
            self.__OUTLINE1.getX() + (self.__OUTLINE1.getWidth() // 2 - self.__CHARACTER1.getWidth() // 2),
            self.__OUTLINE1.getY() + (self.__OUTLINE1.getHeight() // 2 - self.__CHARACTER1.getHeight() // 2))
        self.__CHARACTER1_CD_TEXT = Text(f"{self.__FISH_SPAWN_COOLDOWN[0] - self.__FISH_CURRENT_SPAWN_COOLDOWN[0]}",
                                         "ComicSans", 18)
        self.__CHARACTER1_CD_TEXT.setPOS(
            self.__OUTLINE1.getX() + (self.__OUTLINE1.getWidth() // 2 - self.__CHARACTER1_CD_TEXT.getWidth() // 2),
            self.__OUTLINE1.getY() + (
                        self.__OUTLINE1.getHeight() // 2 - self.__CHARACTER1_CD_TEXT.getHeight() // 2) + 27)

        self.__CHARACTER1_COST_TEXT = Text(f"${self.__OCTOPUS_COST}", "ComicSans", 12)
        self.__CHARACTER1_COST_TEXT.setPOS(
            self.__OUTLINE1.getX() + (self.__OUTLINE1.getWidth() - (self.__CHARACTER1_COST_TEXT.getWidth() + 10)),
            self.__OUTLINE1.getY() + 5)

        self.__CHARACTER2 = ImageSprite("media/eel/eel1idle.png")  # EEL
        self.__CHARACTER2.flipSprite()
        self.__CHARACTER2.setPOS(
            self.__OUTLINE2.getX() + (self.__OUTLINE2.getWidth() // 2 - self.__CHARACTER2.getWidth() // 2),
            self.__OUTLINE2.getY() + (self.__OUTLINE2.getHeight() // 2 - self.__CHARACTER2.getHeight() // 2))
        self.__CHARACTER2_CD_TEXT = Text(f"{self.__FISH_SPAWN_COOLDOWN[1] - self.__FISH_CURRENT_SPAWN_COOLDOWN[1]}",
                                         "ComicSans", 18)
        self.__CHARACTER2_CD_TEXT.setPOS(
            self.__OUTLINE2.getX() + (self.__OUTLINE2.getWidth() - self.__CHARACTER2_CD_TEXT.getWidth() // 2),
            self.__OUTLINE2.getY() + (
                        self.__OUTLINE2.getHeight() // 2 - self.__CHARACTER2_CD_TEXT.getHeight() // 2) + 27)
        self.__CHARACTER2_COST_TEXT = Text(f"${self.__EEL_COST}", "ComicSans", 12)
        self.__CHARACTER2_COST_TEXT.setPOS(
            self.__OUTLINE2.getX() + (self.__OUTLINE2.getWidth() - (self.__CHARACTER2_COST_TEXT.getWidth() + 10)),
            self.__OUTLINE2.getY() + 5)

        self.__CHARACTER3 = ImageSprite("media/swordfish/sfidle1.png")  # OCTOPUS
        self.__CHARACTER3.flipSprite()
        self.__CHARACTER3.setPOS(
            self.__OUTLINE3.getX() + (self.__OUTLINE3.getWidth() // 2 - self.__CHARACTER3.getWidth() // 2),
            self.__OUTLINE3.getY() + (self.__OUTLINE3.getHeight() // 2 - self.__CHARACTER3.getHeight() // 2))
        self.__CHARACTER3_CD_TEXT = Text(f"{self.__FISH_SPAWN_COOLDOWN[2] - self.__FISH_CURRENT_SPAWN_COOLDOWN[2]}",
                                         "ComicSans", 18)
        self.__CHARACTER3_CD_TEXT.setPOS(
            self.__OUTLINE3.getX() + (self.__OUTLINE3.getWidth() // 2 - self.__CHARACTER3_CD_TEXT.getWidth() // 2),
            self.__OUTLINE3.getY() + (
                        self.__OUTLINE3.getHeight() // 2 - self.__CHARACTER3_CD_TEXT.getHeight() // 2) + 27)
        self.__CHARACTER3_COST_TEXT = Text(f"${self.__SWORDFISH_COST}", "ComicSans", 12)
        self.__CHARACTER3_COST_TEXT.setPOS(
            self.__OUTLINE3.getX() + (self.__OUTLINE3.getWidth() - (self.__CHARACTER3_COST_TEXT.getWidth() + 10)),
            self.__OUTLINE3.getY() + 5)

        self.__VISUAL_TIMERS.append(self.__OUTLINE1)
        self.__VISUAL_TIMERS.append(self.__NUM1)
        self.__VISUAL_TIMERS.append(self.__OUTLINE2)
        self.__VISUAL_TIMERS.append(self.__NUM2)
        self.__VISUAL_TIMERS.append(self.__OUTLINE3)
        self.__VISUAL_TIMERS.append(self.__NUM3)
        self.__VISUAL_TIMERS.append(self.__CHARACTER1)
        self.__VISUAL_TIMERS.append(self.__CHARACTER2)
        self.__VISUAL_TIMERS.append(self.__CHARACTER3)
        self.__VISUAL_TIMERS.append(self.__CHARACTER1_CD_TEXT)
        self.__VISUAL_TIMERS.append(self.__CHARACTER2_CD_TEXT)
        self.__VISUAL_TIMERS.append(self.__CHARACTER3_CD_TEXT)
        self.__VISUAL_TIMERS.append(self.__CHARACTER1_COST_TEXT)
        self.__VISUAL_TIMERS.append(self.__CHARACTER2_COST_TEXT)
        self.__VISUAL_TIMERS.append(self.__CHARACTER3_COST_TEXT)

        self.__DEFEAT_TEXT = ImageSprite("media/defeat.png")
        self.__DEFEAT_TEXT.setSpeed(4)
        self.__DEFEAT_TEXT.setScale(1)
        self.__DEFEAT_TEXT.setPOS(self.__WINDOW.getWidth() // 2 - self.__DEFEAT_TEXT.getWidth() // 2,
                                    0 - self.__DEFEAT_TEXT.getHeight())

        self.__VICTORY_TEXT = ImageSprite("media/victory.png")
        self.__VICTORY_TEXT.setScale(1)
        self.__VICTORY_TEXT.setSpeed(4)
        self.__VICTORY_TEXT.setPOS(self.__WINDOW.getWidth() // 2 - self.__VICTORY_TEXT.getWidth() // 2,0 - self.__VICTORY_TEXT.getHeight())

        self.__RETURNING_TEXT = ImageSprite("media/menu/Press-Space-To-Return-1-12-2024.png")
        self.__RETURNING_TEXT.setScale(0.4)
        self.__RETURNING_TEXT.setPOS(self.__WINDOW.getWidth()//2 - self.__RETURNING_TEXT.getWidth()//2, self.__WINDOW.getHeight()+30)

        self.__swordFishLock = ImageSprite("media/menu/levelsBorderLock.png")
        self.__swordFishLock.setScale(0.2)
        self.__swordFishLock.setPOS(
            self.__OUTLINE3.getX() + (self.__OUTLINE3.getWidth() // 2 - self.__swordFishLock.getWidth() // 2),
            self.__OUTLINE3.getY() + (self.__OUTLINE3.getHeight() // 2 - self.__swordFishLock.getHeight() // 2))


    def __menu(self):
        self.__SECOND_SCREEN = []
        self.__SECOND_SCREEN.append(self.__TITLE_TEXT)
        self.__HTP_TEXT = ImageSprite("media/menu/howToPlay1.1.png")
        self.__HTP_TEXT.setScale(0.9)
        self.__HTP_TEXT.setPOS(self.__WINDOW.getWidth() // 2 - self.__HTP_TEXT.getWidth() // 2, 105)
        self.__SECOND_SCREEN.append(self.__HTP_TEXT)
        self.__HTP_TEXT = ImageSprite("media/menu/howToPlay1.2.png")
        self.__HTP_TEXT.setScale(0.9)
        self.__HTP_TEXT.setPOS(self.__WINDOW.getWidth() // 2 - self.__HTP_TEXT.getWidth() // 2, 150)
        self.__SECOND_SCREEN.append(self.__HTP_TEXT)
        self.__HTP_TEXT = ImageSprite("media/menu/howToPlay1.3.png")
        self.__HTP_TEXT.setScale(0.7)
        self.__HTP_TEXT.setPOS(self.__WINDOW.getWidth() // 2 - self.__HTP_TEXT.getWidth() // 2, 210)
        self.__SECOND_SCREEN.append(self.__HTP_TEXT)
        self.__HTP_TEXT = ImageSprite("media/menu/howToPlay2.png")
        self.__HTP_TEXT.setScale(0.9)
        self.__HTP_TEXT.setPOS(self.__WINDOW.getWidth() // 2 - self.__HTP_TEXT.getWidth() // 2, 250)
        self.__SECOND_SCREEN.append(self.__HTP_TEXT)
        self.__HTP_TEXT = ImageSprite("media/menu/continue.png")
        self.__HTP_TEXT.setScale(0.2)
        self.__HTP_TEXT.setPOS(self.__WINDOW.getWidth() - self.__HTP_TEXT.getWidth(), self.__WINDOW.getHeight()-self.__HTP_TEXT.getHeight())
        self.__SECOND_SCREEN.append(self.__HTP_TEXT)


        # Title
        self.__THIRD_SCREEN = []
        self.__LEVELS_TEXT = ImageSprite("media/menu/levelsTitle.png")
        self.__LEVELS_TEXT.setScale(0.26)
        self.__LEVELS_TEXT.setPOS(self.__WINDOW.getWidth() // 2 - self.__LEVELS_TEXT.getWidth() // 2, 5)
        self.__THIRD_SCREEN.append(self.__LEVELS_TEXT)

        # Things
        self.__SELECT_TEXT = ImageSprite("media/menu/1-1-7-2024.png")
        self.__SELECT_TEXT.setScale(0.1)
        self.__SELECT_TEXT.setPOS(246.6, self.__WINDOW.getHeight() // 2 - self.__SELECT_TEXT.getHeight() // 2)

        self.__OUTLINE = ImageSprite("media/menu/numbersBorder.png")
        self.__OUTLINE.setScale(0.3)
        self.__OUTLINE.setPOS(self.__SELECT_TEXT.getX()+(self.__SELECT_TEXT.getWidth()//2 - self.__OUTLINE.getWidth()//2),
                              self.__SELECT_TEXT.getY()+(self.__SELECT_TEXT.getHeight()//2 - self.__OUTLINE.getHeight()//2))

        self.__THIRD_SCREEN.append(self.__OUTLINE)
        self.__THIRD_SCREEN.append(self.__SELECT_TEXT)


        self.__SELECT_TEXT = ImageSprite("media/menu/2-1-7-2024.png")
        self.__SELECT_TEXT.setScale(0.1)
        self.__SELECT_TEXT.setPOS(246.6*2, self.__WINDOW.getHeight() // 2 - self.__SELECT_TEXT.getHeight() // 2)

        self.__OUTLINE = ImageSprite("media/menu/numbersBorder.png")
        self.__OUTLINE.setScale(0.3)
        self.__OUTLINE.setPOS(
            self.__SELECT_TEXT.getX() + (self.__SELECT_TEXT.getWidth() // 2 - self.__OUTLINE.getWidth() // 2) ,
            self.__SELECT_TEXT.getY() + (self.__SELECT_TEXT.getHeight() // 2 - self.__OUTLINE.getHeight() // 2))
        self.__LOCK2 = ImageSprite("media/menu/levelsBorderLock.png")
        self.__LOCK2.setScale(0.3)
        self.__LOCK2.setPOS(
            self.__SELECT_TEXT.getX() + (self.__SELECT_TEXT.getWidth() // 2 - self.__OUTLINE.getWidth() // 2),
            self.__SELECT_TEXT.getY() + (self.__SELECT_TEXT.getHeight() // 2 - self.__OUTLINE.getHeight() // 2))

        self.__THIRD_SCREEN.append(self.__OUTLINE)
        self.__THIRD_SCREEN.append(self.__SELECT_TEXT)


        self.__SELECT_TEXT = ImageSprite("media/menu/3-1-7-2024.png")
        self.__SELECT_TEXT.setScale(0.1)
        self.__SELECT_TEXT.setPOS(246.6*3, self.__WINDOW.getHeight() // 2 - self.__SELECT_TEXT.getHeight() // 2)

        self.__OUTLINE = ImageSprite("media/menu/numbersBorder.png")
        self.__OUTLINE.setScale(0.3)
        self.__OUTLINE.setPOS(
            self.__SELECT_TEXT.getX() + (self.__SELECT_TEXT.getWidth() // 2 - self.__OUTLINE.getWidth() // 2) ,
            self.__SELECT_TEXT.getY() + (self.__SELECT_TEXT.getHeight() // 2 - self.__OUTLINE.getHeight() // 2))
        self.__LOCK3 = ImageSprite("media/menu/levelsBorderLock.png")
        self.__LOCK3.setScale(0.3)
        self.__LOCK3.setPOS(
            self.__SELECT_TEXT.getX() + (self.__SELECT_TEXT.getWidth() // 2 - self.__OUTLINE.getWidth() // 2),
            self.__SELECT_TEXT.getY() + (self.__SELECT_TEXT.getHeight() // 2 - self.__OUTLINE.getHeight() // 2))

        self.__THIRD_SCREEN.append(self.__OUTLINE)
        self.__THIRD_SCREEN.append(self.__SELECT_TEXT)


        self.__SELECT_TEXT = ImageSprite("media/menu/4-1-7-2024.png")
        self.__SELECT_TEXT.setScale(0.1)
        self.__SELECT_TEXT.setPOS(246.6*4, self.__WINDOW.getHeight() // 2 - self.__SELECT_TEXT.getHeight() // 2)
        self.__OUTLINE = ImageSprite("media/menu/numbersBorder.png")
        self.__OUTLINE.setScale(0.3)
        self.__OUTLINE.setPOS(self.__SELECT_TEXT.getX() + (self.__SELECT_TEXT.getWidth() // 2 - self.__OUTLINE.getWidth() // 2),
                              self.__SELECT_TEXT.getY() + (self.__SELECT_TEXT.getHeight() // 2 - self.__OUTLINE.getHeight() // 2))
        self.__LOCK4 = ImageSprite("media/menu/levelsBorderLock.png")
        self.__LOCK4.setScale(0.3)
        self.__LOCK4.setPOS(
            self.__SELECT_TEXT.getX() + (self.__SELECT_TEXT.getWidth() // 2 - self.__OUTLINE.getWidth() // 2),
            self.__SELECT_TEXT.getY() + (self.__SELECT_TEXT.getHeight() // 2 - self.__OUTLINE.getHeight() // 2))

        self.__THIRD_SCREEN.append(self.__OUTLINE)
        self.__THIRD_SCREEN.append(self.__SELECT_TEXT)

        # Skill point bar
        self.__SELECT_TEXT = ImageSprite("media/menu/skillPointsText.png")
        self.__SELECT_TEXT.setScale(0.3)
        self.__SELECT_TEXT.setPOS(self.__WINDOW.getWidth() // 2 - self.__SELECT_TEXT.getWidth() // 2, self.__WINDOW.getHeight()-self.__SELECT_TEXT.getHeight()-15)
        self.__OUTLINE = ImageSprite("media/menu/skillPointsBorder.png")
        self.__OUTLINE.setScale(0.4)
        self.__OUTLINE.setPOS(
            self.__SELECT_TEXT.getX() + (self.__SELECT_TEXT.getWidth() // 2 - self.__OUTLINE.getWidth() // 2),
            self.__SELECT_TEXT.getY() + (self.__SELECT_TEXT.getHeight() // 2 - self.__OUTLINE.getHeight() // 2))
        self.__THIRD_SCREEN.append(self.__OUTLINE)
        self.__THIRD_SCREEN.append(self.__SELECT_TEXT)

        self.__FOURTH_SCREEN = []
        self.__SELECT_TEXT = ImageSprite("media/menu/Increase-Damage-x-1-3-1-1-12-2024.png")
        self.__SELECT_TEXT.setScale(0.35)
        self.__SELECT_TEXT.setPOS(50, 150)
        self.__OUTLINE = ImageSprite("media/menu/skillPointsBorder.png")
        self.__OUTLINE.setScale(0.35)
        self.__OUTLINE.setPOS(
            self.__SELECT_TEXT.getX() + (self.__SELECT_TEXT.getWidth() // 2 - self.__OUTLINE.getWidth() // 2),
            self.__SELECT_TEXT.getY() + (self.__SELECT_TEXT.getHeight() // 2 - self.__OUTLINE.getHeight() // 2))
        self.__FOURTH_SCREEN.append(self.__OUTLINE)
        self.__FOURTH_SCREEN.append(self.__SELECT_TEXT)


        self.__SELECT_TEXT = ImageSprite("media/menu/Increase-Health-x-1-3-2-1-13-2024.png")
        self.__SELECT_TEXT.setScale(0.35)
        self.__SELECT_TEXT.setPOS(self.__WINDOW.getWidth() // 2 - self.__SELECT_TEXT.getWidth() // 2, 150)
        self.__OUTLINE = ImageSprite("media/menu/skillPointsBorder.png")
        self.__OUTLINE.setScale(0.35)
        self.__OUTLINE.setPOS(
            self.__SELECT_TEXT.getX() + (self.__SELECT_TEXT.getWidth() // 2 - self.__OUTLINE.getWidth() // 2),
            self.__SELECT_TEXT.getY() + (self.__SELECT_TEXT.getHeight() // 2 - self.__OUTLINE.getHeight() // 2))
        self.__FOURTH_SCREEN.append(self.__OUTLINE)
        self.__FOURTH_SCREEN.append(self.__SELECT_TEXT)


        self.__SELECT_TEXT = ImageSprite("media/menu/Income-Generation-x-1-3-3-1-12-2024.png")
        self.__SELECT_TEXT.setScale(0.35)
        self.__SELECT_TEXT.setPOS(self.__WINDOW.getWidth()- (self.__SELECT_TEXT.getWidth() +50),150)
        self.__OUTLINE = ImageSprite("media/menu/skillPointsBorder.png")
        self.__OUTLINE.setScale(0.35)
        self.__OUTLINE.setPOS(
            self.__SELECT_TEXT.getX() + (self.__SELECT_TEXT.getWidth() // 2 - self.__OUTLINE.getWidth() // 2),
            self.__SELECT_TEXT.getY() + (self.__SELECT_TEXT.getHeight() // 2 - self.__OUTLINE.getHeight() // 2))
        self.__FOURTH_SCREEN.append(self.__OUTLINE)
        self.__FOURTH_SCREEN.append(self.__SELECT_TEXT)

        self.__SELECT_TEXT = ImageSprite("media/menu/Income-Generation-x-1-3-3-1-12-2024.png")
        self.__SELECT_TEXT.setScale(0.35)
        self.__SELECT_TEXT.setPOS(self.__WINDOW.getWidth() - (self.__SELECT_TEXT.getWidth() + 50), 150)
        self.__OUTLINE = ImageSprite("media/menu/skillPointsBorder.png")
        self.__OUTLINE.setScale(0.35)
        self.__OUTLINE.setPOS(
            self.__SELECT_TEXT.getX() + (self.__SELECT_TEXT.getWidth() // 2 - self.__OUTLINE.getWidth() // 2),
            self.__SELECT_TEXT.getY() + (self.__SELECT_TEXT.getHeight() // 2 - self.__OUTLINE.getHeight() // 2))
        self.__FOURTH_SCREEN.append(self.__OUTLINE)
        self.__FOURTH_SCREEN.append(self.__SELECT_TEXT)

        self.__SELECT_TEXT = ImageSprite("media/menu/Remaining-Skillpoints-1-13-2024.png")
        self.__SELECT_TEXT.setScale(0.30)
        self.__SELECT_TEXT.setPOS(self.__WINDOW.getWidth() - (self.__SELECT_TEXT.getWidth() + 65), 15)
        self.__OUTLINE = ImageSprite("media/menu/skillPointsBorder.png")
        self.__OUTLINE.setScale(0.35)
        self.__OUTLINE.setPOS(
            self.__SELECT_TEXT.getX() + (self.__SELECT_TEXT.getWidth() // 2 - self.__OUTLINE.getWidth() // 2 + 30),
            self.__SELECT_TEXT.getY() + (self.__SELECT_TEXT.getHeight() // 2 - self.__OUTLINE.getHeight() // 2))
        self.__FOURTH_SCREEN.append(self.__OUTLINE)
        self.__FOURTH_SCREEN.append(self.__SELECT_TEXT)

        self.__SKILLPOINTS_TEXT = Text(f"{self.__SKILLPOINTS}", "Cosmic Sans", 42)
        self.__SKILLPOINTS_TEXT.setPOS(1175, 33)
        self.__FOURTH_SCREEN.append(self.__SKILLPOINTS_TEXT)

        self.__SELECT_TEXT = ImageSprite("media/menu/Beating-a-new-Level-grants-yo-1-13-2024.png")
        self.__SELECT_TEXT.setScale(0.47)
        self.__SELECT_TEXT.setPOS(0, -10)
        self.__FOURTH_SCREEN.append(self.__SELECT_TEXT)

        self.__SELECT_TEXT = ImageSprite("media/menu/Return-to-Levels-r-1-13-2024.png")
        self.__SELECT_TEXT.setScale(0.40)
        self.__SELECT_TEXT.setPOS(self.__WINDOW.getWidth()//2 - self.__SELECT_TEXT.getWidth()//2, self.__WINDOW.getHeight() - self.__SELECT_TEXT.getHeight() - 30)
        self.__FOURTH_SCREEN.append(self.__SELECT_TEXT)

        if self.__LEVEL == 1:
            self.__THIRD_SCREEN.append(self.__LOCK2)
            self.__THIRD_SCREEN.append(self.__LOCK3)
            self.__THIRD_SCREEN.append(self.__LOCK4)

        if self.__LEVEL == 2:
            self.__LOCK2.setPOS(-1000,-1000)
            self.__THIRD_SCREEN.append(self.__LOCK3)
            self.__THIRD_SCREEN.append(self.__LOCK4)

        if self.__LEVEL == 3:
            self.__LOCK2.setPOS(-1000,-1000)
            self.__LOCK3.setPOS(-1000, -1000)
            self.__THIRD_SCREEN.append(self.__LOCK4)

        if self.__LEVEL == 4:
            pass



        KEY_PRESSED = pygame.key.get_pressed()
        # Opening Menu
        # If its from the starting menu
        if self.__CURRENT_SCREEN == 0:
            if KEY_PRESSED[pygame.K_e] == 1:
                self.__DISPLAY = self.__SECOND_SCREEN # Go to insturction menu
                self.__CURRENT_SCREEN = 1
                self.__LEVEL_SELECTOR = False

        # Explanation Menu
        if self.__CURRENT_SCREEN == 1: # If in instruction menu
            if KEY_PRESSED[pygame.K_c] == 1 or self.__CURRENT_LEVEL != 0: # and they click c
                self.__DISPLAY = self.__THIRD_SCREEN # go to level selector
                self.__LEVEL_SELECTOR = True




        # LEVEL SELECTING
        if self.__LEVEL_SELECTOR == True and self.__SKILLPOINTS_SELECTOR == False:
            self.__DISPLAY = self.__THIRD_SCREEN  # go to level selector
            if KEY_PRESSED[pygame.K_1]:
                self.__PLAYING = True
                # E_SCALING = [TOWER HEALTH, % Damage Increase, % Health Increase]
                self.__levelPreperation([800, 1, 1])
                self.__CURRENT_LEVEL = 1

            if self.__LEVEL >= 2:
                if KEY_PRESSED[pygame.K_2]:
                    self.__PLAYING = True
                    # E_SCALING = [TOWER HEALTH, % Damage Increase, % Health Increase]
                    self.__levelPreperation([1300, 1.4, 1.15])
                    self.__CURRENT_LEVEL = 2

            if self.__LEVEL >= 3:
                if KEY_PRESSED[pygame.K_3]:
                    self.__PLAYING = True
                    # E_SCALING = [TOWER HEALTH, % Damage Increase, % Health Increase]
                    self.__levelPreperation([10000, 1.5, 1.3])
                    self.__CURRENT_LEVEL = 3

            if self.__LEVEL >= 4:
                if KEY_PRESSED[pygame.K_4]:
                    self.__PLAYING = True
                    # E_SCALING = [TOWER HEALTH, % Damage Increase, % Health Increase]
                    self.__levelPreperation([10000, 1.7, 1.5])
                    self.__CURRENT_LEVEL = 4

            if KEY_PRESSED[pygame.K_s] == 1:
                self.__LEVEL_SELECTOR = False
                self.__SKILLPOINTS_SELECTOR = True


        if self.__SKILLPOINTS_SELECTOR == True:
            self.__DISPLAY = self.__FOURTH_SCREEN
            self.__TIME = time.time()
            if self.__TIME >= self.__PREVIOUS_TIME + self.__SP_TIME_PASSED:  # self.__TIME_PASSED = 0.10. So when 0.10 seconds pass
                if self.__SKILLPOINTS > 0:
                    if KEY_PRESSED[pygame.K_1] == 1:
                        self.__DAMAGE_MULTIPLIER += 0.3
                        self.__SKILLPOINTS -= 1
                        self.__PREVIOUS_TIME = self.__TIME  # saves its current
                if self.__SKILLPOINTS > 0:
                    if KEY_PRESSED[pygame.K_2] == 1:
                        self.__HEALTH_MULTIPLIER += 0.3
                        self.__SKILLPOINTS -= 1
                        self.__PREVIOUS_TIME = self.__TIME  # saves its current
                if self.__SKILLPOINTS > 0:
                    if KEY_PRESSED[pygame.K_3] == 1:
                        self.__INCOME_MULTIPLIER += 0.3
                        self.__SKILLPOINTS -= 1
                        self.__PREVIOUS_TIME = self.__TIME  # saves its current

            if KEY_PRESSED[pygame.K_r] == 1:
                self.__SKILLPOINTS_SELECTOR = False
                self.__LEVEL_SELECTOR = True




        # - - - UPDATES THE SCREEN - - - #

        self.__WINDOW.clearScreen()
        self.__WINDOW.getSurface().blit(self.__MENU_BACKGROUND.getSurface(), self.__MENU_BACKGROUND.getPOS())



        for i in range(len(self.__DISPLAY)):
            self.__WINDOW.getSurface().blit(self.__DISPLAY[i].getSurface(), self.__DISPLAY[i].getPOS())



        self.__WINDOW.updateFrame()

    def __endScreen(self):
        if self.__WIN == None:
            if self.__A_TOWER.getHealth() <= 0:
                self.__WIN = False
                self.__END_SCREEN = []
                self.__END_SCREEN.append(self.__DEFEAT_TEXT)

            if self.__E_TOWER.getHealth() <= 0:
                self.__WIN = True
                self.__END_SCREEN = []
                self.__END_SCREEN.append(self.__VICTORY_TEXT)
                if self.__LEVEL == 1 and self.__CURRENT_LEVEL == 1:
                    self.__LEVEL = 2
                    self.__SKILLPOINTS += 2

                if self.__LEVEL == 2 and self.__CURRENT_LEVEL == 2:
                    self.__LEVEL = 3
                    self.__SKILLPOINTS += 2

                if self.__LEVEL == 3 and self.__CURRENT_LEVEL == 3:
                    self.__LEVEL = 4
                    self.__SKILLPOINTS += 2


        if self.__WIN != None:
            self.__END_SCREEN[0].marqueeY(0)
            if self.__END_SCREEN[0].getY() >= 2:
                self.__END_SCREEN.append(self.__RETURNING_TEXT)
                self.__END_SCREEN[-1].setY(self.__WINDOW.getHeight()-self.__RETURNING_TEXT.getHeight() -20)
                KEYPRESSED = pygame.key.get_pressed()
                if KEYPRESSED[pygame.K_SPACE] == 1:
                    self.__LEVEL_SELECTOR = True
                    self.__PLAYING = False
                    self.__CURRENT_SCREEN = 1






    def __levelPreperation(self, E_SCALING):

        # - - - - - - - - - - - - - - - - - - - - #
        #   -  -  - FISH CONFIGURATIONS -  -  -   #
        # - - - - - - - - - - - - - - - - - - - - #

        self.__INCOME = 0
        self.__TOWERS = []

        self.__A_MAX_HEALTH = 2000
        # Ally Tower
        self.__A_TOWER = MyUnit("media/allybase11.png", None, None, self.__A_MAX_HEALTH, None, None, None, None, None,
                                None, None, None, None, None)
        self.__A_TOWER.setScale(0.80)
        self.__A_TOWER.setY(90)
        self.__A_TOWER.setX(1015)
        self.__TOWERS.append(self.__A_TOWER)

        self.__A_TOWER_HEALTH_TEXT = Text(f"{self.__A_MAX_HEALTH}", "ComicSans", 18)
        self.__A_TOWER_HEALTH_TEXT.setPOS(
            self.__A_TOWER.getX() + (self.__A_TOWER.getWidth() // 2 - self.__A_TOWER_HEALTH_TEXT.getWidth() // 2 + 15),
            self.__A_TOWER.getY() + 95)
        self.__A_TOWER_HEALTH_BAR = Box(100, 10)
        self.__A_TOWER_HEALTH_BAR.setPOS(self.__A_TOWER_HEALTH_TEXT.getX() + (
                    self.__A_TOWER_HEALTH_TEXT.getWidth() // 2 - self.__A_TOWER_HEALTH_BAR.getWidth() // 2),
                                         self.__A_TOWER_HEALTH_TEXT.getY() + self.__A_TOWER_HEALTH_TEXT.getHeight())
        self.__A_TOWER_HEALTH_BAR.setColor(Color.GREEN)

        self.__A_TOWER_DAMAGE_BAR = Box(100, 10)
        self.__A_TOWER_DAMAGE_BAR.setPOS(self.__A_TOWER_HEALTH_TEXT.getX() + (
                    self.__A_TOWER_HEALTH_TEXT.getWidth() // 2 - self.__A_TOWER_HEALTH_BAR.getWidth() // 2),
                                         self.__A_TOWER_HEALTH_TEXT.getY() + self.__A_TOWER_HEALTH_TEXT.getHeight())
        self.__A_TOWER_DAMAGE_BAR.setColor(Color.RED)

        self.__DEPLOYED_FISHES = []
        self.__DEPLOYED_HUMANS = []
        self.__LIVE_FISH_ATTACKS = []
        self.__LIVE_HUMAN_ATTACKS = []



        # --- COST OF THE UNITS --- #
        self.__DEPLOYED_FISHES = []
        self.__OCTOPUS_COST = 50
        self.__EEL_COST = 150
        self.__SWORDFISH_COST = 400


        self.__FISH_RANGE = [-40, 80, 110]
        self.__FISH_SPEED = [3.5, 3, 6]
        self.__FISH_ATTACK_COOLDOWN = [1.5, 3, 7]









        self.__OCTOPUS_COST = 75
        self.__EEL_COST = 150
        self.__SWORDFISH_COST = 400

        self.__FISH_MAX_HEALTH = [85, 150, 350]
        self.__FISH_ATTACK_DAMAGE = [7, 43, 17]

        self.__HUMAN_MAX_HEALTH = [100, 120, 150]
        self.__HUMAN_ATTACK_DAMAGE = [13, 48, 15]

        self.__FISH_SPAWN_COOLDOWN = [2.9, 5.0, 15.0]




























        self.__FISH_CURRENT_SPAWN_COOLDOWN = []
        for i in range(len(self.__FISH_SPAWN_COOLDOWN)):
            self.__FISH_CURRENT_SPAWN_COOLDOWN.append(self.__FISH_SPAWN_COOLDOWN[i]-0.3)
            self.__FISH_MAX_HEALTH[i] = round(self.__FISH_MAX_HEALTH[i] * self.__HEALTH_MULTIPLIER)
            self.__FISH_ATTACK_DAMAGE[i] = round(self.__FISH_ATTACK_DAMAGE[i] * self.__DAMAGE_MULTIPLIER)



        # - - - - - - - - - - - - - - - - - - - - #
        #   -  -   HUMAN CONFIGURATIONS    -  -   #
        # - - - - - - - - - - - - - - - - - - - - #

        self.__E_MAX_HEALTH = E_SCALING[0]
        self.__E_TOWER = MyUnit("media/enemybase1.png", None, None, self.__E_MAX_HEALTH, None, None, None, None, None,
                                None, None, None, None, None)
        self.__E_TOWER.setScale(4 / 10)
        self.__E_TOWER.setY(190)
        self.__E_TOWER.setX(-10)
        self.__TOWERS.append(self.__E_TOWER)

        self.__E_TOWER_HEALTH_TEXT = Text(f"{self.__E_MAX_HEALTH}", "ComicSans", 18)
        self.__E_TOWER_HEALTH_TEXT.setPOS(
            self.__E_TOWER.getX() + (self.__E_TOWER.getWidth() // 2 - self.__E_TOWER_HEALTH_TEXT.getWidth() // 2),
            self.__E_TOWER.getY() - 5)
        self.__E_TOWER_HEALTH_BAR = Box(100, 10)
        self.__E_TOWER_HEALTH_BAR.setPOS(self.__E_TOWER_HEALTH_TEXT.getX() + (
                    self.__E_TOWER_HEALTH_TEXT.getWidth() // 2 - self.__E_TOWER_HEALTH_BAR.getWidth() // 2),
                                         self.__E_TOWER_HEALTH_TEXT.getY() + self.__E_TOWER_HEALTH_TEXT.getHeight())
        self.__E_TOWER_HEALTH_BAR.setColor(Color.GREEN)

        self.__E_TOWER_DAMAGE_BAR = Box(100, 10)
        self.__E_TOWER_DAMAGE_BAR.setPOS(self.__E_TOWER_HEALTH_TEXT.getX() + (
                    self.__E_TOWER_HEALTH_TEXT.getWidth() // 2 - self.__E_TOWER_HEALTH_BAR.getWidth() // 2),
                                         self.__E_TOWER_HEALTH_TEXT.getY() + self.__E_TOWER_HEALTH_TEXT.getHeight())

        self.__E_TOWER_DAMAGE_BAR.setColor(Color.RED)

        self.__DEPLOYED_HUMANS = []
        self.__HUMAN_SPAWN_COOLDOWN = [8.0, 10.0, 4.0]
        self.__HUMAN_CURRENT_SPAWN_COOLDOWN = [2.0, 0.0, 4.0]

        self.__HUMAN_SPEED = [4.5, 3, 3]

        self.__HUMAN_RANGE = [-60, 200, 150]
        self.__HUMAN_ATTACK_COOLDOWN = [1.2, 2, 3]


        # E_SCALING = [TOWER HEALTH, % Damage Increase, % Health Increase]
        for i in range(len(self.__HUMAN_SPAWN_COOLDOWN)):
            self.__HUMAN_MAX_HEALTH[i] = round(self.__HUMAN_MAX_HEALTH[i] * E_SCALING[1])
            self.__HUMAN_ATTACK_DAMAGE[i] = round(self.__HUMAN_ATTACK_DAMAGE[i] * E_SCALING[2])

        #self.__LEVEL_SELECTOR = False # lets the code know that it's now going to exit level_selector
        self.__WIN = None
        self.__HEALTH_SPAWN1 = True
        self.__HEALTH_SPAWN2 = True
        self.__HEALTH_SPAWN3 = True
        self.__HEALTH_SPAWN4 = True
        self.__applyVisuals()


if __name__ == "__main__":
    GAME = Game()
    GAME.run()
