class Settings:
    """A class store all settings for game"""
    def __init__(self):
        """initialize game settings"""
        # Screen Settings
        self.screen_width = 1366
        self.screen_height = 768
        self.bg_color = (0,0,0)

        # Ship Settings
        self.ship_speed = 1.5

        # Bullets Settings
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (224,85,4)
        self.bullet_allowed = 3

