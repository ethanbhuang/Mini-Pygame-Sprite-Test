from main import pygame
import animatedSprite, pyganim

class Character(pygame.sprite.Sprite):
    """
    A Character class with properties for position, speed, and lives
    """

    def __init__(self,pos,screen):
        """
        Initializes a Character object

        Args:
            self (Character) a Character object
            pos (tuple): a tuple containing an x and y integer
            screen (pygame.Surface) a pygame surface object

        Returns:
            (None): None
        """

        pygame.sprite.Sprite.__init__(self)
        self.SCREEN_LIMITS = screen.get_size()
        self.x, self.y = pos
        self.rect = pygame.Rect(self.x,self.y,64,64)
        self.lives = 3
        self.speed = 2
        self.running = False
        self.direction = "DOWN"
        # initializing pyganim objects
        anims = [
            animatedSprite.AnimatedSprite(
                "assets/sprite_sheet.png",64,0,64,64,8,200),
            animatedSprite.AnimatedSprite(
                "assets/sprite_sheet.png",64,64,64,64,8,200),
            animatedSprite.AnimatedSprite(
                "assets/sprite_sheet.png",64,128,64,64,8,200),
            animatedSprite.AnimatedSprite(
                "assets/sprite_sheet.png",64,192,64,64,8,200)
        ]
        anims = [anims[i].getAnimatedSprite() for i in range(4)]
        self.animObjs = {
            "UP":anims[0],
            "LEFT":anims[1],
            "DOWN":anims[2],
            "RIGHT":anims[3]
        }
        self.animObjs[self.direction].pause()

    def setDirection(self,direction):
        """
        Changes the object's direction

        Args:
            self (Character): a Controller object
            direction (str): a string correlating to animObjs

        Returns:
            (None): None
        """

        if self.direction != direction:
            self.direction = direction

    def move(self, direction):
        """
        Change's the object's position

        Args:
            self (Character): a Character Object
            direction (str): a string correlating to animObjs

        Returns:
            (None): None
        """

        if self.running == True:
            self.speed = 4
        else:
            self.speed = 2

        if direction == "UP":
            self.setDirection(direction)
            self.animObjs[self.direction].play()

            if not self.y - self.speed < 0:
                self.y -= self.speed

        elif direction == "DOWN":
            self.setDirection(direction)
            self.animObjs[self.direction].play()

            if not self.y + self.speed > self.SCREEN_LIMITS[1] - 64:
                self.y += self.speed

        elif direction == "LEFT":
            self.setDirection(direction)
            self.animObjs[self.direction].play()

            if not self.x - self.speed < 0:
                self.x -= self.speed

        elif direction == "RIGHT":
            self.setDirection(direction)
            self.animObjs[self.direction].play()

            if not self.x + self.speed > self.SCREEN_LIMITS[0] - 64:
                self.x += self.speed

        self.rect.x, self.rect.y = self.x, self.y
