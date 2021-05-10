import sys
import pygame
import self as self

from ship import Ship
from bullet import Bullet
from alien import Alien

from settings import Settings


class AlienInvasion:

    def __init__(self):

        pygame.init()
        self.settings = Settings()

        # FULL SCREEN GAME
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height

        # self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))

        self.bg_image = pygame.image.load("images/spacebg.png")
        self.bg_image = pygame.transform.scale(self.bg_image, (self.settings.screen_width, self.settings.screen_height))

        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)

        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self.create_fleet()

    def _check_events(self):
        # responds to key and mouse events
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_DELETE):
                sys.exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                self.fire_bullet()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.ship._moving_right = True
                elif event.key == pygame.K_LEFT:
                    self.ship._moving_left = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.ship._moving_right = False
                elif event.key == pygame.K_LEFT:
                    self.ship._moving_left = False

    def fire_bullet(self):

        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def create_fleet(self):
        # Makes an alien
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)

        ship_height = self.ship.rect.height
        available_space_y = (self.settings.screen_height - ((3 * alien_height) - ship_height))
        number_rows = available_space_y // (2 * alien_height)

        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                self.create_alien(alien_number, row_number)

    def create_alien(self, alien_number, row_number):
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + (2 * alien_width) * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + (2 * alien.rect.height) * row_number
        self.aliens.add(alien)

    def _update_screen(self):

        # Updates image on the screen and flip to a new screen
        self.screen.fill(self.settings.bg_color)
        self.screen.blit(self.bg_image, (0, 0))
        self.ship.blitme()

        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

        self.aliens.draw(self.screen)

        pygame.display.flip()

    def run_game(self):

        while True:
            self._check_events()
            self.ship.update()
            self.bullets.update()
            self._update_screen()


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
