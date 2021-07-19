import pygame

from utils import load_sprite
from models import Spaceship


class SpaceRocks:

    def __init__(self):
        self.__init_pygame()
        self.screen = pygame.display.set_mode((800, 600))
        self.background = load_sprite("space", False)
        self.clock = pygame.time.Clock()
        self.spaceship = Spaceship((400, 300))

    def main_loop(self):
        while True:
            self.__handle_input()
            self._process_game_logic()
            self.__draw()

    def __init_pygame(self):
        pygame.init()
        pygame.display.set_caption("Space Rocks")

    def __handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (
                event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE
            ):
                quit()

    def _process_game_logic(self):
        self.spaceship.move()

    def __draw(self):
        self.screen.blit(self.background, (0, 0))
        self.spaceship.draw(self.screen)
        pygame.display.flip()
        self.clock.tick(60)
