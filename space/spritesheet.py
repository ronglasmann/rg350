import pygame


class SpriteSheet:
    def __init__(self, filename, color_key=None):
        try:
            self.sheet = pygame.image.load(filename).convert()
            if color_key is not None:
                if color_key is -1:
                    color_key = self.sheet.get_at((0, 0))
                self.sheet.set_colorkey(color_key, pygame.RLEACCEL)
        except pygame.error, message:
            print 'Unable to load spritesheet image:', filename
            raise SystemExit(message)

    # Load a specific image from a specific rectangle
    def image_at(self, rectangle):
        """Loads image from x,y,x+offset,y+offset"""
        rect = pygame.Rect(rectangle)
        image = pygame.Surface(rect.size).convert()
        image.blit(self.sheet, (0, 0), rect)
        return image

    # Load a whole bunch of images and return them as a list
    def images_at(self, rects, colorkey=None):
        """Loads multiple images, supply a list of coordinates"""
        return [self.image_at(rect, colorkey) for rect in rects]

    # Load a whole strip of images
    def load_strip(self, rect, image_count, colorkey=None):
        """Loads a strip of images and returns them as a list"""
        tups = [(rect[0] + rect[2] * x, rect[1], rect[2], rect[3])
                for x in range(image_count)]
        return self.images_at(tups, colorkey)
