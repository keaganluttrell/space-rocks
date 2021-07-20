import pygame

# make a score algorithm
# show a time
# show stats, bullets fired, hit %
# Create a score based off time and accuracy

from utils import get_random_position, load_sprite, print_text, print_time, print_bullets
from models import Asteroid, Spaceship
from pygame import Color


class SpaceRocks:
    MIN_ASTEROID_DISTANCE = 250

    def __init__(self):
        self.game_over = False
        self.__init_pygame()
        self.screen = pygame.display.set_mode((800, 600))
        self.background = load_sprite("space", False)
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 32)
        self.message = ''

        self.time = 0
        self.click = 0
        self.bullets_fired = 0
        self.bullets_hit = 0

        self.asteroids = []
        self.bullets = []
        self.spaceship = Spaceship((400, 300), self.bullets.append)

        for _ in range(6):
            while True:
                position = get_random_position(self.screen)
                if position.distance_to(self.spaceship.position) > self.MIN_ASTEROID_DISTANCE:
                    break
            self.asteroids.append(Asteroid(position, self.asteroids.append))

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
            elif self.spaceship and event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                self.spaceship.shoot()
                self.bullets_fired += 1
            elif self.game_over:
                if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                    self.game_over = True
                    self.message = ''
                    self = SpaceRocks()
                    self.main_loop()

        is_key_pressed = pygame.key.get_pressed()
        if self.spaceship:
            if is_key_pressed[pygame.K_RIGHT]:
                self.spaceship.rotate(clockwise=True)
            elif is_key_pressed[pygame.K_LEFT]:
                self.spaceship.rotate(clockwise=False)
            elif is_key_pressed[pygame.K_UP]:
                self.spaceship.accelerate()

    def _process_game_logic(self):
        for game_object in self._get_game_objects():
            game_object.move(self.screen)

        if self.spaceship:
            for asteroid in self.asteroids:
                if asteroid.collides_with(self.spaceship):
                    self.spaceship = None
                    self.game_over = True
                    self.message = 'Game Over! Press ENTER to play again'
                    break

        for bullet in self.bullets[:]:
            for asteroid in self.asteroids[:]:
                if asteroid.collides_with(bullet):
                    self.asteroids.remove(asteroid)
                    self.bullets.remove(bullet)
                    asteroid.split()
                    self.bullets_hit += 1
                    break

        for bullet in self.bullets[:]:
            if not self.screen.get_rect().collidepoint(bullet.position):
                self.bullets.remove(bullet)

        if not self.asteroids and self.spaceship:
            self.message = 'You Win! Press ENTER to play again'
            self.game_over = True

    def _get_game_objects(self):
        objs = [*self.asteroids, *self.bullets]
        if self.spaceship:
            objs.append(self.spaceship)
        return objs

    def __draw(self):
        self.screen.blit(self.background, (0, 0))

        for game_object in self._get_game_objects():
            game_object.draw(self.screen)

        if self.message:
            print_text(self.screen, self.message, self.font)

        self.click += 1
        self.time += 1 if not self.game_over and self.click % 60 == 0 else 0
        print_time(self.screen, str(self.time), self.font)
        print_bullets(
            self.screen, f'{self.bullets_fired} {self.bullets_hit}', self.font, Color('Tomato'))

        pygame.display.flip()
        self.clock.tick(60)
