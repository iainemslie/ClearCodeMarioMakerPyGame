import pygame
import sys
from settings import *
from os.path import join

from pygame.image import load

from editor import Editor
from support import *


class Main:
    def __init__(self):
        pygame.init()
        self.display_surface = pygame.display.set_mode(
            (WINDOW_WIDTH, WINDOW_HEIGHT))
        self.clock = pygame.time.Clock()
        self.imports()

        self.editor = Editor(self.land_tiles)

        # cursor
        surf = load(join('graphics', 'cursors', 'mouse.png')).convert_alpha()
        cursor = pygame.cursors.Cursor((0, 0), surf)
        pygame.mouse.set_cursor(cursor)

    def imports(self):
        self.land_tiles = import_folder_dict(
            join('graphics', 'terrain', 'land'))

    def run(self):
        while True:
            dt = self.clock.tick() / 1000

            self.editor.run(dt)
            pygame.display.update()


if __name__ == '__main__':
    main = Main()
    main.run()
