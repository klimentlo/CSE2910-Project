import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.sprites = []
        self.sprites.append(pygame.image.load('media/00.png'))
        self.sprites.append(pygame.image.load('media/01.png'))
        self.sprites.append(pygame.image.load('media/02.png'))
        self.sprites.append(pygame.image.load('media/03.png'))
        self.sprites.append(pygame.image.load('media/10.png'))
        self.sprites.append(pygame.image.load('media/11.png'))
        self.sprites.append(pygame.image.load('media/12.png'))
        self.sprites.append(pygame.image.load('media/13.png'))
        self.sprites.append(pygame.image.load('media/20.png'))
        self.sprites.append(pygame.image.load('media/21.png'))
        self.sprites.append(pygame.image.load('media/22.png'))
        self.sprites.append(pygame.image.load('media/23.png'))
        self.sprites.append(pygame.image.load('media/30.png'))
        self.sprites.append(pygame.image.load('media/31.png'))
        self.sprites.append(pygame.image.load('media/32.png'))
        self.sprites.append(pygame.image.load('media/33.png'))
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]


pygame.init()
clock = pygame.time.Clock()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("anime")


moving_sprites = pygame.sprite.Group()
player = Player(100, 100)
moving_sprites.add(player)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # drawing
    screen.fill((0,0,0))
    moving_sprites.draw(screen)
    pygame.display.flip()
    clock.tick(60)
