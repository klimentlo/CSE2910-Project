import pygame

class Scuda(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.sprites = []
        self.is_animating = False
        self.sprites.append(pygame.image.load('media/00-removebg-preview.png'))
        self.sprites.append(pygame.image.load('media/01-removebg-preview.png'))
        self.sprites.append(pygame.image.load('media/02-removebg-preview.png'))
        self.sprites.append(pygame.image.load('media/03-removebg-preview.png'))
        self.sprites.append(pygame.image.load('media/10-removebg-preview.png'))
        self.sprites.append(pygame.image.load('media/11-removebg-preview.png'))
        self.sprites.append(pygame.image.load('media/12-removebg-preview.png'))
        self.sprites.append(pygame.image.load('media/13-removebg-preview.png'))
        self.sprites.append(pygame.image.load('media/20-removebg-preview.png'))
        self.sprites.append(pygame.image.load('media/21-removebg-preview.png'))
        self.sprites.append(pygame.image.load('media/22-removebg-preview.png'))
        self.sprites.append(pygame.image.load('media/23-removebg-preview.png'))
        self.sprites.append(pygame.image.load('media/30-removebg-preview.png'))
        self.sprites.append(pygame.image.load('media/31-removebg-preview.png'))
        self.sprites.append(pygame.image.load('media/32-removebg-preview.png'))
        self.sprites.append(pygame.image.load('media/33-removebg-preview.png'))
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

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

class Boat(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.sprites = []
        self.is_animating = False
        self.sprites.append(pygame.image.load('media/submarine2.png'))
        self.sprites.append(pygame.image.load('media/submarine4.png'))
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

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



pygame.init()
clock = pygame.time.Clock()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("anime")


moving_sprites = pygame.sprite.Group()
scuda = Scuda(100, 100)
moving_sprites.add(scuda)

#moving_sprites2 = pygame.sprite.Group()
boat = Boat(200, 100)
#moving_sprites2.add(boat)
moving_sprites.add(boat)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        PRESSED_KEYS = pygame.key.get_pressed()

        if event.type == pygame.KEYDOWN:
            scuda.animate()
            boat.animate()

    # drawing
    screen.fill((0,0,0))

    moving_sprites.draw(screen)
    moving_sprites.update()
    pygame.display.flip()
    clock.tick(60)
