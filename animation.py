import pygame


class Octattack(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.sprites = []
        self.is_animating = False
        self.sprites.append(pygame.image.load('media/octopus/oct1attack.png'))
        self.sprites.append(pygame.image.load('media/octopus/oct2attack.png'))
        self.sprites.append(pygame.image.load('media/octopus/oct3attack.png'))
        self.sprites.append(pygame.image.load('media/octopus/oct4attack.png'))
        self.sprites.append(pygame.image.load('media/octopus/oct5attack.png'))
        self.sprites.append(pygame.image.load('media/octopus/oct6attack.png'))
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.image = pygame.transform.flip(self.image, True, False)

        self.__X = pos_x
        self.__Y = pos_y
        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]


    def animate(self):
        self.is_animating = True


    def update(self):
        if self.is_animating == True:
            self.current_sprite += 0.2

            if self.current_sprite >= len(self.sprites):
                self.current_sprite = 0
                self.is_animating = False

            self.image = self.sprites[int(self.current_sprite)]
            self.image = pygame.transform.scale(self.image, (100, 100))
            self.image = pygame.transform.flip(self.image, True, False)

    def setX(self, X):
        self.__X = X
        self.rect.topleft = (self.__X, self.__Y)

    def setY(self, Y):
        self.__Y = Y
        self.rect.topleft = (self.__X, self.__Y)

    def getPOS(self):
        return self.rect

    def getX(self):
        return self.__X

    def getY(self):
        return self.__Y

class Octmove(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.sprites = []
        self.is_animating = False
        self.sprites.append(pygame.image.load('media/octopus/oct1move.png'))
        self.sprites.append(pygame.image.load('media/octopus/oct2move.png'))
        self.sprites.append(pygame.image.load('media/octopus/oct3move.png'))
        self.sprites.append(pygame.image.load('media/octopus/oct4move.png'))
        self.sprites.append(pygame.image.load('media/octopus/oct5move.png'))
        self.sprites.append(pygame.image.load('media/octopus/oct6move.png'))
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.image = pygame.transform.flip(self.image, True, False)
        self.image = pygame.transform.rotate(self.image, 50)

        self.__X = pos_x
        self.__Y = pos_y
        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]


    def animate(self):
        self.is_animating = True


    def update(self):
        if self.is_animating == True:
            self.current_sprite += 0.2

            if self.current_sprite >= len(self.sprites):
                self.current_sprite = 0
                self.is_animating = False

            self.image = self.sprites[int(self.current_sprite)]
            self.image = pygame.transform.scale(self.image, (100, 100))
            self.image = pygame.transform.flip(self.image, True, False)
            self.image = pygame.transform.rotate(self.image, 50)

    def setX(self, X):
        self.__X = X
        self.rect.topleft = (self.__X, self.__Y)

    def setY(self, Y):
        self.__Y = Y
        self.rect.topleft = (self.__X, self.__Y)

    def getPOS(self):
        return self.rect

    def getX(self):
        return self.__X

    def getY(self):
        return self.__Y


class Octidle(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.sprites = []
        self.is_animating = False
        self.sprites.append(pygame.image.load('media/octopus/oct1idle.png'))
        self.sprites.append(pygame.image.load('media/octopus/oct2idle.png'))
        self.sprites.append(pygame.image.load('media/octopus/oct3idle.png'))
        self.sprites.append(pygame.image.load('media/octopus/oct4idle.png'))
        self.sprites.append(pygame.image.load('media/octopus/oct5idle.png'))
        self.sprites.append(pygame.image.load('media/octopus/oct6idle.png'))
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.image = pygame.transform.flip(self.image, True, False)

        self.__X = pos_x
        self.__Y = pos_y
        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]


    def animate(self):
        self.is_animating = True


    def update(self):
        if self.is_animating == True:
            self.current_sprite += 0.2

            if self.current_sprite >= len(self.sprites):
                self.current_sprite = 0
                self.is_animating = False

            self.image = self.sprites[int(self.current_sprite)]
            self.image = pygame.transform.scale(self.image, (100, 100))
            self.image = pygame.transform.flip(self.image, True, False)

    def setX(self, X):
        self.__X = X
        self.rect.topleft = (self.__X, self.__Y)

    def setY(self, Y):
        self.__Y = Y
        self.rect.topleft = (self.__X, self.__Y)

    def getPOS(self):
        return self.rect

    def getX(self):
        return self.__X

    def getY(self):
        return self.__Y

class Octdeath(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.sprites = []
        self.is_animating = False
        self.sprites.append(pygame.image.load('media/octopus/oct1death.png'))
        self.sprites.append(pygame.image.load('media/octopus/oct2death.png'))
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.image = pygame.transform.flip(self.image, True, False)

        self.__X = pos_x
        self.__Y = pos_y
        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]

#
    def animate(self):
        self.is_animating = True


    def update(self):
        if self.is_animating == True:
            self.current_sprite += 0.2

            if self.current_sprite >= len(self.sprites):
                self.current_sprite = 0
                self.is_animating = False

            self.image = self.sprites[int(self.current_sprite)]
            self.image = pygame.transform.scale(self.image, (100, 100))
            self.image = pygame.transform.flip(self.image, True, False)

    def setX(self, X):
        self.__X = X
        self.rect.topleft = (self.__X, self.__Y)

    def setY(self, Y):
        self.__Y = Y
        self.rect.topleft = (self.__X, self.__Y)


    def getPOS(self):
        return self.rect

    def getX(self):
        return self.__X

    def getY(self):
        return self.__Y


class Eelattack(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.sprites = []
        self.is_animating = False
        self.sprites.append(pygame.image.load('media/eel/eel1attack.png'))
        self.sprites.append(pygame.image.load('media/eel/eel2attack.png'))
        self.sprites.append(pygame.image.load('media/eel/eel3attack.png'))
        self.sprites.append(pygame.image.load('media/eel/eel4attack.png'))
        self.sprites.append(pygame.image.load('media/eel/eel5attack.png'))
        self.sprites.append(pygame.image.load('media/eel/eel6attack.png'))
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.image = pygame.transform.flip(self.image, True, False)

        self.__X = pos_x
        self.__Y = pos_y
        self.rect = self.image.get_rect()
        self.rect.topleft = (pos_x, pos_y)


    def animate(self):
        self.is_animating = True


    def update(self):
        if self.is_animating == True:
            self.current_sprite += 0.2

            if self.current_sprite >= len(self.sprites):
                self.current_sprite = 0
                self.is_animating = False

            self.image = self.sprites[int(self.current_sprite)]
            self.image = pygame.transform.scale(self.image, (100, 100))
            self.image = pygame.transform.flip(self.image, True, False)

    def setX(self, X):
        self.__X = X
        self.rect.topleft = (self.__X, self.__Y)

    def setY(self, Y):
        self.__Y = Y
        self.rect.topleft = (self.__X, self.__Y)

    def getPOS(self):
        return self.rect

    def getX(self):
        return self.__X

    def getY(self):
        return self.__Y

pygame.init()
clock = pygame.time.Clock()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("anime")


oct_moving_sprites = pygame.sprite.Group()
eel_moving_sprites = pygame.sprite.Group()
#scuda = Scuda(100, 100)
#moving_sprites.add(scuda)

#moving_sprites2 = pygame.sprite.Group()
#boat = Boat(200, 100)
#moving_sprites2.add(boat)
#moving_sprites.add(boat)

#fish1 = Fish1(300,300)
#moving_sprites.add(fish1)

OCTATTACK = Octattack(100, 300)
oct_moving_sprites.add(OCTATTACK)

OCTMOVE = Octmove(100, 500)
oct_moving_sprites.add(OCTMOVE)

OCTIDLE = Octidle(100, 200)
oct_moving_sprites.add(OCTIDLE)

OCTDEATH = Octdeath(100, 150)
oct_moving_sprites.add(OCTDEATH)

EELATTACK = Eelattack(300, 300)
eel_moving_sprites.add(EELATTACK)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        PRESSED_KEYS = pygame.key.get_pressed()

        if event.type == pygame.KEYDOWN:
            #fish1.animate()
            OCTATTACK.animate()
            OCTMOVE.animate()
            OCTIDLE.animate()
            OCTDEATH.animate()
            EELATTACK.animate()

    # drawing
    screen.fill((0,0,0))
    eel_moving_sprites.draw(screen)
    eel_moving_sprites.update()

    oct_moving_sprites.draw(screen)
    oct_moving_sprites.update()
    pygame.display.flip()
    clock.tick(60)
