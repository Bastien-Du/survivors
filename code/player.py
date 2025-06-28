from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pygame.image.load(join('images', 'player', 'down', '0.png')).convert_alpha()
        self.rect = self.image.get_frect(center = pos)

        # movement
        self.direction = pygame.Vector2()
        self.speed = PLAYER_SPEED

    def input(self):
        keys = pygame.key.get_pressed()
		
        self.direction.x = int(keys[pygame.K_d]) - (keys[pygame.K_q])
        self.direction.y = int(keys[pygame.K_s]) - (keys[pygame.K_z])
        self.direction = self.direction.normalize() if self.direction else self.direction


    def move(self, dt):
        self.rect.center += self.direction * self.speed * dt

    def update(self, dt):
        self.input()
        self.move(dt)