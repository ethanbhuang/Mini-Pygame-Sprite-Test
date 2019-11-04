import pygame

class Button:
    """
    A Button class
    """

    def __init__(self,text,pos,
                width,height,t_color,bg_color):
        """
        A short description.

        A bit longer description.

        Args:
            self (Button): a Button object
            text (str): text to be rendered
            pos (tuple): a tuple with x,y coordinates
            width (int): the width of the button
            height (int): the height of the button
            t_color (tuple): a tuple with r,g,b values for the text
            bg_color (tuple): a tuple with r,g,b values for the text background

        Returns:
            (None): None
        """

        pygame.font.init()
        self.font = pygame.font.Font(None, 16)
        self.text = text
        self.rendered_text = self.font.render(text,True,t_color)
        self.x, self.y = pos[0], pos[1]
        self.width, self.height = width, height
        self.background = pygame.Surface((self.width,self.height))
        self.background.fill(bg_color)

    def draw(self, surface):
        """
        Blits both text and background onto a surface

        Args:
            self (Button): a Button object
            surface (pygame.Surface): a pygame Surface

        Returns:
            (None): None
        """

        surface.blit(self.background,(self.x,self.y))
        surface.blit(self.rendered_text, (
            self.x + (self.width - self.font.size(self.text)[0])/2,
            self.y + (self.height - self.font.size(self.text)[1])/2,
        ))

    def isHover(self,mouse_pos):
        """
        Determines whether the mouse is hovering over the button

        Args:
            self (Button): a Button object
            mouse_pos (tuple): a tuple containing x,y coordinates

        Returns:
            (None): None
        """

        if mouse_pos[0] > self.x and mouse_pos[0] < self.x + self.width:
            if mouse_pos[1] > self.y and mouse_pos[1] < self.y + self.height:
                return True
        return False
