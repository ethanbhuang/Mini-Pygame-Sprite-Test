import pygame
import character
import obstacle
import button
import sys

class Controller():
    """
    A Controller class
    """

    def __init__(self, width=800, height=600):
        """
        Initializes a Controller object

        Args:
            self (Controller): a Controller object
            width (int): the display's width
            height (int): the display's height

        Returns:
            (None): None
        """

        pygame.font.init()
        self.width = width
        self.height = height
        self.windowSurface = pygame.display.set_mode((self.width,self.height))
        pygame.display.set_caption("Skeleton Eats Three Apples Then Dies")
        self.background = pygame.Surface(self.windowSurface.get_size())
        self.running = True
        self.player = character.Character((self.width/2,self.height/2),self.windowSurface)
        self.obstacles = pygame.sprite.Group()
        self.buttons = [
            button.Button(
                "Play Game",(self.width/2 - 35,self.height/2 - 15),70,30,(0,0,0),(0,255,0)
            ),
            button.Button(
                "Play Again?",(self.width/2 - 35,self.height/2 - 15),70,30,(0,0,0),(255,0,0)
            )
        ]
        self.setGame()

    def setGame(self):
        """
        Resets the game's parameter

        Args:
            self (Controller): a Controller object

        Returns:
            (None): None
        """

        self.player.lives = 3
        self.player.x, self.player.y = self.width/2, self.height/2
        self.player.setDirection("DOWN")
        self.player.animObjs[self.player.direction].pause()
        self.player.running = False
        self.obstacles.empty()
        for i in range(10):
            self.obstacles.add(obstacle.Obstacle(self.windowSurface))
        self.state = "START"

    def mainLoop(self):
        """
        The game's main loop controlling

        Args:
            self (Controller): a Controller object

        Returns:
            (None): None
        """

        while self.running:
            if self.state == "START":
                self.startLoop()
            elif self.state == "GAME":
                self.gameLoop()
            elif self.state == "END":
                self.endLoop()

    def startLoop(self):
        """
        The game's start screen

        Args:
            self (Controller): a Controller object

        Returns:
            (None): None
        """

        while self.state == "START":
            self.background.fill((255,255,255))
            self.windowSurface.blit(self.background,(0,0))
            self.buttons[0].draw(self.windowSurface)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()
                    sys.exit()

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if pygame.mouse.get_pressed()[0] and self.buttons[0].isHover(pygame.mouse.get_pos()):
                        self.state = "GAME"

            pygame.display.update()

    def gameLoop(self):
        """
        The game's game screen

        Args:
            self (Controller): a Controller object

        Returns:
            (None): None
        """

        pygame.key.set_repeat(1,50)
        while self.state == "GAME":
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP or event.key == pygame.K_w:
                        self.player.move("UP")
                    elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                        self.player.move("DOWN")
                    elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                        self.player.move("RIGHT")
                    elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                        self.player.move("LEFT")

                    if event.key == pygame.K_RSHIFT or event.key == pygame.K_LSHIFT:
                        self.player.running = True

                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP or event.key == pygame.K_w:
                        # method for this purpose
                        self.player.animObjs["UP"].pause()
                    elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                        self.player.animObjs["DOWN"].pause()
                    elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                        self.player.animObjs["RIGHT"].pause()
                    elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                        self.player.animObjs["LEFT"].pause()

                    if event.key == pygame.K_RSHIFT or event.key == pygame.K_LSHIFT:
                        self.player.running = False

                elif event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()
                    sys.exit()

            hits = pygame.sprite.spritecollide(self.player,self.obstacles, True)
            if hits:
                self.player.lives -= 1
                if self.player.lives == 0:
                    self.state = "END"

            self.obstacles.update()
            self.background.fill((66, 207, 104))
            self.windowSurface.blit(self.background,(0,0))
            self.obstacles.draw(self.windowSurface)
            self.player.animObjs[self.player.direction].blit(self.windowSurface,(self.player.x,self.player.y))
            pygame.display.update()

    def endLoop(self):
        """
        The game's end screen

        Args:
            self (Controller): a Controller object

        Returns:
            (None): None
        """

        while self.state == "END":
            self.background.fill((255,255,255))
            self.windowSurface.blit(self.background,(0,0))
            self.buttons[1].draw(self.windowSurface)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()
                    sys.exit()

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if pygame.mouse.get_pressed()[0] and self.buttons[1].isHover(pygame.mouse.get_pos()):
                        self.setGame()

            pygame.display.update()
