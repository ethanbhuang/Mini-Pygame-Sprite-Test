from main import pygame
import random

class Obstacle(pygame.sprite.Sprite):
    def __init__(self,screen):
        pygame.sprite.Sprite.__init__(self)
        self.SCREEN_LIMITS = screen.get_size()
        self.image = pygame.image.load("assets/apple.png")
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0,self.SCREEN_LIMITS[0])
        self.rect.y = random.randint(0,self.SCREEN_LIMITS[1])
