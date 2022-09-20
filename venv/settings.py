class Settings:
    """A class store all settings for game"""
    def __init__(self):
        """initialize game settings"""
        # Screen Settings
        self.screen_width = 1366
        self.screen_height = 768
        self.bg_color = (230,230,230)

        # Ship Settings

        self.ship_limit = 3

        # Bullets Settings

        self.bullet_width = 1000
        self.bullet_height = 15
        self.bullet_color = (224,85,4)
        self.bullet_allowed = 10

        # Alien Settings

        self.fleet_drop_speed  = 10


        self.speedup_scale = 1.1

        self.initialize_dynamic_settings()


    def initialize_dynamic_settings(self):
        self.ship_speed = 1.5
        self.bullet_speed = 3.0
        self.alien_speed = 1.0
        self.fleet_direction = 1

    def increase_speed(self):
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale




