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


class Eelmove(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.sprites = []
        self.is_animating = False
        self.sprites.append(pygame.image.load('media/eel/eel1move.png'))
        self.sprites.append(pygame.image.load('media/eel/eel2move.png'))
        self.sprites.append(pygame.image.load('media/eel/eel3move.png'))
        self.sprites.append(pygame.image.load('media/eel/eel4move.png'))
        self.sprites.append(pygame.image.load('media/eel/eel5move.png'))
        self.sprites.append(pygame.image.load('media/eel/eel6move.png'))

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


class Eelidle(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.sprites = []
        self.is_animating = False
        self.sprites.append(pygame.image.load('media/eel/eel1idle.png'))
        self.sprites.append(pygame.image.load('media/eel/eel2idle.png'))
        self.sprites.append(pygame.image.load('media/eel/eel3idle.png'))
        self.sprites.append(pygame.image.load('media/eel/eel4idle.png'))
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


class Eeldeath(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.sprites = []
        self.is_animating = False
        self.sprites.append(pygame.image.load('media/eel/eel1death.png'))
        self.sprites.append(pygame.image.load('media/eel/eel2death.png'))
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


class Swordattack(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.sprites = []
        self.is_animating = False
        self.sprites.append(pygame.image.load('media/sword/sword1attack.png'))
        self.sprites.append(pygame.image.load('media/sword/sword2attack.png'))
        self.sprites.append(pygame.image.load('media/sword/sword3attack.png'))
        self.sprites.append(pygame.image.load('media/sword/sword4attack.png'))
        self.sprites.append(pygame.image.load('media/sword/sword5attack.png'))
        self.sprites.append(pygame.image.load('media/sword/sword6attack.png'))
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.image = pygame.transform.flip(self.image, False, False)

        self.__X = pos_x
        self.__Y = pos_y
        self.rect = self.image.get_rect()
        self.rect.topleft = (pos_x, pos_y)

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
            self.image = pygame.transform.flip(self.image, False, False)

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


class Swordmove(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.sprites = []
        self.is_animating = False
        self.sprites.append(pygame.image.load('media/sword/sword1move.png'))
        self.sprites.append(pygame.image.load('media/sword/sword2move.png'))
        self.sprites.append(pygame.image.load('media/sword/sword3move.png'))
        self.sprites.append(pygame.image.load('media/sword/sword4move.png'))
        self.sprites.append(pygame.image.load('media/sword/sword5move.png'))
        self.sprites.append(pygame.image.load('media/sword/sword6move.png'))

        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.image = pygame.transform.flip(self.image, False, False)

        self.__X = pos_x
        self.__Y = pos_y
        self.rect = self.image.get_rect()
        self.rect.topleft = (pos_x, pos_y)

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
            self.image = pygame.transform.flip(self.image, False, False)

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

class Sworddeath(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.sprites = []
        self.is_animating = False
        self.sprites.append(pygame.image.load('media/sword/sword1attack.png'))
        self.sprites.append(pygame.image.load('media/sword/sword1death.png'))
        self.sprites.append(pygame.image.load('media/sword/sword2death.png'))
        self.sprites.append(pygame.image.load('media/sword/sword3death.png'))
        self.sprites.append(pygame.image.load('media/sword/sword4death.png'))
        self.sprites.append(pygame.image.load('media/sword/sword5death.png'))
        self.sprites.append(pygame.image.load('media/sword/sword6death.png'))

        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.image = pygame.transform.flip(self.image, False, False)

        self.__X = pos_x
        self.__Y = pos_y
        self.rect = self.image.get_rect()
        self.rect.topleft = (pos_x, pos_y)

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
            self.image = pygame.transform.flip(self.image, False, False)

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


class Swordidle(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.sprites = []
        self.is_animating = False
        self.sprites.append(pygame.image.load('media/sword/sword1idle.png'))
        self.sprites.append(pygame.image.load('media/sword/sword2idle.png'))
        self.sprites.append(pygame.image.load('media/sword/sword3idle.png'))
        self.sprites.append(pygame.image.load('media/sword/sword4idle.png'))

        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.image = pygame.transform.flip(self.image, False, False)

        self.__X = pos_x
        self.__Y = pos_y
        self.rect = self.image.get_rect()
        self.rect.topleft = (pos_x, pos_y)

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
            self.image = pygame.transform.flip(self.image, False, False)

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


class Wandattack(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.sprites = []
        self.is_animating = False
        self.sprites.append(pygame.image.load('media/wand/wand1attack.png'))
        self.sprites.append(pygame.image.load('media/wand/wand2attack.png'))
        self.sprites.append(pygame.image.load('media/wand/wand3attack.png'))
        self.sprites.append(pygame.image.load('media/wand/wand4attack.png'))
        self.sprites.append(pygame.image.load('media/wand/wand5attack.png'))
        self.sprites.append(pygame.image.load('media/wand/wand6attack.png'))

        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.image = pygame.transform.flip(self.image, False, False)

        self.__X = pos_x
        self.__Y = pos_y
        self.rect = self.image.get_rect()
        self.rect.topleft = (pos_x, pos_y)

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
            self.image = pygame.transform.flip(self.image, False, False)

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

if __name__ == "__main__":
    pygame.init()
    clock = pygame.time.Clock()

    screen_width = 800
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("anime")


    oct_moving_sprites = pygame.sprite.Group()
    eel_moving_sprites = pygame.sprite.Group()
    human_sword_moving_sprites = pygame.sprite.Group()
    human_wand_moving_sprites = pygame.sprite.Group()

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

    EELMOVE = Eelmove(300, 100)
    eel_moving_sprites.add(EELMOVE)

    EELIDLE = Eelidle(300, 200)
    eel_moving_sprites.add(EELIDLE)

    EELDEATH = Eeldeath(300, 150)
    eel_moving_sprites.add(EELDEATH)

    SWORDATTACK = Swordattack(300, 150)
    human_sword_moving_sprites.add(SWORDATTACK)

    SWORDMOVE = Swordmove(400, 200)
    human_sword_moving_sprites.add(SWORDMOVE)

    SWORDDEATH = Sworddeath(400, 300)
    human_sword_moving_sprites.add(SWORDDEATH)

    SWORDIDLE = Swordidle(400, 400)
    human_sword_moving_sprites.add(SWORDIDLE)

    WANDATTACK = Wandattack(500, 400)
    human_sword_moving_sprites.add(WANDATTACK)

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
                EELMOVE.animate()
                EELIDLE.animate()
                EELDEATH.animate()
                SWORDATTACK.animate()
                SWORDMOVE.animate()
                SWORDDEATH.animate()
                SWORDIDLE.animate()
                WANDATTACK.animate()

        # drawing
        screen.fill((0,0,0))
        eel_moving_sprites.draw(screen)
        eel_moving_sprites.update()

        oct_moving_sprites.draw(screen)
        oct_moving_sprites.update()

        human_sword_moving_sprites.draw(screen)
        human_sword_moving_sprites.update()

        human_wand_moving_sprites.draw(screen)
        human_wand_moving_sprites.update()
        pygame.display.flip()
        clock.tick(60)
