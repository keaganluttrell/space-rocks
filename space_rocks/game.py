import pygame


class SpaceRocks:

    def __init__(self):
        self.__init_pygame()
        self.screen = pygame.display.set_mode((800, 600))

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
        pass

    def __draw(self):
        self.screen.fill((0, 0, 255))
        pygame.display.flip()
