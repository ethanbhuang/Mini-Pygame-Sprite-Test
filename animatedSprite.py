import pyganim

class AnimatedSprite:
    def __init__(self, img_file, x, y,
                width, height, n_frames, frame_length):
        self.rects = [(i * width + x,y,width,height) for i in range(n_frames)]
        self.images = pyganim.getImagesFromSpriteSheet(img_file,rects=self.rects)
        self.frames = list(zip(self.images, [frame_length] * len(self.images)))
        self.animObj = pyganim.PygAnimation(self.frames)

    def getAnimatedSprite(self):
        return self.animObj
