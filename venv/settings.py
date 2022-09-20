class Settings:
    """A class store all settings for game"""
    def __init__(self):
        """initialize game settings"""
        # Screen Settings
        self.screen_width = 1366
        self.screen_height = 768
        self.bg_color = (230,230,230)

        # Ship Settings
        self.ship_speed = 1.5
        self.ship_limit = 3

        # Bullets Settings
        self.bullet_speed = 3.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (224,85,4)
        self.bullet_allowed = 5

        # Alien Settings
        self.alien_speed = 3
        self.fleet_drop_speed  = 50
        self.fleet_direction = 1

