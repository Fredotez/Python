import pygame


class Ship:

    def __init__(self, ai_game):
        # Initialize the ship and set its starting pos

        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        self.settings = ai_game.settings

        # load ship img and get its rect
        self.image = pygame.image.load('images/ship.png')
        self.rect = self.image.get_rect()
        # Start each mew ship at the bottom of the screen
        self.rect.midbottom = self.screen_rect.midbottom

        self._moving_right = False
        self._moving_left = False

        self.x = float(self.rect.x)

    def blitme(self):
        # Draw ship at its current location
        self.screen.blit(self.image, self.rect)

    def update(self):

        if self._moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self._moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        self.rect.x = self.x

