from settings import *
from player import Player
from sprites import *

from random import randint

class Game:
    def __init__(self):
        #setup
        pygame.init()
        self.display_surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption('Survivor')
        self.clock = pygame.time.Clock()
        self.running = True

        #groups
        self.all_sprites = pygame.sprite.Group()
        self.collision_sprites = pygame.sprite.Group()
        #sprites
        self.player = Player((400,300), self.all_sprites, self.collision_sprites)
        for i in range(8):
            x,y = randint (0, SCREEN_WIDTH), randint(0, SCREEN_HEIGHT)
            w, h = randint(60, 100), randint(50, 100)
            CollisionSprite((x, y), (w, h), (self.all_sprites, self.collision_sprites))

    def run(self):
        #dt
        while self.running:
            dt = self.clock.tick() / 1000
        
            # event loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            #update
            self.all_sprites.update(dt)

            #draw
            self.display_surface.fill('darkgray')
            self.all_sprites.draw(self.display_surface)
            pygame.display.update()

        pygame.quit()
        
if __name__ == '__main__':
    game = Game()
    game.run()

