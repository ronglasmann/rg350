import os
import sys
import pygame

from spritesheet import SpriteSheet

# Define the screen size. This is the exact size of the RG350 screen.
WIDTH, HEIGHT = 320, 240
BLACK = 0, 0, 0


class SpaceGame:

    def __init__(self, width, height):
        pygame.init()
        pygame.mouse.set_visible(False)

        self._screen = pygame.display.set_mode((width, height))
        self._ship = Ship()

    def run(self):
        while True:
            # Read the next game event.
            for event in pygame.event.get():
                # If this event was a keypress, exit the app.
                if event.type == pygame.KEYDOWN:
                    sys.exit()

            # TODO update position for the ship

            # First, fill the screen with a black color.
            self._screen.fill(BLACK)

            self._ship.draw(self._screen)

            pygame.display.flip()


class Ship:

    def __init__(self):
        current_path = os.path.dirname(__file__)
        self._image_path = os.path.join(current_path, 'images')
        self._sprite_sheet = SpriteSheet(os.path.join(self._image_path, "sprites.png"), color_key=-1)
        self._ship = self._sprite_sheet.image_at((66, 14, 35, 32))
        self._ship_rect = self._ship.get_rect()

    def move(self, speed):
        self._ship_rect = self._ship_rect.move(speed)

    def draw(self, screen):
        screen.blit(self._ship, self._ship_rect)


if __name__ == '__main__':
    game = SpaceGame(WIDTH, HEIGHT)
    game.run()
