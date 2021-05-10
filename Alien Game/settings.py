import pygame
import ship


class Settings:

    def __init__(self):
        # Initialize game settings

        #game settings
        self.screen_width = 1280
        self.screen_height = 720
        self.bg_color = ((136, 17, 240))

        #ship settings
        self.ship_speed = self.screen_width // 25

        #bullet settings
        self.bullet_width = 3
        self.bullet_height = 12
        self.bullet_speed = 10.0
        self.bullet_color = ((241, 64, 21))
        self.bullets_allowed = 10
