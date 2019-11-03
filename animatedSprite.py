import pyganim

class AnimatedSprite:
    """
    An AnimatedSprite class
    """

    def __init__(self, img_file, x, y,
                width, height, n_frames, frame_length):
        """
        Initializes an AnimatedSprite from a sprite sheet

        Args:
            self (AnimatedSprite): an AnimatedSprite object
            img_file (str): an image file's location
            x (int): the left most position of a sprite in a sprite sheet
            y (int): the top most position of a sprite in a sprite sheet
            width (int): the width of a sprite in a sprite sheet
            height (int): the height of a sprite in a sprite sheet
            n_frames (int): the number of frames in an animated sprite
            frame_length (int): length of each frame in ms

        Returns:
            (None): None
        """

        self.rects = [(i * width + x,y,width,height) for i in range(n_frames)]
        self.images = pyganim.getImagesFromSpriteSheet(img_file,rects=self.rects)
        self.frames = list(zip(self.images, [frame_length] * len(self.images)))
        self.animObj = pyganim.PygAnimation(self.frames)

    def getAnimatedSprite(self):
        """
        Returns:
            (Pyganimation): PygAnimation
        """

        return self.animObj
